"""
Модуль для загрузки данных о погоде
"""
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import requests

from . import config


ERROR_WEATHER_API_RESPONSE = JSONResponse(
    status_code=status.HTTP_400_BAD_REQUEST,
    content=jsonable_encoder({ "error": \
        "Невозможно получить данные по этому запросу. Сформулируйте "\
        "запрос более точно, добавив через запятую регион или страну или "\
        "попробуйте ещё раз."
    })
)

def get_middle_data(url: str, headers: dict=dict(), params: dict=dict()) -> dict:
    """
    Метод, получающий json-данные из внешнего api 
    с учётом обработки возможных исключений
    """
    json = {}
    while True:
        try:
            response = requests.get(url, headers=headers, params=params)
        except requests.ConnectionError:
            continue
        else:
            break
    try:
        json = response.json()
    except requests.JSONDecodeError as e:
        json.update({ "error": f"Number: {e.errno if e.errno else 'Unknown number'} - {response.reason}" })
    return json


def get_weather_api_data(location: str) -> dict:
    """
    Метод преобразует параметры запроса пользователя 
    на погоду в допустимую форму, понимаемую внешним 
    сервисом сводки погоды и возвращает данные api 
    погодного сервиса на текущий и следующие 15 дней
    или шаблон ответа в случае ошибки.
    """
    config.params_translate_api["text"] = location

    translate_data = get_middle_data(
        config.URL_TRANSLATE_API, 
        params=config.params_translate_api
    )

    try:
        location_en = translate_data\
            .get("translations", {})\
            .get("possible-translations", [])[0]
        
    except IndexError:
        return ERROR_WEATHER_API_RESPONSE
    
    config.params_weather_api["location"] = location_en

    weather_data = get_middle_data(
        config.URL_WEATHER_API,
        headers=config.headers_weather_api,
        params=config.params_weather_api
    )
    
    weather_values = weather_data\
        .get("locations", {})\
        .get(location_en, {})\
        .get("values")
    
    api_data = { 
        "data": {
            "values": weather_values,
            "location": location
        },
        
    } 
    return api_data if weather_values else ERROR_WEATHER_API_RESPONSE