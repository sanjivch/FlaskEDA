from flask import Flask
import datetime
# now = datetime.datetime.now()
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Last refreshed at'+ str(datetime.datetime.now())


@app.route('/test')
def test():
    return 'Test'