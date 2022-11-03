# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 13:52:59 2022

@author: Nikhil
"""





# updated client id and secret
client_id=5hw8leitbdrn45ull85cfolul3s9qo&client_secret=7t75m570gfns8n17ea7p99doh3ayjv&grant_type=client_credentials

https://id.twitch.tv/oauth2/authorize
    ?response_type=code
    &client_id=5hw8leitbdrn45ull85cfolul3s9qo
    &redirect_uri=http://localhost:80
    &scope=channel%3Amanage%3Apolls+channel%3Aread%3Apolls
    &state=c3ab8aa609ea11e793ae92361f002671

# response ---- ! IMPORTANT ! -----
http://localhost/?
code=orvf6o7ju4lzkvxvpxck011kzemfhl
&scope=channel%3Amanage%3Apolls+channel%3Aread%3Apolls
&state=c3ab8aa609ea11e793ae92361f002671
#############################################################

# send this ->

# https://id.twitch.tv/oauth2/token?client_id=5hw8leitbdrn45ull85cfolul3s9qo&client_secret=7t75m570gfns8n17ea7p99doh3ayjv&grant_type=client_credentials

# to get the below keys

{
  "access_token": "6qesjsfcxxrl8ngairhbwkh7c6pb9b",
  "expires_in": 5404103,
  "token_type": "bearer"
}




import requests


#URL = https://id.twitch.tv/oauth2/authorize?response_type=code&client_id=5hw8leitbdrn45ull85cfolul3s9qo&redirect_uri=http://localhost:8080/&scope=channel%3Amanage%3Apolls+channel%3Aread%3Apolls


from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/get_tokens")
def get_tokens():
    dictToSend = {'client_id':'5hw8leitbdrn45ull85cfolul3s9qo',
                  'client_secret':'nw0uzgmyi1rhs7ydd718dytbeu5uqg',
                  'code':'orvf6o7ju4lzkvxvpxck011kzemfhl',
                  'grant_type':'authorization_code',
                  'redirect_uri':'http://localhost:80'
                 }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    res = requests.post('https://id.twitch.tv/oauth2/token',json = dictToSend, headers=headers)
    print('response from server:',res.text)
    return res.json()
    
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)




{
    "access_token": "005pkxtqeawxa92durmbyybubiouxq",
    "expires_in": 15242,
    "refresh_token": "ay0nsmn1pqdu7nmlzbj4639aw5yzi9owzcuyoh7g0m1klly8we",
    "scope": [
        "channel:manage:polls",
        "channel:read:polls"
    ],
    "token_type": "bearer"
}




import pandas as pd

data = pd.read_csv('100k_a.csv', names=['user_id','stream_id','stream_name','start_time','stop_time'])




len(data['stream_id'].unique())






########################################################################################################


import requests
import json
import pandas as pd
import time
import pprint
pp = pprint.PrettyPrinter(indent=4)
#import psycopg2 as pg
from sqlalchemy import create_engine
from requests.structures import CaseInsensitiveDict

# Twitch Client ID 
clientID = '5hw8leitbdrn45ull85cfolul3s9qo'
clientSecret = '3i3yjol0kv9dhsmotzujgs8dvw1bb8'

# after sending request I got this  using Postman 
# [POST] https://id.twitch.tv/oauth2/token?client_id=5hw8leitbdrn45ull85cfolul3s9qo&client_secret=3i3yjol0kv9dhsmotzujgs8dvw1bb8&grant_type=client_credentials

{
    "access_token": "1x4er7nt1a7i9ad0k6gd1edsa9dl3q",
    "expires_in": 4953583,
    "token_type": "bearer"
}


# get the game details from ID
def get_game_detail_with_id(x):
    url = "https://api.twitch.tv/helix/games?id="+str(x)
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer 1x4er7nt1a7i9ad0k6gd1edsa9dl3q"
    headers["Client-Id"] = "5hw8leitbdrn45ull85cfolul3s9qo"
    resp = requests.get(url, headers=headers)
    print(resp.json())

get_game_detail_with_id(32982)

# get game details with name
def get_game_detail_with_name(x):
    url = "https://api.twitch.tv/helix/games?name="+str(x)
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer 1x4er7nt1a7i9ad0k6gd1edsa9dl3q"
    headers["Client-Id"] = "5hw8leitbdrn45ull85cfolul3s9qo"
    resp = requests.get(url, headers=headers)
    print(resp.json())

get_game_detail_with_name('Grand Theft Auto V')

# get top games 
def get_top_games():
    url = "https://api.twitch.tv/helix/games/top"
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer 1x4er7nt1a7i9ad0k6gd1edsa9dl3q"
    headers["Client-Id"] = "5hw8leitbdrn45ull85cfolul3s9qo"
    headers["after"] = "2"
    headers["before"] = "3"
    headers["first"] = "100"
    resp = requests.get(url, headers=headers)
    return resp.json()['data']

len(get_top_games())

# get gamers details
def get_games_details(x):
    url = "https://api.twitch.tv/helix/users?login="+str(x)
    headers["Authorization"] = "Bearer 1x4er7nt1a7i9ad0k6gd1edsa9dl3q"
    headers["Client-Id"] = "5hw8leitbdrn45ull85cfolul3s9qo"
    resp = requests.get(url, headers=headers)
    return resp.json()['data']

get_games_details('Ninja')


# get gamers details with name
def get_games_details_with_name(x):
    url = "https://api.twitch.tv/helix/users?login="+str(x)
    headers["Authorization"] = "Bearer 6qesjsfcxxrl8ngairhbwkh7c6pb9b"
    headers["Client-Id"] = "5hw8leitbdrn45ull85cfolul3s9qo"
    resp = requests.get(url, headers=headers)
    return resp.json() #['data']

get_games_details_with_name('RanbooLive')


# get gamers followers
def get_user_follows(user_id):
    url = "https://api.twitch.tv/helix/users/follows?to_id="+str(user_id)+"&first=100"
    headers["Authorization"] = "Bearer 1x4er7nt1a7i9ad0k6gd1edsa9dl3q"
    headers["Client-Id"] = "5hw8leitbdrn45ull85cfolul3s9qo"
    resp = requests.get(url, headers=headers)
    return resp.json()['data']

len(get_user_follows(19571641))


# list of top 100 gamers
top_100_gamer_username = ['Ninja',
                         'auronplay',
                         'Rubius',
                         'ibai',
                         'xQc',
                         'Tfue',
                         'shroud',
                         'TheGrefg',
                         'juansguarnizo',
                         'pokimane',
                         'sodapoppin',
                         'Heelmike',
                         'Myth',
                         'tommyinnit',
                         'TimTheTatman',
                         'AdinRoss',
                         'NICKMERCS',
                         'Riot Games',
                         'SypherPK',
                         'Dream',
                         'summit1g',
                         'Amouranth',
                         'alanzoka',
                         'ElMariana',
                         'ElSpreen',
                         'ESL_CSGO',
                         'Clix',
                         'elded',
                         'Fortnite',
                         'Mongraal',
                         'AriGameplays',
                         'Quackity',
                         'Bugha',
                         'loltyler1',
                         'Tubbo',
                         'GeorgeNotFound',
                         'MontanaBlack88',
                         'Dakotaz',
                         'WilburSoot',
                         'moistcr1tikal',
                         'Robleis',
                         'DrLupo',
                         'Fresh',
                         'RanbooLive',
                         'NickEh30',
                         'DaequanWoco',
                         'Philza',
                         'SLAKUN10',
                         'Sykkuno',
                         'Squeezie',
                         'benjyfishy',
                         'Faker',
                         'RocketLeague',
                         'Gotaga',
                         'NOBRU',
                         'Gaules',
                         'Symfuhny',
                         'coscu',
                         'Castro_1021',
                         'Elraenn',
                         'loud_coringa',
                         'karljacobs',
                         'VALORANT',
                         'Fernanfloo',
                         's1mple',
                         'Asmongold',
                         'buster',
                         'Alexby11',
                         'gabelulz',
                         'Trymacs',
                         'MissaSinfonia',
                         'IamCristinini',
                         'TenZ',
                         'ludwig',
                         'Syndicate',
                         'x2Twins',
                         'QuackityToo',
                         'Sapnap',
                         'casimito',
                         'elxokas',
                         'biyin_',
                         'LOLITOFDEZ',
                         'LIRIK',
                         'Aydan',
                         'Jelty',
                         'Loserfruit',
                         'cloakzy',
                         'jacksepticeye',
                         'aceu',
                         'wtcN',
                         'Carreraaa',
                         'MrSavage',
                         'Staryuuki',
                         'DisguisedToast',
                         'Nightblue3',
                         'KaiCenat',
                         'Nihachu',
                         'EASPORTSFIFA',
                         'Anomaly',
                         'StableRonaldo']


# fetching the streamers details
import time
user_ids_and_names = []
for i in top_100_gamer_username:
    temp = []
    temp2 = get_games_details_with_name(i)
    try:
        temp.append(temp2['data'][0]['id'])
    except:
        temp.append('')
        pass
    try:
        temp.append(temp2['data'][0]['login'])
    except:
        temp.append('')
        pass
    try:
        temp.append(temp2['data'][0]['display_name'])
    except:
        temp.append('')
        pass
    try:
        temp.append(temp2['data'][0]['type'])
    except:
        temp.append('')
        pass
    try:
        temp.append(temp2['data'][0]['broadcaster_type'])
    except:
        temp.append('')
        pass
    try:
        temp.append(temp2['data'][0]['description'])
    except:
        temp.append('')
        pass
    try:
        temp.append(temp2['data'][0]['view_count'])
    except:
        temp.append('')
        pass
    user_ids_and_names.append(temp)
    time.sleep(3)


# create pandas dataframe of streamers details
streamers_details = pd.DataFrame(user_ids_and_names, columns = ['id','login','display_name','type','broadcaster_type','description','view_count'])

# saving the streamers data
streamers_details.to_csv("Data/streamer_details.csv", index=False)

# importing the streamers data
data_streamers = pd.read_csv('Data/streamer_details.csv')







