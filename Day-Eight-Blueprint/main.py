import os
import csv
import requests
from bs4 import BeautifulSoup

def parse(url):
  result = requests.get(alba_url)
  soap = BeautifulSoup(result.text, "html.parser")
  superbrand = soap.find("div", {"id":"MainSuperBrand"}).find_all("li")
  infos = []
  for s in superbrand:
    info = []
    link = s.find("a", {"class":"goodsBox-info"})
    company = s.find("span", {"class": "company"})
    if link is not None and company is not None:
      info.append(link["href"])
      info.append(company.string)
      infos.append(info)
  return infos

def each_brand(infos):
  for info in infos:
    brand_url = info[0]+"/job/brand"
    brand_name = info[1]
    result = requests.get(brand_url)
    soup = BeautifulSoup(result.text, "html.parser")
    try:
      jobCount = int(soup.find("div", {"id":"NormalInfo"}).find("p", {"class":"jobCount"}).find("strong").string.replace(",",""))
      job_list = []
      if jobCount != 0:
        pages = jobCount//50+1
        for i in range(pages):
          pr = requests.get(brand_url+f"/?page={i+1}")
          prsoup = BeautifulSoup(pr.text, "html.parser")
          job_list_tr = prsoup.find("div", {"id":"NormalInfo"}).find("table").find_all("tr")
          for tr in job_list_tr:
            info = {}
            loc = tr.find("td", {"class":"local first"})
            if loc is not None:
              info["loc"] = loc.get_text().replace("\xa0"," ")
            company = tr.find("td", {"class":"title"})
            if company is not None:
              info["company"] = company.find("span", {"class" : "company"}).get_text().strip()
            worktime = tr.find("td", {"class":"data"})
            if worktime is not None:
              info["worktime"] = worktime.get_text()
            pay = tr.find("td", {"class":"pay"})
            if pay is not None:
              info["pay"] = pay.get_text()
            rtime = tr.find("td",{"class":"regDate last"})
            if rtime is not None:
              info["rtime"] = rtime.get_text()
              job_list.append(info)
      file = open(f"{brand_name}.csv", mode="w")
      writer = csv.writer(file)
      writer.writerow(["place", "title", "time", "pay", "date"])
      for job in job_list:
        writer.writerow(list(job.values()))
    except:
      continue

os.system("clear")
alba_url = "http://www.alba.co.kr"

infos = parse(alba_url)
job_list = each_brand(infos)
