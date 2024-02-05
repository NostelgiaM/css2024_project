# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:15:59 2024

@author: USER
"""

import pandas as pd
from collections import Counter

file = 'movie_dataset.csv'
df = pd.Dataframe(file)
print(df)


df['Revenue (Millions)'].fillna(df['Revenue (Millions'].median(),inplace=True
df['Metascore'].fillna(df['Metascore'].median(),inplace=True
                       
high_rated-movie =df.loc[df['Rating'].idxmax()]['Title']

avarage  revene = df['Revenue (Millions)'].mean()

avarage_rev_2015_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]['Revenue (Millions)'].mean()

Movies_released_2016 = df[df['Year'] == 2016], shape[0]

Movie_directed_Christoper =df[df['Director'] == 'Christopher Nolan'].shape[0]

Movie_with_atleast_8_rating  = df[df['Rating'] >= 8.0].shape[0]

median_rating_Christopher_movies = df[df['Director'] == 'Christopher Nolan']['Rating'].median()

High_avarage_year =df.groupby(Year)['Rating'].mean()idxmax()

