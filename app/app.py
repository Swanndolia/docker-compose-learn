from werkzeug.utils import redirect
from model.articleModel import ArticleModel
from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)
article = ArticleModel()


@app.route('/')
def hello():
    result = article.fetch_all_article()
    return render_template('index.html', data=result)


@app.route('/add_article_template/')
def add_article_template():
    return render_template('add_article.html')


@app.route('/insert_article', methods=['POST', 'GET'])
def insert_article():
    data = request.form
    article.add_article(data)
    return redirect('/')

@app.route('/delete_article/<id>')
def delete_article(id):
    article.delete_article(int(id))
    return redirect('/')

@app.route('/update_article/<id>')
def update_article(id):
    article.delete_article(int(id))
    return redirect('/')
