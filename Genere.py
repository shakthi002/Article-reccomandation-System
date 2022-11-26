
import pandas as pd
import streamlit as st

def dictionary(df):
    his = {}
    user_id=st.text_input('Your User_ID', 'U24775')
    df['History'] = df['History'].astype(str)
    for i in range(df.shape[0]):
        arr = [x for x in df['History'][i].split(' ')]
        his[df['Userid'][i]] = arr
    # print(his['U91836'])
    # i=df[df['Userid']==movie].index[0]
    # his[movie]=[x for x in df['History'][i]]
    return his,user_id

def genere(his,df_news,user_id):
    final={}

    for i in his:
        genre={}
        m=0
        for j in range(len(his[i])):
            if  df_news['Category'][j] not in genre:
               genre[df_news['Category'][j]]=1
            else:
              genre[df_news['Category'][j]]+=1
        for k in genre:
            x=genre[k]
            if m<x:
             cat=k
        final[i]=cat
        # return i,cat
    return final[user_id]
    # df_genre = pd.DataFrame({"User":list(final.keys()),"genre":list(final.values())})