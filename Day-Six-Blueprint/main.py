import os
import requests
from bs4 import BeautifulSoup
from parse import get_info_list
from selection import get_input
from babel.numbers import format_currency

URL = "https://wise.com/gb/currency-converter/"

def ask_amount(code_one, code_two):
  print(f"\nHow many {code_one} do you want to conver to {code_two}?")
  try:
    num = int(input())
  except:
    print("That wasn't a number.")
    return ask_amount(code_one, code_two)
  return num

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

infos = get_info_list()
print("Welcome to CurrencyConvert PRO 2000\n")
for i, name in enumerate(infos):
  print(f"# {i} {name[0]}")

print("\nWhere are you from? Choose a country by number.\n")
index_one = get_input(len(infos)-1)
country_one = infos[index_one]
print(f"{country_one[0]}")

print("\nNow choose another country.\n")
index_two = get_input(len(infos)-1)
country_two = infos[index_two]
print(f"{country_two[0]}")

code_one = country_one[2]
code_two = country_two[2]

amount = ask_amount(code_one, code_two)
r = requests.get(f"{URL}{code_one.lower()}-to-{code_two.lower()}-rate?amount=50")
soup = BeautifulSoup(r.text, "html.parser")
convert = soup.find("span", {"class":"text-success"}).string
result = float(convert)*amount
amount_in_format = format_currency(amount, code_one, locale = "ko_KR")
result_in_format = format_currency(result, code_two, locale="ko_KR")

print(f"{amount_in_format} is {result_in_format}")