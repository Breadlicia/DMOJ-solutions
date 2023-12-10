Song=input()
SongUnedited=Song
Song=Song.split('|')
Song=[word[0] for word in Song]
Song=''.join(Song)
Length=len(SongUnedited)
Length-=1
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
    if SongUnedited[Length]=='A':
        print('A-mol')
    elif SongUnedited[Length]=='C':
        print('C-dur')