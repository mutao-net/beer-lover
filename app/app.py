from flask import Flask,render_template
import requests
import json

app = Flask(__name__)

# https://punkapi.com/documentation/v2
@app.route("/")
def index():
    url="https://api.punkapi.com/v2/beers"
    headers = {"content-type": "application/json"}
    response = requests.get(url, headers).json()
    return render_template("index.html", response=response)


#おまじない
if __name__ == "__main__":
    app.run(debug=True)