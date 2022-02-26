# Dynamic HTML Pages Templates and Buiding URL in Flask Using Jinja

from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)


@app.route('/guess/<name>/')
def guess(name):
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    agify_response = requests.get(url=f"https://api.agify.io?name={name}")
    agify_response.raise_for_status()
    age_data = agify_response.json()
    age = age_data["age"]
    return render_template('guess.html', first_name=name, gender=gender, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    blog_response = requests.get(url="https://api.npoint.io/ed99320662742443cc5b")
    blog_response.raise_for_status()
    all_posts = blog_response.json()
    return render_template('blog.html', posts=all_posts)


# Blog Capstone Project - Templating
@app.route('/capstone-blog')
def capstone_blog():
    blog_response = requests.get(url="https://api.npoint.io/ed99320662742443cc5b")
    blog_response.raise_for_status()
    all_posts = blog_response.json()
    return render_template('capstone_blog.html', posts=all_posts)


@app.route('/post/<num>')
def capstone_post(num):
    blog_response = requests.get(url="https://api.npoint.io/ed99320662742443cc5b")
    blog_response.raise_for_status()
    all_posts = blog_response.json()
    return render_template('capstone_post.html', posts=all_posts[int(num)-1])


if __name__ == '__main__':
    app.run(debug=True)
