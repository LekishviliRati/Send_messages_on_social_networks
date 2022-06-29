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
    """"""
    header = {
        'Authorization': 'OTkxNjE1NjI1OTEyOTA5ODQ0.GiGOV_.IE_lplPZTCYYxznZ-GghZLEYPfyB-s31MDxd3o'
    }

    example = {
        'content': '{}'.format(input)
    }

    response = requests.post("https://discord.com/api/v9/channels/991618332895752255/messages", data=example, headers=header)
    return response


message = "test depuis ANNECY"
send_message(message)
