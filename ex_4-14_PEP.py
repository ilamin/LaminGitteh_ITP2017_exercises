def fib(n):
    a, b = 0, 1
    while a < n:
         print(a, end=' ')
         a, b = b, a+b
    print()
fib(1000)

fruits = ['Banana', 'Apple', 'Lime']
loud_fruits = [fruit.upper() for fruit in fruits]
print(loud_fruits)
list(enumerate(fruits))
[(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]