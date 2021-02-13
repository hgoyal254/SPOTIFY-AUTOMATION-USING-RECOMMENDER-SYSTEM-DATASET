import pandas
import numpy as np
import time

#Load datasets
#Read userid-songid-listen_count triplets
#This step might take time to download data from external sources
triplets_file = 'https://static.turi.com/datasets/millionsong/10000.txt'
songs_metadata_file = 'song_data.csv'

song_df_1 = pandas.read_table(triplets_file,header=None)
song_df_1.columns = ['user_id', 'song_id', 'listen_count']

#Read song  metadata
song_df_2 =  pandas.read_csv(songs_metadata_file)

#Merge the two dataframes above to create input dataframe for recommender systems
song_df = pandas.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")


#Explore datasets
song_df['song'] = song_df['title'].map(str) + " & " + song_df['artist_name']
song_grouped = song_df.groupby(['song']).agg({'listen_count': 'count'}).reset_index()
song_grouped = song_grouped.groupby('song').sum()['listen_count'].sort_values(ascending=False)
songs = song_grouped.keys()
songs = list(songs)
song_dic = []
for i in range(50):
    x = songs[i].split(' & ')
    dic = {
        "song_name" : x[0],
        "artist" : x[1]
    }
    song_dic.append(dic)

def createDic():
    return song_dic