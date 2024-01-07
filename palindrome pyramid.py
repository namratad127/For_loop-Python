'''left palindrome pyramid'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()


'''center palindrome pyramid'''
n=5
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    for l in range(i-1,0,-1):
        print(l,end="")
    print()

'''left alphabetic palindrome pyramid'''
for i in range(1,7):
    for j in range(65,65+i):
        print(chr(j),end="")
    for k in range(63+i,64,-1):
        print(chr(k),end="")
    print()

