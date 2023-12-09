sentence=input()
previouschar='I'
H=0
O=0
N=0
I=0
real=[]
for currentchar in sentence:
    if currentchar=='H' and previouschar=='I':
        real.append(currentchar)
        previouschar=currentchar
    elif currentchar=='O' and previouschar=='H':
        real.append(currentchar)
        previouschar=currentchar
    elif currentchar=='N' and previouschar=='O':
        real.append(currentchar)
        previouschar=currentchar
    elif currentchar=='I' and previouschar=='N':
        real.append(currentchar)
        previouschar=currentchar
real="".join(real)
number=real.count("HONI")
print(number)