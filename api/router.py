from fastapi import APIRouter, status

from . import load_data, schemes


class Router:

    def __init__(self):
        self.router = APIRouter()
        self.setup_routes()

    def setup_routes(self):
        
        @self.router.get(
            "/weathertomorrow", 
            description="Прогноз погоды на завтра",
            status_code=status.HTTP_200_OK, 
            response_model=schemes.WeaverTomorrowResponse
        )
        async def get_weathertomorrow(location: str):
            return load_data.get_weather_api_data(location)
            
        
        @self.router.get(
            "/weather16days", 
            description="Прогноз погоды на текущий и следующие 15 дней",
            status_code=status.HTTP_200_OK, 
            response_model=schemes.WeaverNext16DaysResponse
        )
        async def get_weather16days(location: str):
            return load_data.get_weather_api_data(location)

weatherapi = Router()