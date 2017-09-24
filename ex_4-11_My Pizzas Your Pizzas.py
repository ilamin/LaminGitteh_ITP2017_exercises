pizzas = ['Marinara', 'Mac & Cheese', 'Salad']
friend_pizzas = ['Marinara', 'Mac & Cheese', 'Salad']
pizzas.insert(0, "Mushroom")
friend_pizzas.insert(2, "Mexican Piazza")
print("My favorite pizzas are:")
for i in pizzas:
    print(i)
print("\n")

print("My friend’s favorite pizzas are: ")
for i in friend_pizzas:
    print(i)