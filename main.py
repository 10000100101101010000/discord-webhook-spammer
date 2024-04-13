# Made by 10000100101101010000 on Github | Licensed (MIT)
# This was made for educational purposes only
# Find the latest version at https://github.com/10000100101101010000/discord-webhook-spammer


import requests
import json
import time

def load_config():
    with open("config.json", "r") as config_file:
        config_data = json.load(config_file)
    return config_data.get("webhook_url")


def send_webhook_message(webhook_url, message, pfp, name):
    data = {
        "content": message,
        "username": name,
        "avatar_url": pfp
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    
    if response.status_code == 204:
        print(f"success: {response.status_code}")
    else:
        print(f"err: {response.status_code}")

def main():
    webhook_url = load_config()
    if not webhook_url:
        print("url isnt valid/isnt in json file")
        return
    # pfp is good dont change it pls
    pfp = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjyrhJBQxS4K58zdqWROk4F4F8cTZIFWWIUw&s'
    name = '#RATELIMITS' # name of webhook you want
    message = "# ||@everyone|| \n# killed ratelimits ; discord.gg/coded" # message of webhook you want


    for i in range(30): # anything over 30 will kill the bot
        send_webhook_message(webhook_url, f"{message}", pfp, name)
        time.sleep(0.01)

if __name__ == "__main__":
    main()

# enjoy and good luck, i dont take responsibility for what you use this tool with
