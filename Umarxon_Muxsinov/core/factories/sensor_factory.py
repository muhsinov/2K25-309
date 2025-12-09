from Umarxon_Muxsinov.modules.energy.sensor import EnergySensorFlyweight
from Umarxon_Muxsinov.modules.energy.energy_sensor import EnergySensor

class SensorFactory:
    _flyweights = {}

    def __init__(self):
        pass

    def _get_flyweight(self, sensor_type, unit):
        key = (sensor_type, unit)

        if key not in SensorFactory._flyweights:
            SensorFactory._flyweights[key] = EnergySensorFlyweight(sensor_type, unit)

        return SensorFactory._flyweights[key]

    def create(self, sensor_type: str):

        if sensor_type == "energy":
            fw = self._get_flyweight("energy", "kWh")
            return EnergySensor(fw.sensor_type, fw.unit)

        elif sensor_type == "air":
            fw = self._get_flyweight("air", "ppm")
            return EnergySensor(fw.sensor_type, fw.unit)

        else:
            raise ValueError("Unknown sensor type")
