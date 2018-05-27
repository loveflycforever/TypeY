class ResultBuilder:
    def __init__(self, code, message, serial_number, data):
        self.code = code
        self.message = message
        self.serial_number = serial_number
        self.data = data
        self.Ro = AttributeError

    def build(self):
        return None
