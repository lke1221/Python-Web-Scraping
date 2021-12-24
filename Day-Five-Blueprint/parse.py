import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"

def get_info_list():
  r = requests.get(url)
  soup = BeautifulSoup(r.text, "html.parser")
  tr = soup.find_all("tr")

  countries = []
  for td in tr:
    countries.append(td.find_all("td"))

  infos = []
  for country in countries:
    info_per_country = []
    for info in country:
      info_per_country.append(info.string)
    infos.append(info_per_country)

  infos = infos[1:]
  return infos