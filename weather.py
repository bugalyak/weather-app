import requests

def get_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(url)
    data = response.json()

    if "results" in data and len(data["results"]) > 0:
        result = data["results"][0]
        return result["latitude"], result["longitude"]
    else:
        print("Город не найден.")
        return None, None

def get_weather(lat, lon):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )
    response = requests.get(url)
    data = response.json()

    if "current_weather" in data:
        weather = data["current_weather"]
        return weather
    else:
        print("Не удалось получить данные о погоде.")
        return None

def main():
    city = input("Введите название города: ")

    lat, lon = get_coordinates(city)

    if lat is not None and lon is not None:
        weather = get_weather(lat, lon)

        if weather:
            print(f"\nПогода в городе {city.title()}:")
            print(f"Температура: {weather['temperature']}°C")
            print(f"Скорость ветра: {weather['windspeed']} км/ч")
            print(f"Время обновления: {weather['time']}")
        else:
            print("Ошибка при получении погоды.")
    else:
        print("Ошибка при получении координат.")

if __name__ == "__main__":
    main()
