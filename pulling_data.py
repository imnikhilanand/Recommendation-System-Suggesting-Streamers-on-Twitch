# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 13:52:59 2022

@author: Nikhil
"""


"""
SCRAPPING DATA FROM TWITCH API

"""

# Imporing the libraries 
import configparser
import requests
import json
import pandas as pd
import time
import pprint
pp = pprint.PrettyPrinter(indent=4)
from requests.structures import CaseInsensitiveDict
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


# Extracting the API details from the config file
config = configparser.ConfigParser()
config.read('configuration.ini')
client_id = config["app_info"]["client_id"]
client_secret = config["app_info"]["client_secret"]
access_token = config["app_info"]["access_token"]

"""

SEND A POST REQUEST USING POSTMAN TO THIS ->

https://id.twitch.tv/oauth2/token?

client_id= 
&client_secret=
&grant_type=client_credentials

WILL RECEVIE THIS ->

{
  "access_token": ,
  "expires_in": 5404103,
  "token_type": "bearer"
}


PUT THE ACCESS TOKENS ALONG WITH CLIENT CREDENTIALS IN THE CONFIGURATION>INI FILE

"""

# get the game details from game ID
def get_game_detail_with_id(x):
    url = "https://api.twitch.tv/helix/games?id="+str(x)
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer "+access_token
    headers["Client-Id"] = client_id
    resp = requests.get(url, headers=headers)
    print(resp.json())

get_game_detail_with_id(32982)

# get game details with fame game name
def get_game_detail_with_name(x):
    url = "https://api.twitch.tv/helix/games?name="+str(x)
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer "+access_token
    headers["Client-Id"] = client_id
    resp = requests.get(url, headers=headers)
    print(resp.json())

get_game_detail_with_name('Grand Theft Auto V')

# get top games on twitch
def get_top_games():
    url = "https://api.twitch.tv/helix/games/top"
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer "+access_token
    headers["Client-Id"] = client_id
    resp = requests.get(url, headers=headers)
    return resp.json()['data']

get_top_games()

# get steamers details from gamer id 
def get_games_details(x):
    url = "https://api.twitch.tv/helix/users?login="+str(x)
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer "+access_token
    headers["Client-Id"] = client_id
    resp = requests.get(url, headers=headers)
    return resp.json()['data']

get_games_details('Ninja')

# get streamers details from streamers id
def get_games_details_with_name(x):
    url = "https://api.twitch.tv/helix/users?login="+str(x)
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer 6qesjsfcxxrl8ngairhbwkh7c6pb9b"
    headers["Client-Id"] = "5hw8leitbdrn45ull85cfolul3s9qo"
    resp = requests.get(url, headers=headers)
    return resp.json() #['data']

get_games_details_with_name('RanbooLive')

# get gamers followers
def get_user_follows(user_id):
    url = "https://api.twitch.tv/helix/users/follows?to_id="+str(user_id)+"&first=100"
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer "+access_token
    headers["Client-Id"] = client_id
    resp = requests.get(url, headers=headers)
    return resp.json() #['data']


# list of top 100 gamers extracted from an online source
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


# fetching top 100 streamers details using the abi
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

# get the list of 10000 latest followers of each of these people
temp = []
def get_user_follows_2(user_id):
    pagination = ''
    for i in range(0,100):
        if i == 0:
            url = "https://api.twitch.tv/helix/users/follows?to_id="+str(user_id)+"&first=100"
        else:
            url = "https://api.twitch.tv/helix/users/follows?to_id="+str(user_id)+"&first=100&after="+str(pagination['cursor'])
        print("i : ",i)
        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Bearer 6qesjsfcxxrl8ngairhbwkh7c6pb9b"
        headers["Client-Id"] = "5hw8leitbdrn45ull85cfolul3s9qo"
        resp = requests.get(url, headers=headers)
        resp = resp.json()
        for j in range(0, len(resp['data'])):
            temp.append([resp['data'][j]['from_id'], 
                        resp['data'][j]['from_login'], 
                        resp['data'][j]['to_id'], 
                        resp['data'][j]['to_name'], 
                        resp['data'][j]['followed_at']])
        pagination = resp['pagination']
        print(pagination)

# iterating over top 100 players to create the 
for index, vals in data_streamers[0:100].iterrows():
    get_user_follows_2(vals['id'])

# creating the dataframe from the followers and following mapping
followers_of_top_10_streamers = pd.DataFrame(temp, columns=['user_id','user_name','streamer_id','streamer_name','followed_at'])

# saving the dataframe for the folllowers and following mapping
followers_of_top_10_streamers.to_csv('Data/followers_of_top_10_streamers.csv', index=False)



"""

    Getting the list of games played by the top streamers the most

