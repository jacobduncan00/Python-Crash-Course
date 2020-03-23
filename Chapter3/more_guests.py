glist = ['blaine', 'lexi', 'justin', 'daniel', 'tj']
print("Found more people!")
glist.insert(0, "jeff")
glist.insert(3, "damien")
glist.append("ben")
for i in range(0,8):
    print("{}, will you come to my dinner?".format(glist[i].title()))
