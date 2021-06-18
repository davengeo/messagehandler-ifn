import os
import sys
from typing import Any, Tuple

from assertpy import assert_that
from kombu import Message

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from messagehandler.message_handler import MessageHandler  # noqa: E402

NO_SETUP: int = 5
SETUP: int = 10
HANDLED: int = 15


class TrivialHandler(MessageHandler):
    value: int = NO_SETUP

    def setup(self, params: Tuple[Any, ...]) -> None:
        self.value = params[0]

    def handler(self, body: Any, message: Message) -> None:
        self.value = HANDLED


def test_trivial_handler() -> None:
    test: TrivialHandler = TrivialHandler()
    assert_that(test.value).is_equal_to(NO_SETUP)
    test.setup((SETUP,))
    assert_that(test.value).is_equal_to(SETUP)
    test.handler(None, Message())
    assert_that(test.value).is_equal_to(HANDLED)
