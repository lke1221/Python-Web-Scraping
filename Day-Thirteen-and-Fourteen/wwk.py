import requests
from bs4 import BeautifulSoup

def get_job_wwk(keyword):
  url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
  print(url)
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  sections = soup.find_all("section", {"class":"jobs"})
  infos = []
  for section in sections:
    lis = section.find_all("li")
    lis = lis[:-1]
    for li in lis:
      info = {}
      atags = li.find_all("a")
      info["title"] = li.find("span", {"class":"title"}).get_text()
      info["company"] = li.find("span", {"class":"company"}).get_text()
      link = atags[1]["href"]
      info["link"] = f"https://weworkremotely.com{link}"
      infos.append(info)
  return infos