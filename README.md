Приложение на Python 3.8 для автоматических сообщений о погоде на завтрашний день

Позволяет в чате бота `weavertomorrow` делать запрос на естественном языке 
в виде названия географического места, чьи погодные данные требуется получить


**Команды**

*Краткая справка:*

```
/start
```

*Погодные данные на завтрашний день:*

```
<Название географического объекта>
```


!NB Настройки:

При необходимости, в файле `/api/config.py` -- в переменной `headers_weather_api` 
поменяйте параметер `` на свой*

*Получить `X-RapidAPI-Key` можно при регистрации личного кабинета в сервисе:
[visualcrossing](https://www.visualcrossing.com/sign-up) или зарегистрировавшись на [rapidapi](https://rapidapi.com/auth/sign-up?referral=/visual-crossing-corporation-visual-crossing-corporation-default/api/visual-crossing-weather/),
используя google-аккаунт.


**Запуск проекта**


*Сборка:*

```
docker-compose up -d --build

```

*Поднять контейнеры:*
```
docker-compose up
```