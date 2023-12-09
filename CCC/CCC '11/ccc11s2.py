N=int(input())
student=[]
answer=[]
C=0
for x in range(N):
    inputing=input()
    student.append(inputing)
for x in range(N):
    inputing=input()
    answer.append(inputing)
for x in range(N):
    if student[x]==answer[x]:
        C+=1
    else:
        pass
print(C)