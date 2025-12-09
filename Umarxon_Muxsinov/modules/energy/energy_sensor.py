class EnergySensor:
    def __init__(self, id, flyweight):
        self.id = id
        self.flyweight = flyweight
        self.value = 0

    def start(self):
        print(f"[Energy] Sensor {self.id} ACTIVATED")

    def stop(self):
        print(f"[Energy] Sensor {self.id} DEACTIVATED")

    def status(self):
        return {
            "id": self.id,
            "value": self.value,
        }
