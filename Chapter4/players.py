players = ['charles', 'martina', 'michael', 'florence', 'eli']
# Splicing a list
# this will print players from
# index 0, 1, 2
# so essentially, the first 3 players
print(players[0:3])
# this will print players at
# index 1, 2, 3
print(players[1:4])

# if you do not put a starting
# number in the splice, it will
# start from the beginning
print(players[:4])

# if you do not put a ending
# number in the splice, it will
# go to the end
print(players[2:])

# To print from the end to the beginning
# you would use negatives
print(players[-3:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
# Splicing can be used to loop
for player in players[:3]:
    print(player.title())



