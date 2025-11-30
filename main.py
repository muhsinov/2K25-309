# main.py
from core.controller import CentralController
from core.factories.device_factory import DeviceFactory
from core.factories.sensor_factory import SensorFactory
from core.builders.report_builder import ReportBuilder
from core.adapters.weather_adapter import WeatherAPIAdapter
from core.proxy.access_proxy import AccessProxy
from core.proxy.access_proxy import User


def main():
    print("\n===== SMART CITY SYSTEM BO'SHLANDI =====\n")


    # Singleton Controller
    controller = CentralController()

    # Proxy orqali boshqarish
    user = User("admin", True)
    proxy = AccessProxy(controller, user, controller)

    device_factory = DeviceFactory()
    sensor_factory = SensorFactory()

    street_light = device_factory.create("street_light")
    traffic_light = device_factory.create("traffic_light")
    camera = device_factory.create("camera")

    air_sensor = sensor_factory.create("air")
    energy_sensor = sensor_factory.create("energy")

    controller.register_subsystem("street_light", street_light)
    controller.register_subsystem("traffic_light", traffic_light)
    controller.register_subsystem("camera", camera)
    controller.register_subsystem("air", air_sensor)
    controller.register_subsystem("energy", energy_sensor)



    controller.start_all()
    controller.status_report()
    print("\nWeather:", controller.get_weather(user, "Tashkent"))


    print("===== DASTUR YAKUNLANDI =====")


if __name__ == "__main__":
    main()