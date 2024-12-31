n=int(input())
print("*"*n)
for i in range(n-2):
    print('*',end="")
    print(' '*(n-3-i),end="")
    print('*')
print('*')