year=int(input())
year+=1
while len(set(str(year))) < len(str(year)):
    year+=1

print(year)