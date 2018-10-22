from flask import render_template, logging

from . import index_blue

@index_blue.route('/')
def index():
    # print('come here')
    # set_log()
    return render_template('index.html')

def set_log():
    logging.log(logging.DEBUG, "This is a debug log.")
    logging.log(logging.INFO, "This is a info log.")
    logging.log(logging.WARNING, "This is a warning log.")
    logging.log(logging.ERROR, "This is a error log.")
    logging.log(logging.CRITICAL, "This is a critical log.")

