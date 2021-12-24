import os
from parse import get_info_list
from selection import get_input

os.system("clear")
infos = get_info_list()

print("Hello! Please choose select a country by number:")
for i, name in enumerate(infos):
  print(f"# {i} {name[0]}")

index = get_input(len(infos)-1)
info = infos[index]

print(f"You chose {info[0]}")
print(f"The currency code is {info[2]}")