import os
import requests

ans = 'y'
while ans=='y':
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (separated by comma)")

  str_input = input()
  urls = str_input.split(',')

  for url in urls:
    url = url.strip()
    check = url.lower()
    if "http" not in check:
      check = "http://"+check
    try:
      r = requests.get(check)
      if r.status_code == 200:
        print(check,"is up!")
      else:
        print(check,"is down!")
    except:
      print(url,"is not a valid URL.")

  while True:
    print("Do you want to start over? y/n")
    ans = input()
    if ans=='y':
      os.system('clear')
      break
    elif ans=='n':
      print("k. bye!")
      break
    else:
      print("That's not a valid answer")
