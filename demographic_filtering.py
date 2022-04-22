import pandas as pd
import numpy as np

import plotly.express as px 

df = pd.read_csv('FLASK MOCKUP - 1/articles.csv')

df1=df[df['eventType'] == "CONTENT SHARED"]

df1=df1.reset_index(drop=True)

df1.shape

def find_total_events(df1_row):
  total_views=df1[(df1["contentId"] == df1_row["contentId"]) & (df1["eventType"] == "VIEW")].shape[0]
  total_likes=df1[(df1["contentId"] == df1_row["contentId"]) & (df1["eventType"] == "LIKE")].shape[0]
  total_bookmarks=df1[(df1["contentId"] == df1_row["contentId"]) & (df1["eventType"] == "BOOKMARK")].shape[0]
  total_follows=df1[(df1["contentId"] == df1_row["contentId"]) & (df1["eventType"] == "FOLLOW")].shape[0]
  total_comments=df1[(df1["contentId"] == df1_row["contentId"]) & (df1["eventType"] == "COMMENT CREATED")].shape[0]
  return total_views+total_likes+total_bookmarks+total_follows+total_comments

df1["total_events"]=df1.apply(find_total_events,axis=1)

df1=df1.sort_values('total_events',ascending=False)
df1.head(10)

fig = px.bar((df1.head(10).sort_values("total_events",ascending = True)),x = "total_events",y = "title",orientation ="h")
fig.show()

output = df1[["url","title","text","lang","total_events"]]