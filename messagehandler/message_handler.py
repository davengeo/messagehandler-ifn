from abc import abstractmethod, ABC
from typing import Any, Tuple

from kombu import Message


class MessageHandler(ABC):

    @abstractmethod
    def setup(self, params: Tuple[Any, ...]) -> None:
        pass

    @abstractmethod
    def handler(self, body: Any, message: Message) -> None:
        pass
