a=[[None for i in range(3)] for i in range(3)]
print(a)
for i in range(0,3):
    for j in range(0,3):
        a[i][j]=1

print(len(a))