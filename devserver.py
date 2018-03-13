import os
import requests
from flask import Flask
from flask import render_template
from jinja2 import Template
import os
from . utils import PostsParser
from graphqlclient import GraphQLClient
import json

app = Flask(__name__)


# template_dir = os.path.abspath('templates/')
# app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def main():
    posts_objects = PostsParser()
    posts = posts_objects.posts
    return render_template('index.html', posts=posts)


@app.route("/posts")
def blog():
    posts_objects = PostsParser()
    posts = posts_objects.posts
    return render_template('posts.html', posts=posts)


@app.route('/<slug>')
def single_blog(slug):
    # Shows individual post
    # TODO: normal 404 if not found
    # TODO: create template for single-post
    # TODO: remove '\n from parsing?'
    posts_objects = PostsParser()
    posts = posts_objects.posts

    for post in posts:
        if post['slug'] == slug:
            # return post['content']
            return render_template('single-post.html', post=post)

    return page_not_found(404)


@app.route("/play")
def play():
    access_token = "7e0118b3603a7c3a54435db7"
    bearer_token = 'Bearer ' + access_token

    client = GraphQLClient("https://wip.chat/graphql")
    client.inject_token(bearer_token)

    result = client.execute('''

    query{
      user(id: "73") {
        username
        products {
          name
          id
        }
      }
    }
    ''')

    products = json.loads(result)

    url = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=ronald911&limit=10&api_key=b45188c880a0f2f08c244f72d92d011d&format=json"

    r = requests.get(url)

    raw = r.json()

    data = json.dumps(raw["recenttracks"])

    songs = json.loads(data)

    return render_template('play.html', data=products, music=songs)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0')

# export FLASK_APP=devserver.py
# export FLASK_DEBUG=1
# export LC_ALL="en_US.UTF-8"
# export LC_CTYPE="en_US.UTF-8"
