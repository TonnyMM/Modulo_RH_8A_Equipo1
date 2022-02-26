from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__, template_folder='../vista', static_folder='../static')
Bootstrap(app)

if __name__ == '__main__':
    app.run(debug=True)

