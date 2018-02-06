import markdown2
from flask import Markup, url_for
import os


class PostsParser():
    '''
    Initiates parsing of all the posts.
    '''

    def __init__(self):
        self.posts = []
        print(url_for('static', filename='featured-images'))
        for post in os.listdir("posts/"):
            # Loops over all posts and stores html in posts[]
            if post.endswith('.md'):
                path = "posts/" + post
                html = markdown2.markdown_path(path)
                title, author, date, image = self.getVars(html)

                self.posts.append({
                    'title': title,
                    'author': author,
                    'date': date,
                    'slug': post.replace('.md', ''),
                    'content': html,
                    'image': url_for('static', filename='featured-images/' + image)
                })

    def getVars(self, html):
        '''
        Parses the html to get the variables.
        @input markdown to html string
        @returns title, author and date
        '''
        begin = html.find("<!-- VARS")
        end = html.find("./VARS -->")
        params = html[begin + 10:end]

        title = params[(params.find("##title: ") + 9):params.find(" ./title")]
        author = params[(params.find("##author: ") + 10):params.find(" ./author")]
        date = params[(params.find("##date: ") + 8):params.find(" ./date")]
        image = params[(params.find("##image: ") + 8):params.find(" ./image")].replace(' ', '')

        return title, author, date, image