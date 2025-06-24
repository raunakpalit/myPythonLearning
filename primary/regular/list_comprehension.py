'''List comprehensions'''

squares = []

for i in range(10):
    squares.append(i*i)

print(squares)

square = [i*i for i in range(10)]
print(square)

even = [i for i in range(1, 10) if i%2==0]
print(even)

