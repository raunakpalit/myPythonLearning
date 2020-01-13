# Create a generator to return an infinite sequence of odd numbers, starting at 1.
# Print the first 100 numbers, to check that the generator is working correctly.
# Note that this is just for testing. We are going to need far more than 100 numbers,
# and do not know in advance how many, so that is why we are creating our own generator, 
# instead of just using range.

def generate_odd():
    number = 1
    while True:
        yield number
        number = number + 2

genOdd = generate_odd()

# for i in range(100):
#     print(next(genOdd))

def pi_series():
    odds = generate_odd()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation

approx_pi = pi_series()

for x in range(10000000):
    print(next(approx_pi))