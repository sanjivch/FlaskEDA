from flask import Flask
import datetime
# now = datetime.datetime.now()
app = Flask(__name__)


@app.route('/')
def hello():
    return str(datetime.datetime.now())


@app.route('/test')
def test():
    return 'Test'