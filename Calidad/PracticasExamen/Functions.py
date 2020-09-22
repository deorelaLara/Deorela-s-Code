def add(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiply(x, y):
    return x * y 

def divide(x, y):
    if y == 0:
        print('ERROR Can not divide by zero!')
    return x/y


if __name__ == "__main__":
    print(add(10,15))