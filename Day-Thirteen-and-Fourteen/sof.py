import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def get_pages(pagetag):
  spans = pagetag.find_all("span")
  last_page = int(spans[-2].get_text())
  return last_page

def get_job_sof(keyword):
  url = f"https://stackoverflow.com/jobs?r=true&q={keyword}"
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = get_pages(soup.find("div", {"class":"s-pagination"}))
  infos = []
  jobid = []
  for page in range(1, pages+1):
    current_url = f"{url}&pg={page}"
    print(current_url)
    r = requests.get(current_url)
    s = BeautifulSoup(r.text, "html.parser")
    divs = s.find_all("div")
    jobs = []
    for div in divs:
      try:
        if div["data-jobid"]:
          if div["data-jobid"] not in jobid:
            jobid.append(div["data-jobid"])
            jobs.append(div)
      except:
        continue
    for job in jobs:
      info = {}
      atag = job.find("h2").find("a")
      info["title"] = atag.get_text()
      info["company"] = job.find("h3").find("span").get_text().strip()
      link = atag["href"]
      info["link"] = f"https://stackoverflow.com{link}"
      infos.append(info)
  return infos