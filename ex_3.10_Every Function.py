countries = ["Canada","South Korea","Japan"]
foods = ["Chicken","Beef","Pineapple"]

print(" CHOOSE>>> 1 : For list of countries OR 2: For list for foods I Like")
check = int(input())
if check == 1:
    print("My favorites countries are : ", countries)
elif check == 2:
    print("My favorites foods are : ", foods)
else:
    print("NO INFO")