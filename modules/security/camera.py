from abc import ABC, abstractmethod

class CameraComponent(ABC):
    @abstractmethod
    def start(self):
        raise NotImplementedError()

    @abstractmethod
    def stop(self):
        raise NotImplementedError()

    @abstractmethod
    def status(self):
        raise NotImplementedError()