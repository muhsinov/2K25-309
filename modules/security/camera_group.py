from modules.security.camera import CameraComponent

class CameraGroup(CameraComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: CameraComponent):
        self.children.append(component)

    def start(self):
        for child in self.children:
            child.start()

    def stop(self):
        for child in self.children:
            child.stop()

    def status(self):
        return {
            "group": self.name,
            "devices": [child.status() for child in self.children]
        }
