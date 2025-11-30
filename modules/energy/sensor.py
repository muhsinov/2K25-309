class EnergySensorFlyweight:
    def __init__(self, sensor_type, unit):
        self.sensor_type = sensor_type
        self.unit = unit

    def shared_info(self):
        return {
            "type": self.sensor_type,
            "unit": self.unit
        }
