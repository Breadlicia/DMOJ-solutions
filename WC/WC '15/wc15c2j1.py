N=int(input())
if N==1:
    print("A long time ago in a galaxy "+"far "*N+"away...")
else:
    print("A long time ago in a galaxy "+"far, "*(N-1)+"far away...")