import vk_api

group = vk_api.VkApi(token='token')
personal = vk_api.VkApi(token='token')

send = ''
c = ''
messages = []
i = 0
current_msg = ''
id_new = ''
sms_new = ''

friend = []

while True:
    try:
        msg = personal.method("messages.getConversations", {'offset': 0, 'count': 100, 'filter': "unread"})
        if msg["count"] >= 1:
            id = msg["items"][0]["last_message"]["from_id"]
            if id in friend:
                body = msg["items"][0]["last_message"]["text"]
                sms = str(msg["items"][0]["last_message"]["id"]) + ' ' + str(id) + ' ' + body
                if not (sms in messages):
                    messages.append(sms)
            for i in range(len(messages)):
                if messages[i] == 0:
                    continue
                k = personal.method('messages.getById', {"message_ids": messages[i]})
                if k["count"] == 0:
                    z = messages[i]
                    messages[i] = 0
                    for c in range(7, len(z)):
                        send = send + z[c]
                    for c in send:
                        if c.isalpha():
                            sms_new = sms_new + c
                    for c in send:
                        if c.isdigit():
                            id_new = id_new + c
                    id_new = id_new.rstrip()
                    if z != current_msg:
                        group.method("messages.send",
                                     {"peer_id": "436211452", "message": '[id' + id_new + '|' + sms_new + ']'})
                    current_msg = z
                    send = ''
                    sms_new = ''
                    id_new = ''
    except:
        continue
