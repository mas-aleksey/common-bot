import pytest
from telegram.ext import Updater
from src.bot import BotWorker


@pytest.fixture
def worker(mocker) -> BotWorker:

    def init_mock(*args, **kwargs):
        pass
    Updater.__init__ = init_mock
    Updater.dispatcher = mocker.Mock()
    return BotWorker('token')


def test_help_text(worker):
    assert worker.help_text == 'Привет!\n/start\n/help\n/chat_id'
