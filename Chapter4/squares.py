squares = []
# Values 1-10
# for value in range(1,11):
    # value ^ 2
    # square = value ** 2
    # squares.append(square)

    # More efficient code
    # squares.append(value ** 2)

# LIST COMPREHENSION
# an even more efficient way
# of doing what we did above

squares = [value ** 2 for value in range (1,11)]

print(squares)
print("Max value:", max(squares))
print("Min value:", min(squares))
print("Sum value:", sum(squares))


