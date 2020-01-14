# Create a new Python file - I have called this one "compchallenge1.py"
#
# Use a conditional expression from the previous video to produce 
# a list comprehension that returns the fizzbuzz results.
#
# If a number is divisible by 3, the value should be "fizz".
# If it is divisible by 5, the value should be "buzz".
# If it is divisible by both 3 and 5, the value should be "fizz buzz".
# Finally, if none of those conditions apply, the value will be the number itself.
#
# The code from the end of the last video appears below, so you can check the result.

# for x in range(1, 31):
#     fizzbuzz = "fizz buzz" if x % 15 == 0 else "buzz" if x % 5 == 0 else "fizz" if x % 3 == 0 else str(x)
#     print(fizzbuzz)

fizzbuzz = ["fizz buzz" if x % 15 == 0 else "buzz" if x % 5 == 0 else "fizz" if x % 3 == 0 else str(x) for x in range(1, 31)]
print(fizzbuzz)