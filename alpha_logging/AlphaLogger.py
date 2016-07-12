class AlphaLogger:
    instance = None

    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    @staticmethod
    def log(message):
        if AlphaLogger.instance is None:
            AlphaLogger.instance = AlphaLogger()
        AlphaLogger.instance.events.append(message)

    @staticmethod
    def reset_logger():
        AlphaLogger.instance = AlphaLogger()

    @staticmethod
    def get_messages():
        messages = []
        if AlphaLogger.instance is not None:
            for message in AlphaLogger.instance.events:
                messages.append(message)
        return messages
