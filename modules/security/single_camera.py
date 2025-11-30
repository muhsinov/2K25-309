from modules.security.camera import CameraComponent

class SingleCamera(CameraComponent):
    def __init__(self, id: str):
        self.id = id
        self.active = False

    def start(self):
        self.active = True
        print(f"[Security] Camera {self.id} ON")

    def stop(self):
        self.active = False
        print(f"[Security] Camera {self.id} OFF")

    def status(self):
        return {"camera_id": self.id, "active": self.active}
