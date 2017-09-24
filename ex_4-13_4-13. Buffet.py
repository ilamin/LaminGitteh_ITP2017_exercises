foods = ['Rice','Nasi Goreng','Meat Pie','Fish Pie', 'Sate', 'Chicken']
print("\tFOOD MENU\n..................")
for i in foods:
    print(i)
newfoods = foods
del newfoods[0]
del newfoods[0]
newfoods.insert(0, "Bebek")
newfoods.insert(1, "Fries")
print("\n")

print("\tNEW MENU\n..................")
for x in foods:
    print(x)