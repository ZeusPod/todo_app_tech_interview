import requests
import os
from dotenv import load_dotenv


load_dotenv()



def get_weather(city):
    api_key =  os.getenv("API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.exceptions.HTTPError as err:
        return {'error': f"HTTP error occurred: {err}"}
    except requests.exceptions.RequestException as err:
        return {'error': f"Error occurred: {err}"}
    
