dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

# Cannot do this
# cannot assign new value
# to a tuple object

# dimensions[0] = 250

# Defining tuple with
# one object

my_t = (3,)

# In order to "over-write"
# you must reinitialize values
# in tuple

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


