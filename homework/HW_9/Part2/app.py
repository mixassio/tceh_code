# -*- coding: utf-8 -*-

import random

from flask import Flask, request, jsonify
from flask import render_template


class Storage(object):  # storage = Storge()
    obj = None
    users = None
    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.users = []
        return cls.obj
    def add(self, user):
        self.users.append(user)
    def dell(self, user):
        self.users.remove(user)
    def get(self, index):
        return self.users[index]

class User(object):
    def __init__(self, username, email):
        self.username = username
        self.email = email
    def __eq__(self, other):
        return self.username == other.username
    def to_json(self):
        return {
            'username': self.username,
            'email': self.email,
        }


app = Flask(__name__, template_folder='templates')


@app.route('/user', methods=['GET', 'POST'])
def index():
    storage = Storage()

    if request.method == 'POST':
        data = request.get_json()

        user = User(data['username'], data['email'])
        storage.add(user)

        return jsonify({'status': 'done'})
    elif request.method == 'GET':
        data = [item.to_json() for item in storage.users]
        return jsonify(data)

@app.route('/user/dell', methods=['GET', 'POST'])
def dell_user():
    storage = Storage()

    if request.method == 'POST':
        data = request.get_json()

        user = User(data['username'], data['email'])
        storage.dell(user)

        return jsonify({'status': 'done'})
    elif request.method == 'GET':
        data = [item.to_json() for item in storage.users]
        return jsonify(data)

@app.route('/user/users')
def list_users():
    storage = Storage()
    data = [item.to_json() for item in storage.users]
    return render_template('list_users.txt', data=data)

if __name__ == '__main__':
    app.run(host='localhost', port=4000)