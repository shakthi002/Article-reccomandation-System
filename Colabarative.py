
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import pandas as pd

def cosine_similar(df_new):
    X_user=df_new.drop(['User_id'], axis=1,inplace=False)
    vectors_user=X_user.to_numpy()
    similarity_user = cosine_similarity(vectors_user)
    return similarity_user

def similar_user(df_new,df,similarity_user,user_id):
    similar_users=[]
    # movie=st.text_input('Your User_ID', 'U24775')
    # movie=input("ENter the user_id")
    movie_index = df_new[df_new['User_id'] == user_id].index[0]
    distances = similarity_user[movie_index]
        
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6] 
    # print(movies_list) 
    
    print("\nSimilar Users:")
    for i in movies_list:
        x=i[0]
        # print(x)
        # print(df['Userid'][x])
        similar_users.append(df['Userid'][x])
    # print(similar_users)
    return similar_users,user_id
def reccomand_article(similar_users,his):
    rec=[]
    for i in similar_users:
       rec.append(his[i][:5])
    # print(rec)
    return rec
def reccomand_name(rec,df_news,user,his):
    news_rec2 = pd.DataFrame(columns=['News_ID','Title'])
    for i in rec:
        print(i)
        for j in i:
            #  print(j)
            if j not in his[user]:
                b={}
                ind=df_news[df_news['News_ID'] == j].index[0]
                b['News_ID']=df_news['News_ID'][ind]
                b['Title']=df_news['Title'][ind]
                news_rec2 = news_rec2.append(b, ignore_index = True)
    return news_rec2
def Colabarative(df_new,df_news,df,his,user_id):

    similarity_user=cosine_similar(df_new)
    similar_users,user=similar_user(df_new,df,similarity_user,user_id)

    rec=reccomand_article(similar_users,his)
    return reccomand_name(rec,df_news,user,his)