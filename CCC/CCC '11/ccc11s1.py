N = int(input())
paragraph=[]
for x in range(N):
    sentence=input()
    paragraph.append(sentence)
paragraph = ' '.join(paragraph)
paragraph = paragraph.lower()
TCount=paragraph.count('t')
SCount=paragraph.count('s')
if TCount>SCount:
    print('English')
if SCount>TCount:
    print('French')
if TCount==SCount:
    print('French')