BurgerChoice=int(input())
SideChoice=int(input())
DrinkChoice=int(input())
DessertChoice=int(input())

if BurgerChoice==1:
    BurgerCalories=461
elif BurgerChoice==2:
    BurgerCalories=431
elif BurgerChoice==3:
    BurgerCalories=420
elif BurgerChoice==4:
    BurgerCalories=0

if SideChoice==1:
    SideCalories=100
elif SideChoice==2:
    SideCalories=57
elif SideChoice==3:
    SideCalories=70
elif SideChoice==4:
    SideCalories=0

if DrinkChoice==1:
    DrinkCalories=130
elif DrinkChoice==2:
    DrinkCalories=160
elif DrinkChoice==3:
    DrinkCalories=118
elif DrinkChoice==4:
    DrinkCalories=0

if DessertChoice==1:
    DessertCalories=167
elif DessertChoice==2:
    DessertCalories=266
elif DessertChoice==3:
    DessertCalories=75
elif DessertChoice==4:
    DessertCalories=0

TotalCalories=BurgerCalories+SideCalories+DrinkCalories+DessertCalories
print("Your total Calorie count is "+str(TotalCalories)+".")