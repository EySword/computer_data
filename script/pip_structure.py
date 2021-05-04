

initPOSCAR=open('betaCP_POSCAR','r')

file=initPOSCAR.readlines()
i=0
for a in file:
    print(a,end='')
    i+=1
print(i)

initPOSCAR.close()