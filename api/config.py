URL_WEATHER_API = "https://visual-crossing-weather.p.rapidapi.com/forecast"
URL_TRANSLATE_API = "https://ftapi.pythonanywhere.com/translate"


headers_weather_api = {
    'X-RapidAPI-Key': '7c9ce6cf4fmsh284ac1b5f2df364p1a8b1ajsn6428e63fc0c1',
    'X-RapidAPI-Host': 'visual-crossing-weather.p.rapidapi.com'
}

params_weather_api = {
    'aggregateHours': 24,
    'contentType': 'json',
    'lang': 'ru',
    'unitGroup': 'metric'
}

params_translate_api = {
    "dl": "en",
    "sl": "ru"
}