# Takes too long
owner=input()
owners={owner}
for x in range(int(input())):
    duel=input().split()
    if owner==duel[0] or owner==duel[1]:
        owner=duel[0]
    else:
        owner=owner
owners.add(owner)
print(owner)
print(len(owners))