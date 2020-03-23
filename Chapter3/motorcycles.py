motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Reassigning index 0
motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# Appending onto end of list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Inserting element into list
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing element
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# Using pop instead of del
# allows you to work with the
# data you removed from list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped = motorcycles.pop()
print(motorcycles)
print(popped)

# Useful example
last_owned = motorcycles.pop()
print("My last owned motorcycle was a {}".format(last_owned))

# Popping from any position
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
first_owned = motorcycles.pop(0)
print("My first owned motorcycle was a {}".format(first_owned))

# You can even remove by value
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

# Example
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print("A {} is too expensive for me".format(too_expensive.title()))



