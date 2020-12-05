from src.bot import BotWorker
from src import settings


def main(token):
    BotWorker(token).start()


if __name__ == '__main__':
    main(settings.TOKEN)
