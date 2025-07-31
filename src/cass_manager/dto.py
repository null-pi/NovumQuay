import enum
from pydantic import BaseModel


class ProvidedBy(str, enum.Enum):
    USER = "user"
    SYSTEM = "system"


class MessageType(str, enum.Enum):
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"


class ChatMessage(BaseModel):
    providedBy: ProvidedBy
    messageType: MessageType
    content: str

    def __str__(self):
        return f"{self.providedBy}: {self.content}"