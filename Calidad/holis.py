def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-2) + fib(n-1)

#print(fib(7))

if __name__ == "__main__":
    for i in range(1, 10):
        print(i, fib(i))