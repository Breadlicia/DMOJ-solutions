Song=input()
Last=len(Song) # also doesn't work now because the element in the array will be counted but whatever
Last-=1
# Song=Song.replace("|","")
# divide into array, and count first character of everything in the array
Song=Song
A1=Song.count('A')
A2=Song.count('D')
A3=Song.count('E')
Atotal=A1+A2+A3
C1=Song.count('C')
C2=Song.count('F')
C3=Song.count('G')
Ctotal=C1+C2+C3

if Atotal>Ctotal:
    print('A-mol')
elif Ctotal>Atotal:
    print('C-dur')
else:
    if Song[Last]=='A':
        print('A-mol')
    if Song[Last]=='C':
        print('C-dur')