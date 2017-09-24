names = ["Lamin","Arden","Brain"]
names.insert(0,"Muhammad")
names.insert(3,"Midman")
names.append("John")
message = ", I would like you to attend my birthday dinner tonight"
sorry = ", sorry I can only invite 2 people."


print("LIST OF ATTENDEES")
print(names[0]+message)
print(names[1]+message)
print(names[2]+message)
print(names[3]+message)
print(names[4]+message)
print(names[5]+message)
print("\n")

print("LIST OF NON PARTICIPANTS")
first = names.pop(0)
print(first + sorry)
second = names.pop(0)
print(second + sorry)
third = names.pop(0)
print(third + sorry)
forth = names.pop(0)
print(forth + sorry)
print("\n")

print("LIST OF ATTENDEES")
print(names[0] + message )
print(names[1] + message )

del(names[0], names[0])
print("\n")

print("CURRENT LIST")
print(names)

