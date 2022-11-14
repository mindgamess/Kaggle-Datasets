import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.title('Anime Recommendation system')
df = pickle.load(open('ANIME recsys/anime_recs.pkl', 'rb'))
similarity = pickle.load(open('ANIME recsys/similarity.pkl', 'rb'))
list_anime = np.array(df['Name'])
option = st.selectbox('Select Anime', (list_anime))


def anime_recommend(anime):
     index = df[df['Name'] == anime].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
     res = []
     for i in distances[1:6]:
          res.append("{}".format(df.iloc[i[0]]['Name']))
     return res


if st.button('Recommend Me'):
     st.write('Anime Recommended for you:')
     df = pd.DataFrame({'Anime Recommended': anime_recommend(option)})
     st.table(df)