FinalA=0
FinalB=0

for x in range(1,int(input())+1):
    A=0
    B=0
    game1=input().split()
    if game1==['R','S']:
        A=+1
    elif game1==['P','S']:
        A=+1
    elif game1==['S','P']:
        A=+1
    elif game1==['S','R']:
        B=+1
    elif game1==['S','P']:
        B=+1
    elif game1==['P','S']:
        B=+1
    else:
        A=A
        B=B

    game2=input().split()
    if game2==['R','S']:
        A=+1
    elif game2==['P','S']:
        A=+1
    elif game2==['S','P']:
        A=+1
    elif game2==['S','R']:
        B=+1
    elif game2==['S','P']:
        B=+1
    elif game2==['P','S']:
        B=+1
    else:
        A=A
        B=B

    game3=input().split()
    if game3==['R','S']:
        A=+1
    elif game3==['P','S']:
        A=+1
    elif game3==['S','P']:
        A=+1
    elif game3==['S','R']:
        B=+1
    elif game3==['S','P']:
        B=+1
    elif game3==['P','S']:
        B=+1
    else:
        A=A
        B=B

    game4=input().split()
    if game4==['R','S']:
        A=+1
    elif game4==['P','S']:
        A=+1
    elif game4==['S','P']:
        A=+1
    elif game4==['S','R']:
        B=+1
    elif game4==['S','P']:
        B=+1
    elif game4==['P','S']:
        B=+1
    else:
        A=A
        B=B
    
    game5=input().split()
    if game5==['R','S']:
        A=+1
    elif game5==['P','S']:
        A=+1
    elif game5==['S','P']:
        A=+1
    elif game5==['S','R']:
        B=+1
    elif game5==['S','P']:
        B=+1
    elif game5==['P','S']:
        B=+1
    else:
        A=A
        B=B
    
    if A>B:
        FinalA=+1
        A=0
        B=0
    elif B>A:
        FinalB=+1
        A=0
        B=0
    else:
        A=0
        B=0

if finalA > finalB:
    print("A "+str(finalA))
elif finalB > finalA:
    print("B "+str(finalB))
else:
    print("TIE")