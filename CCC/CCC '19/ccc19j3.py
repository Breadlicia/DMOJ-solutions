N=int(input())
for x in range(N):
    sentence=input()
    prevchar=sentence[0]
    out=[]
    currcharcount=0
    for currchar in sentence:
        if currchar == prevchar:
            currcharcount+=1
        if currchar != prevchar:
            out.append( f'{currcharcount} {prevchar}' )
            prevchar = currchar
            currcharcount=1
    out.append( f'{currcharcount} {prevchar}' )
    out=" ".join(out)
    print(out)