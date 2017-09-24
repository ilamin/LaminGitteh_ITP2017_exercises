#THIS PROGRAM WILL TAKE 2 INPUTS FROM A USER THEN GIVES BACK A ANSWER DEPENDING ON THE OPERATION.

print("ENTER YOUR FIRST NUMBER")
no1 = int(input())
print("ENTER YOUR SECOND NUMBER")
no2 = int(input())
print("CHOOSE OPERATIONS : - | * | / | + ")
op = input()
if op == str("-"):
    print(no1 - no2)
elif op == str("*"):
    print(no1 * no2)
elif op == str("/"):
    print(no1 / no2)
elif op == str("+"):
    print(no1 + no2)
elif op != "+" or "-" or "/" or "*":
    print("ERROR")

#THIS PART OF THE PROGRAM TAKES USERS'S INPUT AND GIVES BACK THE LENGTH OF THE INPUT

print("ENTER ANY WORD OR NAME")
name = input()
length = name.replace(' ', '')
print(length)
print("The input consist of : " + str(len(length)) + " characters ")

