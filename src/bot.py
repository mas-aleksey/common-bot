from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

logger = logging.getLogger('BotWorker')


class BotWorker:
    def __init__(self, token):
        self.updater = Updater(token=token)
        self.commands = {
            'start': self.help_handler,
            'help': self.help_handler,
            'chat_id': self.chat_id_handler
        }
        self.register_handlers()

    def start(self):
        self.updater.start_polling(poll_interval=2, timeout=30, read_latency=5)
        self.updater.idle()

    def register_handlers(self):
        dp = self.updater.dispatcher
        for command, handler in self.commands.items():
            dp.add_handler(CommandHandler(command, handler))
            logger.info('Register command: \'%s\'', command)
        dp.add_error_handler(self.error)

    @property
    def help_text(self):
        help_text = 'Привет!\n{0}'
        commands = '\n'.join(['/{0}'.format(com) for com in self.commands.keys()])
        return help_text.format(commands)

    def help_handler(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /start is issued."""
        update.message.reply_text(self.help_text)

    def chat_id_handler(self, update: Update, context: CallbackContext):
        """Send a message when the command /start is issued."""
        update.message.reply_text(update.message.chat_id)

    @staticmethod
    def error(bot, update, err):
        logger.warning('Update "%s" caused error "%s"' % (update, err))
