import pandas as pd
# import Preprocesing
import Genere
import Content_based
import Colabarative
# genre={}
import streamlit as st
from streamlit_option_menu import option_menu

def Genere(df,df_news):
    import Genere
    his,user_id=Genere.dictionary(df)
    Gen=Genere.genere(his,df_news,user_id)
    # print(len(final))
    return user_id,Gen,his

# # df_news['Title_Entries'] = df_news['Title_Entries'].apply(lambda x:[i.replace(" ","") for i in x])
def Contentbased(df_news):
    import Content_based
    st.write(Content_based.call_preprop(df_news))
     
def Colabarative(df_new,df_news,df,his,user_id):
    import Colabarative
    # st.Write(Gen)
    st.write(Colabarative.Colabarative(df_new,df_news,df,his,user_id))
    

df=pd.read_csv('D:\\Capstone\\behaviors.csv')
# print(df)
df.rename(columns = {'1':'Index'}, inplace = True)
df.rename(columns = {'U13740':'Userid'}, inplace = True)
df.rename(columns = {'11/11/2019 9:05:58 AM':'Time'}, inplace = True)
df.rename(columns = {'N55189 N42782 N34694 N45794 N18445 N63302 N10414 N19347 N31801':'History'}, inplace = True)
df.rename(columns = {'N55689-1 N35729-0':'Impressions'}, inplace = True)

df_news=pd.read_csv("D:\\Capstone\\news.tsv", delimiter='\t',header=None)

col_names = ['News_ID', 'Category', 'SubCategory', 'Title', 'Abstract', 'URL', 'Title_Entries', 'Abstract_Entities']
df_news.columns = col_names


df_new=pd.read_csv('D:\\Capstone\\df_new.csv')
print("Hi")
# df_news.set_index('News_ID', inplace = True)
# his=Genere.dictionary(df)
# # Colabarative(df_new,df_news,df)
# Colabarative.Colabarative(df_new,df_news,df,his)
# # print(his)

# Genere(df,df_news)
# Contentbased(df_news)
# Colabarative(df_new,df_news,df)

with st.sidebar:
    selected = option_menu(menu_title='Main Menu',options=['About','Content_Based','Collaborative'])

if selected=='About':
    st.title('Article recommendation')

elif selected=='Content_Based':
    Contentbased(df_news)

elif selected=='Collaborative':
    user_id,Gen,his=Genere(df,df_news)
    st.write('Your Genere is')
    st.write(Gen)
    Colabarative(df_new,df_news,df,his,user_id)
    

