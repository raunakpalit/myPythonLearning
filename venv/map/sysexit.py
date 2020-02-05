import sys

def swapvalues(a, b):
    if b:
        a, b = b, a
        print("a: {}".format(a))
        print("b: {}".format(b))
    else:
        # print("Nothing in b")
        sys.exit(1)
    print("Swapping done")

swapvalues(1, 1)
    