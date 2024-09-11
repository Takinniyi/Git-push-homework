list_of_food_items = {
  "Baja Taco": 4.25,
  "Burrito": 7.50,
  "Bowl": 8.50,
  "Nachos": 11.00,
  "Quesadilla": 8.50,
  "Super Burrito": 8.50,
  "Super Quesadilla": 9.50,
  "Taco": 3.00,
  "Tortilla Salad": 8.00
}
items = []
total = 0
try:
  while True:
      item = input("Item: ").title()
      if item == "":
          break
      if item in list_of_food_items:
          items.append(item)
          total += list_of_food_items[item]
          print("Total:", f"${total:.2f}")
      else:
          print(f"{item} is not available.")
  print("Items purchased:")
  for item in items:
      print(f"{item}: {list_of_food_items[item]}")
  print(f"Total: {total}")
except EOFError:
    print("\nTotal:", total)
print()
