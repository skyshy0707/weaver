from datetime import datetime
from pydantic import BaseModel, AliasChoices, AliasPath, Field, field_serializer
from typing import List


def date_to_russian_strfmt(date: datetime):
    """
    Шаблон для преобразования даты в русский формат:
    `Д Мес ГГГГ г. ЧЧ:ММ`
    """
    return date.strftime("X%d X%b %Y г.").replace('X0', 'X').replace('X', '')

class WeaverItemData(BaseModel):
    conditions: str = Field(
        validation_alias=AliasChoices(
            "conditions", 
             AliasPath("values", 1, "conditions")
        ))
    datetimeStr: str = Field(
        validation_alias=AliasChoices(
            "datetimeStr", 
            AliasPath("values", 1, "datetimeStr")
        ))
    humidity: float = Field(
        validation_alias=AliasChoices(
            "humidity", 
            AliasPath("values", 1, "humidity")
        ))
    sealevelpressure: float = Field(
        validation_alias=AliasChoices(
            "sealevelpressure", 
            AliasPath("values", 1, "sealevelpressure")
        ))
    temp: float = Field(
        validation_alias=AliasChoices(
            "temp", 
            AliasPath("values", 1, "temp")
        ))
    wspd: float = Field(
        validation_alias=AliasChoices(
            "wspd", 
            AliasPath("values", 1, "wspd")
        ))

    @field_serializer("datetimeStr")
    def datetime(self, value: str):
        try:
            return date_to_russian_strfmt(datetime.fromisoformat(value))
        except ValueError:
            return date_to_russian_strfmt(datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ"))
    
    @field_serializer("sealevelpressure")
    def pressure(self, value: float):
        return round(value * 0.000987, 4)
    
class WeaverData(WeaverItemData):
    location: str

class WeaverNext16Days(BaseModel):
    values: List[WeaverItemData] = Field(default_factory=list)
    location: str


class WeaverTomorrowResponse(BaseModel):
    data: WeaverData = Field(default=None, validate_default=False)

class WeaverNext16DaysResponse(BaseModel):
    data: WeaverNext16Days
