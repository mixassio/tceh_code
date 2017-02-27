# -*- coding: utf-8 -*-
import random
from flask import Flask, render_template
from flask import request

app = Flask(__name__, template_folder='templates')

value_rand = random.randint(0,51)
val = 0

@app.route('/<int:first>')
def get_sum(first):
    global value_rand
    if value_rand == first:
        global val
        val += 1
        value_rand = random.randint(0, 51)
        return render_template('report_true.txt', data = first, sum = val)
    else:
        if first < value_rand:
            return render_template('report_false.txt', val = 'меньше', data = first, sum = val)
        else:
            return render_template('report_false.txt', val='больше', data = first, sum = val)


if __name__ == '__main__':
    app.run(host='localhost', port=4000)