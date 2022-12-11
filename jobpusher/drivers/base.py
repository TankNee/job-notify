class BaseDriver():
    def __init__(self) -> None:
        pass

    def auth(self) -> None:
        raise NotImplementedError
        pass
        
    def send(self, to: str, subject: str, content: str, attachments) -> None:
        raise NotImplementedError
        pass