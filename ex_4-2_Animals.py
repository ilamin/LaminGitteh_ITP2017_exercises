print("ANIMALS")
animals = ["dogs", "cats", "birds"]
info1 = [" likes to sing", " are cute", " likes to play"]
for i in animals:
    print(i)

print("\n")
print("ANIMALS")
for i in animals:
    print(i, info1[-1])
    del info1[-1]

print("\n")
print("MESSAGE")
print("Any of these animals would make a bad pet.")