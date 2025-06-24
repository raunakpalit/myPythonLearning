def myfunc():
    return "This is my function"

def myfuncadd(a, b):
    return a+b

print(__name__)
if __name__ == '__main__':
    print(myfunc())
    print(myfuncadd(2, 3))
