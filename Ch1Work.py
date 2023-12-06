import math
Paint=int(input())
PaintUsed=int(input())
Price=int(input())
Badges=Paint/PaintUsed
Badges=math.floor(Badges)
RemainingPaint=Paint-(Badges*PaintUsed)
FinalPrice=(Badges*Price)+RemainingPaint
print(FinalPrice)