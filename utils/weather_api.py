import requests


def get_weather(city):
    api_key = "4959a28a12d151d79d95f7373b244dfc"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.exceptions.HTTPError as err:
        return {'error': f"HTTP error occurred: {err}"}
    except requests.exceptions.RequestException as err:
        return {'error': f"Error occurred: {err}"}
    
