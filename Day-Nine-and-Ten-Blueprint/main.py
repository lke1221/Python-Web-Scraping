import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"

db= {}

# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")

@app.route("/")
def home():
  order_by = request.args.get('order_by')
  if order_by == "new":
    fromDb = db.get("new")
    if fromDb:
      news = fromDb
      return render_template("index.html", order=order_by, hits = db["new"].get("hits"))
    else:
      news = requests.get(new)
      db["new"] = news.json()
      return render_template("index.html", order=order_by, hits = db["new"].get("hits"))
  else:
    fromDb = db.get("popular")
    if fromDb:
      news = fromDb
      return render_template("index.html", order=order_by, hits = db["popular"].get("hits"))
    else:
      news = requests.get(popular)
      db["popular"] = news.json()
      return render_template("index.html", order=order_by, hits = db["popular"].get("hits"))

@app.route("/<id>")
def get_detail(id):
  url = make_detail_url(id)
  result = requests.get(url)
  return render_template("detail.html", detail = result.json())


app.run(host="0.0.0.0")