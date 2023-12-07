firstnumber=int(input())
secondnumber=int(input())
thirdnumber=int(input())
fourthnumber=int(input())

# if firstnumber==8 or firstnumber==9:
#     if secondnumber-thirdnumber==0:
#         if fourthnumber==8 or fourthnumber==9:
#             print("ignore")
#         else:
#             print("answer")
#     else:
#         print("answer")
# else:
#     print("answer")

if ((firstnumber==8 or firstnumber==9) and
        (secondnumber==thirdnumber) and
        (fourthnumber==8 or fourthnumber==9)):
    print("ignore")
else:
    print("answer")