class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin


class AccessProxy:
    def __init__(self, subsystem, user: User, controller):
        self.real = subsystem
        self.user = user
        self.controller = controller

    def turn_on_all(self):
        for subsystem in self.controller.subsystems:
            subsystem.turn_on()

    def start(self):
        if not self.user.is_admin:
            raise PermissionError("Admin rights required.")
        return self.real.start()

    def stop(self):
        if not self.user.is_admin:
            raise PermissionError("Admin rights required.")
        return self.real.stop()

    def status(self):
        return self.real.status()
