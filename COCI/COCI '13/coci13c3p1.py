# this used too much memory, so doesn't work
Sentence='A'
N=int(input())
for x in range(N):
    Sentence = Sentence.replace('A', 'X').replace('B', 'Y').replace('X', 'B').replace('Y', 'BA')
Acount=Sentence.count('A')
Bcount=Sentence.count('B')
print(str(Acount)+" "+str(Bcount))