from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import add_entities
from .sensor import ArsoWeatherSensor

def setup_platform(hass: HomeAssistant, config, add_entities, discovery_info=None):
    """Setup the ARSO weather sensor platform."""
    sensor = ArsonWeatherSensor()
    add_entities([sensor])

def setup(hass: HomeAssistant, config):
    """Set up the ARSO component."""
    return True
