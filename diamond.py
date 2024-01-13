'''solid diamond'''
n=5
for i in range(1,n+1):
    print(" " * (n-i) + "*" * (2*i-1))
for i in range(n-1,0,-1):
    print(" " * (n-i) + "*" * (2*i-1))



'''solid half diamond'''
n=6
for i in range(1,n+1):
    print("*" * (i))

for i in range(n-1):
    print("*" * (n-i-1))

'''solid half diamond with integer'''
for i in range(1,7):
    for j in range(i):
        print(j,end="")
    print()
