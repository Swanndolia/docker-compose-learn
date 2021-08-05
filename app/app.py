from werkzeug.utils import redirect
from model.userModel import userModel
from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)
user = userModel()


@app.route('/')
def hello():
    result = user.fetch_all_user()
    return render_template('index.html', data=result)


@app.route('/add_user_template/')
def add_user_template():
    return render_template('add_user.html')


@app.route('/insert_user', methods=['POST', 'GET'])
def insert_user():
    data = request.form
    user.add_user(data)
    return redirect('/')

@app.route('/delete_user/<id>')
def delete_user(id):
    user.delete_user(int(id))
    return redirect('/')

@app.route('/update_user/<id>')
def update_user(id):
    user.delete_user(int(id))
    return redirect('/')