"""

# using selenium scrapping tool we will be extracitng hte recenlty played games from the user profile
driver = webdriver.Chrome()
players_and_games = {}
for index, val in data_streamers.iterrows():
    user_name = val['login']
    url = "https://www.twitch.tv/"+str(user_name)
    driver.get(url)
    time.sleep(5)
    temp = []
    try:
        content = driver.find_elements('xpath','//a[@data-test-selector="home-game-card-link"]/h2')
        for i in content:
            temp.append(i.text)
    except:
        pass
    players_and_games[user_name] = temp
driver.close()


# details for these players was not present so manually evaluated these
players_and_games['xqc'] = ['Overwatch 2']
players_and_games['thegrefg'] = ['God of War']
players_and_games['myth'] = ['Fall Guys','VALORANT','Among Us','Grand Theft Auto V']
players_and_games['timthetatman'] = ['Call of Duty: Modern Warfare II']
players_and_games["adinross"] = []
players_and_games["nickmercs"] = ['Apex Legends']
players_and_games["dream"] = ['Minecraft']
players_and_games["summit1g"] = ['Grand Theft Auto V']
players_and_games["elmariana"] = ['Call of Duty: Modern Warfare II','DEVOUR','Minecraft'] 
players_and_games["esl_csgo"] = ['Counter-Strike: Global Offensive']
players_and_games["elded"] = ['Left 4 Dead 2']
players_and_games["fortnite"] = ['fortnite']
players_and_games["moistcr1tikal"] = []
players_and_games["drlupo"] = ['Call of Duty: Modern Warfare II']
players_and_games["fresh"] = ['fortnite']
players_and_games["daequanwoco"] = ['fortnite','Call of Duty: Modern Warfare II']
players_and_games["sykkuno"] = ['among us']
players_and_games["faker"] = ["league of legends"]
players_and_games["rocketleague"] = ["rocket league"] 
players_and_games["nobru"] = ['fortnite'] 
players_and_games["gaules"] = ['Counter-Strike: Global Offensive',]
players_and_games["s1mple"] = ['Counter-Strike: Global Offensive'] 
players_and_games["asmongold"] = ['World of Warcraft']
players_and_games["gabelulz"] = []
players_and_games["trymacs"] = ['Minecraft']
players_and_games["ludwig"] = ['Mario Party']
players_and_games["x2twins"] = ['fortnite']
players_and_games["aydan"] = ['Call of Duty: Modern Warfare II','Fortnite']
players_and_games["jelty"] = ['VALORANT']
players_and_games["loserfruit"] = ['Fortnite']
players_and_games["kaicenat"] = []
players_and_games['fernanfloo']=['Just Chatting','fortnite']


# creating the a temp array to store the games played by top streamers
temp = []
for i in players_and_games:
    temp.append([i, players_and_games[i]])

# creating dataframe for the stremers and the most played games
streamers_games = pd.DataFrame(temp, columns=['streamer','games'])

# saving the data to dataframe
streamers_games.to_csv('Data/streamers_games.csv', index=False)













