## taking director from crew
import ast
# import main 
import numpy as np
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

def Abstract_Entities(obj):
    L=[]
    for i in ast.literal_eval(obj):
            L.append(i['Label'])
            break
    return L

def Title_Entries(obj):
    L=[]
    for i in ast.literal_eval(obj):
            L.append(i['Label'])
    return L

def space(df_news):
    df_news['Title_Entries'] = df_news['Title_Entries'].apply(lambda x:[i.replace(" ","") for i in x])
    df_news['Abstract_Entities'] =df_news['Abstract_Entities'].apply(lambda x:[i.replace(" ","") for i in x])
    df_news['Category']= df_news['Category'].apply(lambda x: x.split())
    df_news['SubCategory']= df_news['SubCategory'].apply(lambda x: x.split())
    df_news['Abstract'] = df_news['Abstract'].apply(lambda x: x.split())


def tags(df_news):
    df_news['tags']=df_news['Abstract']+df_news['Title_Entries']+df_news['Abstract_Entities']+df_news['Category']+df_news['SubCategory']
    new_df = df_news[['News_ID','Title','tags']]
    new_df['tags'] = new_df['tags']
    return new_df


def vectorizer(new_df):
    cv = CountVectorizer(max_features=1000)
    vectors = cv.fit_transform(new_df['tags'].values.astype('U')).toarray()
    return vectors


def preprop(df_news):
    # df_news['Abstract_Entities'] = df_news['Abstract_Entities'].apply(Abstract_Entities)
    # df_news['Title_Entities'] = df_news['Title_Entities'].apply(Abstract_Entities)
    # space(df_news)
    new_df=tags(df_news)
    # print(new_df)
    vectors=vectorizer(new_df)
    # print(vectors)
    return new_df,vectors

