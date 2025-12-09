import threading
class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._init()
        return cls._instance

    def _init(self):
        self.logs = []

    def info(self, msg):
        entry = f"[INFO] {msg}"
        print(entry)
        self.logs.append(entry)

    def error(self, msg):
        entry = f"[ERROR] {msg}"
        print(entry)
        self.logs.append(entry)
