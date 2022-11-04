# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:49:31 2022

@author: Nikhil
"""


# Importing the libraries
import pandas as pd


# importing the dataset
followers_of_top_10_streamers = pd.read_csv("Data/followers_of_top_10_streamers.csv")

"""
 creating the pivot table for modeling
"""

# adding an addtional colum for counting
followers_of_top_10_streamers['follows'] = 1

# making the pivot
followers_of_top_10_streamers_pivot = followers_of_top_10_streamers.pivot(index="user_id", columns=["streamer_id"])["follows"]



