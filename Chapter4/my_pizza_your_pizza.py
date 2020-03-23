pizzas = ['cheese', 'pepperoni', 'meat', 'hawaiian', 'olive', 'ginger']
friends_pizzas = pizzas[:]
pizzas.append('dessert')
friends_pizzas.append('cake')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)
