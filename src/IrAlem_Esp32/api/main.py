from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
import asyncio
import aio_pika

# Inicia o consumidor RabbitMQ quando a aplicação iniciar
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Gerencia a inicialização e finalização da aplicação
    task = asyncio.create_task(consume_queue())
    yield
    task.cancel() # Cancela o consumidor do RabbitMQ quando a aplicação fecha

app = FastAPI(
    title="FarmTech API Websocket",
    docs_url="/docs",  # URL para disponibilização do Swagger UI
    lifespan=lifespan
)

active_connections = []

RABBITMQ_URL = os.getenv('RABBITMQ_URL')
QUEUE = os.getenv('RABBITMQ_QUEUE')

@app.websocket("/temperature-humidity")
async def websocket_endpoint(websocket: WebSocket):
    # WebSocket que envia atualizações em tempo real
    await websocket.accept()
    active_connections.append(websocket)
    
    try:
        while True:
            await websocket.receive_text()
    except:
        pass
    finally:
        active_connections.remove(websocket)

async def consume_queue():
    # Consome mensagens do RabbitMQ e envia para os WebSockets
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    channel = await connection.channel()
    queue = await channel.declare_queue(QUEUE, durable=False)

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                data = message.body.decode()
                
                for ws in active_connections:
                    await ws.send_text(data)

# Libera o CORS da API para requisições via http
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)