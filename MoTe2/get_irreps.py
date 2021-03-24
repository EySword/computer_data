Name=input('文件名:')
fileName=Name+'-irreps.yaml'
file=open(fileName,'r')
outFile=open(Name+'.txt','w')
lines=file.readlines()

ir=[]
fre=[]
for line in lines:
    if line[:11]=='  frequency':
        fre.append(line.strip())
    if line[:10]=='  ir_label':
        ir.append(line.strip())

file.close()
# print(len(ir),len(fre))
n=len(ir)
for i in range(n):
    outFile.write('{}: {}\n'.format(ir[i][10:],fre[i][11:]))
    # print('{}{}'.format(ir[i],fre[i]))

outFile.close()