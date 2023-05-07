import requests
import re
import random
from time import sleep
import json

with open('text1.txt', 'r') as arquivo1, open('text2.txt', 'r') as arquivo2:
    texto1 = arquivo1.read()
    texto2 = arquivo2.read()
delay = int(input('Delay (seconds): \n'))

webhook_url = '' #webhook here
mensagem = '' # webhook message if problem
def send_webhook_message(url, mensagem):
    data = {
        'content': mensagem
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 204:
        print("Webhook message sent!")
    else:
        print(f"Error sending webhook message. Status code: {response.status_code}")
def send_tweet(number):
    x = open('accounts.txt', 'r+')
    accounts = x.readlines()
    accountarget = str(accounts[number])
    newtext = accountarget.split(":")
    finalresult = str(newtext[3])
    y = True
    match = re.search(r'ct0=([^;]+)', accountarget)
    if match:
        ct0 = str(match.group(1))
    while y:
        random_number = str(random.randint(0, 99999))
        mensagem = str(random.choice([texto1, texto2])) + " " + random_number
        url = "https://twitter.com/i/api/graphql/1RyAhNwby-gzGCRVsMxKbQ/CreateTweet"
        payload = {
            "variables": {
                "tweet_text": mensagem,
                "dark_request": False,
                "media": {
                    "media_entities": [],
                    "possibly_sensitive": False
                },
                "semantic_annotation_ids": []
            },
            "features": {
                "tweetypie_unmention_optimization_enabled": True,
                "vibe_api_enabled": True,
                "responsive_web_edit_tweet_api_enabled": True,
                "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
                "view_counts_everywhere_api_enabled": True,
                "longform_notetweets_consumption_enabled": True,
                "tweet_awards_web_tipping_enabled": False,
                "interactive_text_enabled": True,
                "responsive_web_text_conversations_enabled": False,
                "longform_notetweets_rich_text_read_enabled": True,
                "blue_business_profile_image_shape_enabled": True,
                "responsive_web_graphql_exclude_directive_enabled": True,
                "verified_phone_label_enabled": False,
                "freedom_of_speech_not_reach_fetch_enabled": True,
                "standardized_nudges_misinfo": True,
                "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": False,
                "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
                "responsive_web_graphql_timeline_navigation_enabled": True,
                "responsive_web_enhance_cards_enabled": False
            },
            "queryId": "1RyAhNwby-gzGCRVsMxKbQ"
        }
        headers = {
            "authority": "twitter.com",
            "accept": "*/*",
            "accept-language": "pt-BR,pt;q=0.9",
            "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
            "content-type": "application/json",
            "cookie": finalresult,
            "origin": "https://twitter.com",
            "referer": "https://twitter.com/home",
            "sec-ch-ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
            "x-csrf-token": ct0,
            "x-twitter-active-user": "yes",
            "x-twitter-auth-type": "OAuth2Session",
            "x-twitter-client-language": "pt"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        if response.status_code == 200:
            print('Tweet sent')
            sleep(delay)
            continue
        else:
            print('Problem while sending tweet')
            break



y = open('accounts.txt', 'r+')
rndmlist = y.readlines()
max = len(rndmlist)
print(max)


x = 0
while True:
    try:
        send_tweet(x)
    except:
        x += x
        if x >= max:
            break
        pass
    else:
        send_webhook_message(webhook_url, mensagem)
        break