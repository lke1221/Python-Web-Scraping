import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]


app = Flask("DayEleven")

@app.route("/")
def home():
  return render_template("home.html", subreddits = subreddits)

@app.route("/read")
def read():
  subreddits = request.args
  results = []
  for subreddit in subreddits:
    url = f"https://www.reddit.com/r/{subreddit}/top/?t=month"
    result = requests.get(url, headers=headers)
    soap = BeautifulSoup(result.text, "html.parser")
    tags = soap.find_all("div",{"data-testid": "post-container"})
    for tag in tags:
      if tag.find("a", {"data-click-id":"body"}):
        info = []
        link = tag.find("a", {"data-click-id":"body"})["href"]
        link = "https://reddit.com"+link
        title = tag.find("h3").get_text()
        upvote = tag.find("div", {"class":"_1rZYMD_4xY3gRcSS3p8ODO _25IkBM0rRUqWX5ZojEMAFQ"}).get_text()
        if upvote[-1]=='k':
          upvote = int(float(upvote[:-1])*1000)
        else:
          upvote = int(upvote)
        info.append(link)
        info.append(title)
        info.append(upvote)
        info.append(f"r/{subreddit}")
        results.append(info)
  results.sort(key=lambda x:-x[2])
  return render_template("read.html", results = results, subreddits = subreddits)

app.run(host="0.0.0.0")