print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

user_input = int(input("Please enter a number to get the square of: "))

squares = []
for number in numbers:
    squares.append(number ** 2)

index_pos = numbers.index(user_input)
print(squares[index_pos])
# print(squares)
