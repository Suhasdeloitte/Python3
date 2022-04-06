#write a decorator which will take a function and execute it twice.
def multiply_div(func):
    def inner1(num1,num2):
        print("inner function" , num1*num2)
        func(num1,num2)

    return inner1

@multiply_div
def multiply(num1, num2):
    print(num1 * num2)
multiply(3,4)

print()

#Create a generator to return the fibonnaci sequence starting from the first elementup to (n). The first numbers of the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, . . .

print("Fibonacci Series")
def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        a, b = b, a + b # Adds values together then swaps them



for x in fib(100):
    print(x)