name=input('Input name:')

POSCAR = open('POSCAR','r')
read = open(name,'r')
write = open(name+'compare.txt','w')

POSCARdata=[]
poscarLineNumber=1
for i in POSCAR.readlines():
    if poscarLineNumber>=9:
        POSCARdata.append(i.strip().split('  '))
        pass
    poscarLineNumber+=1
    #将坐标放入POSCARdata中,为2级列表

readData=[]
readLineNumber=1
for i in read.readlines():
    if readLineNumber>=9 and readLineNumber<=18:
        readData.append(i.strip().split('  '))
        pass
    readLineNumber+=1
    #将坐标放入raedData中,为2级列表

elementNumber=len(POSCARdata)
print(elementNumber)
resule=[[None for j in range(3)]for i in range(elementNumber)]
#结果写入result
for line in range(0,10):
    for number in range(0,3):
        # resule[line][number]=float([line][number])-float(POSCARdata[line][number])
        resule[line][number] = float(readData[line][number]) - float(POSCARdata[line][number])
        pass
    pass

#写入新文件
for line in range(0,10):
    for number in range(0,3):
        write.write(str('%.17f'%resule[line][number])+'   ')
        pass
    write.write('\n')

# if __name__=='__main__':
#     for i in resule:
#         print(i)
#
#     pass


POSCAR.close()
read.close()
write.close()