# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:49:31 2022

@author: Nikhil
"""


# Importing the libraries
import pandas as pd
import string

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
    
# getting all the unique games
set_of_unique_games = set()

for index, val in streamers_games.iterrows():
    for i in val["games_list"]:
        set_of_unique_games.add(i)

# adding games names as a list correponding to each streamer
streamers_games["games_list"][20] = ['just chatting', "i'm only sleeping", 'pools, hot tubs, and beaches']


































































