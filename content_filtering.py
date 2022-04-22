from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

df = pd.read_csv('FLASK MOCKUP - 1/articles.csv')


count=CountVectorizer(stop_words="english")
count_matrix=count.fit_transform(df["title"])

cosine_sim = cosine_similarity(count_matrix, count_matrix)

df=df.reset_index()
indices=pd.Series(df.index,index=df['contentId'])

def get_recommendations(contentId):
    idx = indices[contentId]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df[['title', 'text', 'lang', 'total_events']].iloc[movie_indices].values.tolist()