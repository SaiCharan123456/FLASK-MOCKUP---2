from nntplib import ArticleInfo
from flask import Flask, jsonify, request
import csv
from demographic_filtering import output
from content_filtering import get_recommendations,df





liked_articles = []
not_liked_articles = []
did_not_watch = []

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    article_data = {
            "title": df[12],            
            "overview": df[13],            
            "language": df[14],
            "total_events": df[15],
            
        }
    return jsonify({
        "data": article_data,
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch():
    article = all_articles[0]
    all_articles = all_articles[1:]
    did_not_watch.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-articles")
def popular_articles():
    article_data = []
    for article in output:
        _d = {
            "title": article[1],
            "overview": article[2],
            "link": article[0],
            "language": article[3],
            "total_events": article[4],
            
            
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendations(liked_article[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
            "title": recommended[0],            
            "overview": recommended[1],            
            "language": recommended[2],
            "total_events": recommended[3],
            
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
  app.run()