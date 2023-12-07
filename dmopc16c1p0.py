Width = int(input())
Cheese = int(input())

if 3>=Width>=1 and 100>=Cheese>=0:
    if Width == 3 and Cheese>=95:
        M="absolutely"
    elif Width == 1 and Cheese<=50:
        M="fairly"
    else:
        M="very"
else:
    print("input invalid")

print("C.C. is "+M+" satisfied with her pizza.")