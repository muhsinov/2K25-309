class StreetLight:
    def __init__(self, id: str):
        self.id = id
        self.on = False

    def start(self):
        self.on = True
        print(f"StreetLight {self.id} ON")

    def stop(self):
        self.on = False
        print(f"StreetLight {self.id} OFF")

    def status(self):
        return {"id": self.id, "on": self.on}
