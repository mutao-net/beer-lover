from flask import Flask,render_template
import requests

app = Flask(__name__)

# https://punkapi.com/documentation/v2
@app.route("/")
def index():
    url="https://api.punkapi.com/v2/beers/random"
    response = requests.get(url)
    return render_template("index.html", response=response.text)


#おまじない
if __name__ == "__main__":
    app.run(debug=True)