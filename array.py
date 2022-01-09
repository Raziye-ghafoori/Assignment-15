array=[1,3,2,2,3,1]
s=0
for i in range(len(array)//2):
    if array[i]==array[len(array)-i-1]:
        s=1
    else:
        s=0
        break

if s==1:
    print("motagharen")
else:
    print("na motagharen")