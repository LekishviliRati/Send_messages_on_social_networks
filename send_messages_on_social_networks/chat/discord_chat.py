import requests


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


def send_message(input):
    """
    This function is set to send a message to my discord channel : "koesio server test"
    Authorization key might change, need to be carteful.
    """
    header = {
        'Authorization': 'OTkxNjE1NjI1OTEyOTA5ODQ0.GpFQuQ.7e9Eu9H98D6_Ukv0TibbCeqFmp7_Ue11LOyBoI'
    }

    example = {
        'content': '{}'.format(input)
    }

    response = requests.post("https://discord.com/api/v9/channels/991618332895752255/messages", data=example, headers=header)
    return response


message = "FONCTION SEND_MESSAGE"
send_message(message)
