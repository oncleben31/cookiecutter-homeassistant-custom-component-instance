"""Binary sensor platform for Cookiecutter Home Assistant Custom Component Instance."""
from homeassistant.components.binary_sensor import BinarySensorDevice

from .const import BINARY_SENSOR
from .const import BINARY_SENSOR_DEVICE_CLASS
from .const import DEFAULT_NAME
from .const import DOMAIN
from .entity import CookiecutterHomeassistantCustomComponentInstanceEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup binary_sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        [
            CookiecutterHomeassistantCustomComponentInstanceBinarySensor(
                coordinator, entry
            )
        ]
    )


class CookiecutterHomeassistantCustomComponentInstanceBinarySensor(
    CookiecutterHomeassistantCustomComponentInstanceEntity, BinarySensorDevice
):
    """cookiecutter_homeassistant_custom_component_instance binary_sensor class."""

    @property
    def name(self):
        """Return the name of the binary_sensor."""
        return f"{DEFAULT_NAME}_{BINARY_SENSOR}"

    @property
    def device_class(self):
        """Return the class of this binary_sensor."""
        return BINARY_SENSOR_DEVICE_CLASS

    @property
    def is_on(self):
        """Return true if the binary_sensor is on."""
        return self.coordinator.data.get("bool_on", False)
