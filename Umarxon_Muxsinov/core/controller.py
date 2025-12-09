from .singleton.logger import Logger
from .adapters.weather_adapter import WeatherAPIAdapter

class CentralController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.logger = Logger()
        self.subsystems = {}

    def register_subsystem(self, name, subsystem):
        self.subsystems[name] = subsystem
        self.logger.info(f"Subsystem registered: {name}")

    def start_all(self):
        self.logger.info("Starting all subsystems...")
        for name, s in self.subsystems.items():
            s.start()
            self.logger.info(f"{name} started")

    def stop_all(self):
        self.logger.info("Stopping all subsystems...")
        for name, s in self.subsystems.items():
            s.stop()
            self.logger.info(f"{name} stopped")

    def get_weather(self, client, city):
        self.logger.info("Getting weather...")
        return WeatherAPIAdapter(client).get_weather(city)

    def status_report(self):
        report = {}
        for name, s in self.subsystems.items():
            report[name] = s.status()
        return report
