# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:49:31 2022

@author: Nikhil
"""


# Importing the libraries
import pandas as pd
import string
from selenium import webdriver
import time
import random

# importing the dataset
followers_of_top_10_streamers = pd.read_csv("Data/followers_of_top_10_streamers.csv")

"""
 creating the pivot table for modeling

"""

# adding an addtional colum for counting
followers_of_top_10_streamers['follows'] = 1

# making the pivot
followers_of_top_10_streamers_pivot = followers_of_top_10_streamers.pivot(index="user_id", columns=["streamer_id"])["follows"]

# creating a column to store the number of streamers a person follows
followers_of_top_10_streamers_pivot["following_count"] = 99-followers_of_top_10_streamers_pivot.isnull().sum(axis=1)

# extractinv only those usrers who have followed more than 3 streamers
follower_of_top_10_stremers_pivot_more_than_4_streamers = followers_of_top_10_streamers_pivot.query("following_count>3")

# saving this file to create the model 
follower_of_top_10_stremers_pivot_more_than_4_streamers.to_csv("data/follower_of_top_10_stremers_pivot_more_than_4_streamers.csv", index=False)

# extracting the unique games from the dataset
streamers_games = pd.read_csv("data/streamers_games.csv")

streamers_games["games_list"] = ''

# function to return the games played a particular streamer in list
def get_games_as_list(x):
    a = str(x).split(",")
    temp = []
    for i in a:
        temp.append(i.translate(str.maketrans('','', string.punctuation)).strip().lower())
    return temp

for index, val in streamers_games.iterrows():
    streamers_games.at[index,'games_list'] = get_games_as_list(val["games"])
    
# adding games names as a list correponding to each streamer
streamers_games["games_list"][20] = ['just chatting', "i'm only sleeping", 'pools, hot tubs, and beaches']

# getting all the unique games
set_of_unique_games = set()

for index, val in streamers_games.iterrows():
    for i in val["games_list"]:
        set_of_unique_games.add(i)

games_and_genre = {}

# get the details of games from scrapping data
driver = webdriver.Chrome()
m = 0
for i in set_of_unique_games:
    m = m + 1
    if len(i)>0 and m>49:
        url = "https://www.google.com/search?q=wikipedia.com + "+str(i)+" + game"
        driver.get(url)
        driver.find_elements('xpath',"//h3[@class='LC20lb MBeuO DKV0Md']")[0].click()
        t = random.randint(4, 9)
        time.sleep(t)
        temp_genre = []
        temp_type = []
        try:
            # genre
            content_genre = driver.find_elements('xpath',"//th[*='Genre(s)']/following::td[1]")
            # type
            content_type = driver.find_elements('xpath',"//th[text()='Mode(s)']/following::td[1]")
            for k in content_genre:
                temp_genre.append(k.text)
            for l in content_type:
                temp_type.append(l.text)
        except:
            pass
        games_and_genre[i] = [temp_genre, temp_type]


# checking which of the games have got their genre
for i in set_of_unique_games:
    if i not in games_and_genre:
        print(i)

# manually assigning the genre
games_and_genre["the mortuary assistant"] = [['Adventure'],['Single-player']]
games_and_genre["cuphead"] = [['Run and Gun'],['Single-player','multiplayer']]
games_and_genre["the closing shift"] = [['Action', 'Adventure', 'Casual', 'Indie', 'Simulation', 'Strategy','Walking Simulation'],['Single-player']]
games_and_genre['escape the ayuwoki'] = [['Adventure','Walking Simulation'],['Single-player','multiplayer']]
games_and_genre['way of the hunter'] = [['Simulation'],['Single-player']]
games_and_genre['phasmophobia'] = [['Indie', 'Adventure', 'Survival horror', 'Action', 'Puzzle'],['Single-player''multiplayer']]
games_and_genre['fall guys'] = [['Battle royale', 'Indie','Simulation','platform'],['multiplayer']]
games_and_genre['just dance 2015'] = [['rythm'],['Single-Player','multiplayer']]
games_and_genre['brotato'] = [['Shooter', 'Indie', 'Role-playing', 'Casual', 'Fighting']]
games_and_genre['dota 2'] = [['MOBA'],['multiplayer']]
games_and_genre['just chatting'] = []
games_and_genre['mortal kombat 11'] = [['Fighting','Action','Adventure'],['Single-Player','multiplayer']]
games_and_genre['among us'] = [['Party','social deduction'],['Multiplayer']]
games_and_genre['nba 2k23'] = [['Sports'],['Single-player','multiplayer']]
games_and_genre['rampage knights'] = [['Action', 'Roguelike', 'Indie', 'Fighting', 'Arcade', 'Adventure'], ['multiplayer']] 
games_and_genre['call of duty modern warfare ii'] = [['First-person shooter'],['Single-player, multiplayer']]
games_and_genre['chivalry 2'] = [['Hack and Slash'],['Multiplayer']]
games_and_genre['ranch simulator'] = [['Simulation', 'Adventure', 'Shooting', 'Strategy'],['Single-player, multiplayer']]
games_and_genre['dealers life 2'] = [['Trading'],['Single-player']]
games_and_genre['devour'] = [['Indie', 'Action', 'Adventure'],['Single-player, multiplayer']]
games_and_genre['sports'] = [['Sports'],[]]
games_and_genre['labyrinthian'] = [['Puzzle', 'Indie', 'Adventure', 'Action', 'Adventure'],['Single-player, multiplayer']]
games_and_genre['car dealership simulator'] = [['Simulation'],['Single-player']]
games_and_genre['stress test'] = [['Action', 'Adventure', 'RPG', 'Strategy'],['Multiplayer']]
games_and_genre['dave the driver'] = [['Adventure', 'RPG'], ['Single-player']]
games_and_genre['music'] = [['rythm'],[]]
games_and_genre['the chant']= [['Third-person','Action','Adventure'],['Single-player']]
games_and_genre['the bathhouse'] = [['Adventure', 'Indie'],['Single-player']]
games_and_genre['slots'] = []
games_and_genre['food drink'] = []
games_and_genre['dome keeper'] = []
games_and_genre['king of the castle'] = []
games_and_genre["i'm only sleeping"] = []
games_and_genre['pools, hot tubs, and beaches'] = []


# creating dataframe for genre
games_and_genre_list = []
for i in games_and_genre:
    games_and_genre_list.append([i,games_and_genre[i]])
    
games_and_genre_dataframe = pd.DataFrame(games_and_genre, columns=["game","genre & player type"])

# saving games and genre dataframe
games_and_genre_dataframe.to_csv("data/games_and_genre.csv", index=False)









































