glist = ['blaine', 'lexi', 'justin', 'daniel', 'tj']
remove_person = glist.pop(2)
print("{} can't make it!".format(remove_person))
add_person = "kyle"
glist.insert(2, add_person)
for i in range(0,5):
    print("{}, will you come to my dinner?".format(glist[i].title()))
