month=int(input())
day=int(input())

if 1<=month<=12 and 1<=day<=31:
    if month<2 or (month==2 and day<18):
        print("Before")
    elif month>2 or(month==2 and day>18):
        print("After")
    else:
        print("Special")
else:
    print("invalid date")