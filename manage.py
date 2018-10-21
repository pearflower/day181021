from flask import Flask
from info.moduel.index import index_blue

app = Flask(__name__)

app.register_blueprint(index_blue)


def main():
    app.run()


if __name__ == '__main__':
    main()