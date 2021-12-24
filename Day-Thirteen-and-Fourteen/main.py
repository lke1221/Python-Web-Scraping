"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
from flask import Flask, render_template, request, redirect, send_file
from sof import get_job_sof
from wwk import get_job_wwk
from rmt import get_job_rmt
from save import save_to_file

db={}

app = Flask("FindJob")

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/job")
def find_job():
  keyword = request.args.get("keyword").lower()
  if keyword:
    fromDB = db.get(keyword)
    if fromDB:
      return render_template("result.html", keyword=keyword, cnt=len(fromDB), job_list=fromDB)
    else:
      sof_list = get_job_sof(keyword)
      wwk_list = get_job_wwk(keyword)
      rmt_list = get_job_rmt(keyword)
      job_list = sof_list+wwk_list+rmt_list
      db[keyword] = job_list
      return render_template("result.html", keyword=keyword, cnt=len(job_list), job_list=job_list)
  else:
    redirect("/")

@app.route("/save")
def save_job():
  keyword = request.args.get("keyword")
  if keyword:
    jobs = db.get(keyword)
    if jobs:
      save_to_file(keyword, jobs)
      return send_file(f"{keyword}.csv", as_attachment = True,attachment_filename=f"{keyword}.csv")
    else:
      return redirect("/")
  else:
    return redirect("/")

app.run(host="0.0.0.0")