from flask import render_template

from . import index_blue

@index_blue.route('/')
def index():
    # print('come here')
    return render_template('index.html')

