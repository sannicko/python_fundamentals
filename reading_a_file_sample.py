import json

look_up = input("What software acronym would you like to look up?\n").upper()
found = False

with open('/Users/sannicko/Downloads/clean.json') as file:
  data = json.load(file)
  if look_up == "ALL":
    count = 0
    for item in data:
      print(f"Abbreviation: {item['Abbreviation']}")
      print(f"Definition: {item['Definition']}")
      print()
      count += 1
    print(f"Total number of items: {count}")
    found = True
  else:
    for item in data:
      if look_up == item['Abbreviation']:
        print(f"Definition: {item['Definition']}")
        found = True
        break

if not found:
  print('Acronym not found')