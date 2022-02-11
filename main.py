import requests
token = input("token of bot: ")
id = input("chat id : ")
text = input("text to send : ")
for x in range(10000):
    requests.post("https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + id + "&text=" + text)
    print("Message send :D " + text)
    