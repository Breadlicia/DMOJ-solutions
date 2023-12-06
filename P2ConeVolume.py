import math

radius = int(input())
height = int(input())

if 1<=radius<=100 or 1<=height<=100:
    conevolume = math.pi*radius**2*height*(1/3)
    print(conevolume)
else:
    print("invalid input")
