import os

#import requests
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


# webhook_url = os.getenv("WEBHOOK_URL")
# webhook = DiscordWebhook(url=webhook_url, content='Webhook Message')
# response = webhook.execute()


# https://discord.com/api/v9/channels/991618332895752255/messages
#
# Authorization: OTkxNjE1NjI1OTEyOTA5ODQ0.GiGOV_.IE_lplPZTCYYxznZ-GghZLEYPfyB-s31MDxd3o

# payload = {
#     'content': 'depuis fichier python'
# }
#
# header = {
#     'Authorization': 'OTkxNjE1NjI1OTEyOTA5ODQ0.GiGOV_.IE_lplPZTCYYxznZ-GghZLEYPfyB-s31MDxd3o'
# }
#
# r = requests.post("https://discord.com/api/v9/channels/991618332895752255/messages", data=payload, headers=header)


# class DiscordMessage:
#     """
#     User send message on a discord channel.
#     """
#
#     def __init__(self):
#         self.send_message()
#
#     def send_message(self):
#         """"""
#         header = {
#             'Authorization': 'OTkxNjE1NjI1OTEyOTA5ODQ0.GiGOV_.IE_lplPZTCYYxznZ-GghZLEYPfyB-s31MDxd3o'
#         }
#
#         example = {
#             'content': 'Test depuis une classe'
#         }
#
#         url = str("https://discord.com/api/v9/channels/991618332895752255/messages), data={}, headers={}").\
#             format(example, header)
#
#         response = requests.post(url)
#         return response
#
#
# test = DiscordMessage()


# def send_message(input):
#     """
#     This function is set to send a message to my discord channel : "koesio server test"
#     Authorization key might change, need to be carteful.
#     """
#     header = {
#         'Authorization': 'OTkxNjE1NjI1OTEyOTA5ODQ0.GrxTwV.B7c1dB8KfDW_HQIlvrC01qWh-Fx_jySKZwbeLs'
#     }
#
#     example = {
#         'content': '{}'.format(input)
#     }
#
#     response = requests.post("https://discord.com/api/v9/channels/991618332895752255/messages", data=example, headers=header)
#     return response
#
#
# message = "RATIII"
# send_message(message)




