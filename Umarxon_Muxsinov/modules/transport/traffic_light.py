class TrafficLight:
    def __init__(self, id: str):
        self.id = id
        self.active = False

    def start(self):
        self.active = True
        print(f"TrafficLight {self.id} active")

    def stop(self):
        self.active = False
        print(f"TrafficLight {self.id} inactive")

    def status(self):
        return {"id": self.id, "active": self.active}
