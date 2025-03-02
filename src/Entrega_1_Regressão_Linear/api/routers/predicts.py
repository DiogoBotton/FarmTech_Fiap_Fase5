from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import numpy as np
import os

router = APIRouter(tags=["Predicts"])

class RequestData(BaseModel):
    CropOilPalmFruit: bool
    CropRicePaddy: bool
    Precipitation: float
    TemperatureC: float
    SpecificHumidity: float
    RelativeHumidity: float

@router.post("/predict")
async def predict(data: RequestData):
    # Caso pertencer as duas categorias, gera um erro
    if data.CropOilPalmFruit and data.CropRicePaddy:
        raise HTTPException(status_code=400, detail='O modelo só pode pertencer a uma única categoria.')

    # Adquire o caminho do modelo
    main_path = os.path.dirname(__file__)
    model_path = os.path.join(main_path, '..', 'random_forest_model_all_crops.joblib')

    # Tenta carregar o modelo, dá erro caso não encontre
    try:
        model = joblib.load(model_path)
    except:
        raise HTTPException(status_code=404, detail='Modelo não encontrado.')

    # Cria um dicionário com os mesmos nomes de colunas que o modelo foi treinado
    # Isto é necessário, pois o modelo espera que os dados tenham a mesma nomenclatura de colunas
    data_dict = {
        'Crop_Oil palm fruit': [data.CropOilPalmFruit],
        'Crop_Rice, paddy': [data.CropRicePaddy],
        'Precipitation': [data.Precipitation],
        'Temperature_C': [data.TemperatureC],
        'SpecificHumidity': [data.SpecificHumidity],
        'RelativeHumidity': [data.RelativeHumidity]
    }

    # Converte para DataFrame
    df = pd.DataFrame(data_dict)

    # Realiza a combinação de features das colunas de humidade
    df['HumidityCombined'] = df['SpecificHumidity'] * df['RelativeHumidity']
    df.drop(['SpecificHumidity', 'RelativeHumidity'], axis=1, inplace=True)

    # Seleciona as colunas necessárias para a predição
    X = df[['Crop_Oil palm fruit', 'Crop_Rice, paddy', 'Precipitation', 'HumidityCombined', 'Temperature_C']]

    predict = model.predict(X) # Realiza a predição
    predict = np.expm1(predict) # Volta para a escala original
    
    return {
        "predictValue": predict.tolist(), # Converte para lista para evitar erros de serialização
    }