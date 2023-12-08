movement=input()
ballpos=1

for x in movement:
    if x=='A' and ballpos==1:
        ballpos=2
    elif x=='A' and ballpos==2:
        ballpos=1
    elif x=='B' and ballpos==2:
        ballpos=3
    elif x=='B' and ballpos==3:
        ballpos=2
    elif x=='C' and ballpos==3:
        ballpos=1
    elif x=='C' and ballpos==1:
        ballpos=3
    else:
        ballpos=ballpos

print(ballpos)