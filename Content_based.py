from sklearn.metrics.pairwise import cosine_similarity

import Preprocesing
import streamlit as st
import pandas as pd

def cosine_similar(vectors):
    similarity = cosine_similarity(vectors[:10000])
    similarity.shape
    return similarity
def recommend(new_df,movie,similarity,df_news):
    a=[]
    movie_index = new_df[new_df['Title'] == movie].index[0]
    distances = similarity[movie_index]
    
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:10]

    news_rec = pd.DataFrame(columns=['News_Id','Title','URL'])

    for i in movies_list:
        b={}
        id = new_df[new_df['Title'] ==new_df.iloc[i[0]].Title].index[0]
        news_id=new_df['News_ID'][id]
        url_index=df_news[df_news['Title']==df_news.iloc[i[0]].Title].index[0]
        
        b['News_Id']=news_id
        b['Title']=new_df.iloc[i[0]].Title
        b['URL']=df_news['URL'][url_index]
        # b.append(new_df.iloc[i[0]].Title)
        news_rec = news_rec.append(b, ignore_index = True)
    return news_rec
# print(recommend(new_df['Title'][int(x)]))
# pickle.dump(y, open('capstone.pkl', 'wb'))
def call_preprop(df_news):
   print("b_p")
   new_df,vectors=Preprocesing.preprop(df_news)
   print("A_p")
   similarity=cosine_similar(vectors)
   print('A_c')
   y= st.text_input('News-ID', 'N55528')
#    st.write('The current movie title is', title)
#    y=input("ENter the News ID:")
   x=new_df[new_df['News_ID'] == y].index[0]
   z=new_df['Title'][int(x)]
   return recommend(new_df,z,similarity,df_news)
