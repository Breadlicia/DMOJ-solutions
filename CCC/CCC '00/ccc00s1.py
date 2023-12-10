quarters = int(input())
slot1 = int(input())
slot2 = int(input())
slot3 = int(input())
play = 0
machine = 0

while quarters > 0:
    quarters -= 1
    play += 1
    if machine == 0:
        slot1+=1
        if slot1 == 35:
            quarters +=30
            slot1 =0
    elif machine == 1:
        slot2 += 1
        if slot2 == 100:
            quarters += 60
            slot2=0
    elif machine ==2:
        slot3 += 1
        if slot3 == 10:
            quarters += 9
            slot3 = 0
    machine+=1
    if machine==3:
        machine=0

print("Martha plays " + str(play) + " times before going broke.")