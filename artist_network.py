from api_key import *
import numpy as np
import pandas as pd
import json
import os
import time
import networkx as nx
import matplotlib.pyplot as plt #plotting

from pyechonest import config
#config.ECHO_NEST_API_KEY = api_key_1
config.ECHO_NEST_API_KEY = api_key_2
#config.ECHO_NEST_API_KEY = api_key_3
from pyechonest import artist
total_singer = pd.read_csv('similar_artists_top_50.csv', encoding="utf-8")
ln = len(total_singer)
total_artist_edge = pd.DataFrame(np.zeros(ln**2).reshape(ln,ln))
star = '*'*10
for i in range(ln):
    sim_list = [singer.name for singer in artist.Artist(total_singer.iloc[i]['artist']).similar[:30]]
    for j in range(ln):
        if (i!=j)and(total_singer.iloc[j]['artist'] in sim_list):
            total_artist_edge.iloc[i][j] = 1
    if ((i+1)%40==0):
        time.sleep(60)
    print('{0} {1}|{2} {3}'.encode("utf-8").format(star, i+1, artist.Artist(total_singer.iloc[i]['artist']), star))
total_artist_edge.to_csv("total_artist_edge.csv",encoding="utf-8",index=True)
