import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def get_job_rmt(keyword):
  url = f"https://remoteok.io/remote-dev+{keyword}-jobs"
  print(url)
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  trs = soup.find_all("tr")
  infos = []
  for tr in trs:
    try:
      if tr["data-company"]:
        info = {}
        info["title"] = tr.find("h2", {"itemprop":"title"}).get_text()
        info["company"] = tr.find("h3", {"itemprop":"name"}).get_text()
        link = tr.find("a", {"itemprop":"url"})["href"]
        info["link"] = f"https://remoteok.io{link}"
        infos.append(info)
    except:
      continue
  return infos