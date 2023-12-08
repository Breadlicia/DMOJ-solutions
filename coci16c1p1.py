mbpermonth=int(input())
months=int(input())
total=mbpermonth*(months+1)
for x in range(months):
    y=int(input())
    total=total-y
print(total)