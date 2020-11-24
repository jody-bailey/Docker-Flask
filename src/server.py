from flask import Flask
from flask import render_template
server = Flask(__name__)

@server.route("/")
def hello():
    return render_template('index.html')

@server.route("/info")
def info():
    return render_template('info.html')

if __name__ == "__main__":
   server.run(host='0.0.0.0')