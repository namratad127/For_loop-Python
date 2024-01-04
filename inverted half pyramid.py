'''inverted half pyramid with *'''
n=6
for i in range(n+1):
    for j in range(n,i,-1):
        print("*",end="")
    print()

'''inverted half pyramid with integer'''
for i in range(6,0,-1):
    for j in range(1,i,+1):
        print(j,end="")
    print()