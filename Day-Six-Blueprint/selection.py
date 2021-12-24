def get_input(max_num):
  try:
    num = int(input("#: "))
  except:
    print("That wasn't a number.")
    return get_input(max_num)

  if num<0 or num>max_num:
    print("Choose a number from the list.")
    return get_input(max_num)
  else:
    return num