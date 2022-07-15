import os


from discord_webhook import DiscordWebhook
from dotenv import load_dotenv

load_dotenv()


class SendMessageToDiscord:
    def __init__(self, data=None):
        self.data = data
        self.webhook_url = os.getenv("WEBHOOK_URL")
        self.webhook = DiscordWebhook(url=self.webhook_url, content=self.data)
        self.response = self.webhook.execute()


SendMessageToDiscord()
