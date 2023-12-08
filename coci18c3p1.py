sentence=input()
y=''
H=0
O=0
N=0
I=0
for x in sentence:
    if H>=1:
        y=x
        if x=='H' and y=='' or y=='I':
            H+=1
        elif x=='O' and y=='H':
            O+=1
        elif x=='N' and y=='O':
            N+=1
        elif x=='I' and y=='N':
            I+=1
        else:
            H=H
    if x=='H' and y=='' or y=='I':
        H+=1
    if x=='O' and y=='H':
        O+=1
    if x=='N' and y=='O':
        N+=1
    if x=='I' and y=='N':
        I+=1
    else:
        H=H
Total=H+O+N+I
Total=int(Total/4)
print(Total)