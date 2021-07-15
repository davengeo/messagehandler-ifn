from abc import abstractmethod, ABC
from typing import Any, Dict, Text

from kombu import Message


class MessageHandler(ABC):

    @abstractmethod
    def setup(self, params: Dict[Text, Any]) -> None:
        pass

    @abstractmethod
    def handler(self, body: Any, message: Message) -> None:
        pass
