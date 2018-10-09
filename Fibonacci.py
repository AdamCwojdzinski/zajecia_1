def fibonacciIteration(n):
    first_fib = 0
    second_fib = 1
    for i in range(0, n):
        if i <= 1:
            next_fib = i
        else:
            next_fib = first_fib + second_fib
            first_fib = second_fib
            second_fib = next_fib
        print(next_fib)


def fibonacciRecursion(n):
    if n <= 1:
        return n
    else:
        return (fibonacciRecursion(n - 1) + fibonacciRecursion(n - 2))


print("Display Fibonacci Sequence Using Iteration")
while True:
    iter_value = int(input("Enter a positive integer: "))
    if iter_value < 0:
        print("That is not a positive number!")
    else:
        fibonacciIteration(iter_value)
        break
print("Display Fibonacci Sequence Using Recursion")
while True:
    recur_value = int(input("Enter a positive integer: "))
    if recur_value < 0:
        print("That is not a positive number!")
    else:
        for i in range(recur_value):
            print(fibonacciRecursion(i))
        break
