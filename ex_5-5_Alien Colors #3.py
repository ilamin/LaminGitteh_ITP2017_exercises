print("ALIEN POINT")
alien_color = input("SHOOT WITH \nType here: ")

if 'green' in alien_color:
    print("The player earned 5 points")
elif 'yellow' in alien_color:
    print("The player earned 10 points")
elif 'red' in alien_color:
    print("The player earned 15 points")
else:
    print("OVER!")