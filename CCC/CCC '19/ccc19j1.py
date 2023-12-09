A3Point=int(input())
A2Point=int(input())
A1Point=int(input())
B3Point=int(input())
B2Point=int(input())
B1Point=int(input())
AFinalScore=A3Point*3+A2Point*2+A1Point
BFinalScore=B3Point*3+B2Point*2+B1Point
if AFinalScore > BFinalScore:
    print("A")
elif BFinalScore > AFinalScore:
    print("B")
else:
    print("T")