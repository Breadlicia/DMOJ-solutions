password=str(input())
lowercase=0
uppercase=0
digit=0
if all(x.isupper() or x.islower() or x.isdigit() for x in password) and 8<=len(password)<=12:
    for y in password:
        if y.islower():
            lowercase+=1
        if y.isupper():
            uppercase+=1
        if y.isdigit():
            digit+=1
    if lowercase>=3 and uppercase>=2 and digit>=1:
        print('Valid')
    else:
        print('Invalid')
else:
     print('Invalid')
