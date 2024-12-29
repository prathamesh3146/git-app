from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return "Welcome to the flask server"

@app.route('/test', methods=['GET'])
def test():
    return "this is a test route"

app.run(host="0.0.0.0", port=5000, debug=True)