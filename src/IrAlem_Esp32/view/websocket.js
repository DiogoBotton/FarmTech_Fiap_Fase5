const ws = new WebSocket("ws://localhost:5000/temperature-humidity");

ws.onmessage = function (event) {
    try {
        const data = JSON.parse(event.data);
        console.log('dados do websocket:', data)
        document.getElementById("temp").innerText = data.temperature;
        document.getElementById("hum").innerText = data.humidity;
    } catch (error) {
        console.error("Erro ao processar dados:", error);
    }
};

ws.onerror = function (error) {
    console.error("Erro na conexão WebSocket:", error);
};