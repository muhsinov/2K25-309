from modules.lighting.street_light import StreetLight
from modules.transport.traffic_light import TrafficLight
from modules.security.single_camera import SingleCamera
from modules.energy.energy_sensor import EnergySensor

class DeviceFactory:
    def __init__(self):
        self.sl_counter = 0
        self.tl_counter = 0
        self.ca_counter = 0

    def create(self, device_type: str):
        if device_type == "street_light":
            self.sl_counter += 1
            return StreetLight(f"{device_type}-{self.sl_counter}")
        if device_type == "traffic_light":
            self.tl_counter += 1
            return TrafficLight(f"{device_type}-{self.tl_counter}")
        if device_type == "camera":
            self.ca_counter += 1
            return SingleCamera(f"{device_type}-{self.ca_counter}")
        raise ValueError("Unknown device type")
