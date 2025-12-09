class ReportBuilder:
    def __init__(self):
        self.parts = []

    def header(self, title):
        self.parts.append(f"===== {title} =====")
        return self

    def add_subsystem(self, name, status):
        self.parts.append(f"{name}: {status}")
        return self

    def footer(self, note):
        self.parts.append(f"--- {note} ---")
        return self

    def build(self):
        return "\n".join(self.parts)
