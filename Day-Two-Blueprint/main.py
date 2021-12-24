"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""
def is_on_list(lst, element):
  if type(lst) is list:
    return element in lst
  else:
    return "ERROR"

def get_x(lst, idx):
  if type(lst) is not list:
    return "ERROR"
  num = int(idx)
  if(num >= len(lst) or num < 0):
    return "ERROR"
  return lst[num]

def add_x(lst, element):
  lst.append(element)

def remove_x(lst, element):
  if element in lst:
    lst.remove(element)

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #
