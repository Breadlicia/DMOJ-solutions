nspaces=int(input())
yesterday=input()
today=input()
yesterdayresults=[]
todayresults=[]
total=0

for x in yesterday:
    if x=='.':
        yesterdayresults.append(0)
    if x=='C':
        yesterdayresults.append(1)
for y in today:
    if y=='.':
        todayresults.append(0)
    if y=='C':
        todayresults.append(1)

for z in range(nspaces):
    if yesterdayresults[z]==todayresults[z] and yesterdayresults[z]>=1:
        total+=1
    else:
        total=total

print(total)