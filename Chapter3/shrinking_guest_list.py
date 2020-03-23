glist = ['blaine', 'lexi', 'justin', 'daniel', 'tj']
glist.insert(0, "jeff")
glist.insert(3, "damien")
glist.append("ben")
for i in range(0,8):
    print("{}, will you come to my dinner?".format(glist[i].title()))

print("I can invite only 2 people!")
for i in range(0,6):
    temp = glist.pop()

for i in range(0,2):
    print("{}, you're still invited!".format(glist[i].title()))

del glist[0]
del glist[0]
print(glist)


