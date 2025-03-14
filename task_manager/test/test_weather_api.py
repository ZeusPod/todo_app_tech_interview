from django.test import TestCase
from unittest.mock import patch
from utils.weather_api import get_weather

class WeatherApiTest(TestCase):
    @patch('utils.weather_api.requests.get')
    def test_get_weather_success(self, mock_get):
        """Prueba que get_weather devuelva datos simulados correctamente."""
        mock_response = {
            "main": {"temp": 25.0, "humidity": 60},
            "weather": [{"description": "cielo despejado"}]
        }
        mock_get.return_value.json.return_value = mock_response
        mock_get.return_value.status_code = 200

        weather_data = get_weather("Santiago")
        self.assertEqual(weather_data["main"]["temp"], 25.0)
        self.assertEqual(weather_data["weather"][0]["description"], "cielo despejado")
