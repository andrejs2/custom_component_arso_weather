
import requests
from bs4 import BeautifulSoup
from homeassistant.helpers.entity import Entity

def scrape_weather_data():
    """Scrapes weather data from the ARSO website."""
    url = 'http://www.arso.gov.si/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        temperature = soup.find('span', {'id': 'temperature_element_id'})
        return temperature.text.strip() if temperature else 'Unknown'  # Ensures that if the span is not found, 'Unknown' is returned
    else:
        return 'Unavailable'  # Changed from None for clearer error status in UI

class ArsoWeatherSensor(Entity):
    """Representation of a Weather Sensor from ARSO."""

    def __init__(self):
        self._state = 'Unknown'  # Set initial state to 'Unknown'
        self._name = 'ARSO Temperature Sensor'
        self._unique_id = 'arso_temperature_sensor'

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def unique_id(self):
        """Return the unique ID of the sensor."""
        return self._unique_id

    @property
    def state(self):
        """Return the current state of the sensor."""
        return self._state

    def update(self):
        """Update the sensor state by scraping the web data."""
        self._state = scrape_weather_data()

    @property
    def extra_state_attributes(self):
        """Return additional state attributes."""
        return {'vendor': 'ARSO'}

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of the sensor."""
        return '°C'
