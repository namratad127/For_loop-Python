''''write a function that can print the below pattern'''

n=3
c=1
for i in range(n+1):
    for j in range(1,i+1):
        print(c,end="")
        c+=1
    print()


n=3
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()








