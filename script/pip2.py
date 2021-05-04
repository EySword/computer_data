import math
import copy
import sys
"""
读取a，b，c
根据元素对每个原子进行分组，格式为P=[[a,b,c],[]]  c坐标需要调整，调整为以0为中心的
通过a与N计算出周长
得到半径r
建立关于原子的极坐标[[ρ,b,θ],[,]]，默认ρ为r
算出每个原子a坐标对应在极坐标里的角度
ρ=r+c
极坐标改为直角坐标
平移坐标
增加边界距离
"""

initPOSCAR=open('POSCAR','r')
Plines=initPOSCAR.readlines()

# N=int(sys.argv[1]) #选择N
N=3
#读取a，b，c

a=float(Plines[2].split()[0])
b=float(Plines[3].split()[1])
c=float(Plines[4].split()[2])
# print(a,b,c)
#获得元素种类以及数量
eleTypeList=Plines[5].split() #名称
eleNum=Plines[6].split() #每个元素的数量
eleSum=len(eleTypeList) #一共有多少种元素
# print(eleNum)
eleListFract=[]#以分数坐标呈现的总元素列表
eleListCart=[]#以直角坐标呈现的总元素列表
#allEleFractionalCoordinates按顺序获得所有原子分数坐标
allEleFractionalCoordinates=Plines[8:24]
allEleFractionalCoordinates.reverse()
# print(len(allEleFractionalCoordinates))
# exec(eleTypeList[0]+'=1')
# print(P)

# 根据元素对每个原子进行分组，格式为P=[[a,b,c],[]]  c坐标需要调整，调整为以0为中心的
for i in range(eleSum):
    tempEleListFract=[]
    tempEleListCart = []
    for j in range(int(eleNum[i])):
        eleData1=(allEleFractionalCoordinates.pop()).split()
        eleData2=[]
        eleData1=list(map(float,eleData1))
        if eleData1[2]>0.5:
            eleData1[2]=eleData1[2]-1.0
        tempEleListFract.append(eleData1)

        eleData2.append(eleData1[0] * a)
        eleData2.append(eleData1[1] * b)
        eleData2.append(eleData1[2] * c)
        # print(eleData)
        tempEleListCart.append(eleData2)

        pass
    eleListFract.append(tempEleListFract)

    eleListCart.append(tempEleListCart)

    pass



#通过a与N计算出周长,得到半径R
perimeter=a*N #周长
radius=perimeter/2/math.pi #半径
# print(radius)

#建立关于原子的极坐标[[θ,b,ρ],[,,]]，默认ρ为r
#算出每个原子a坐标对应在极坐标里的角度，总角度2π，ρ=r+c
eleListPolar=[] #极坐标列表
angleRate=2*math.pi/N
for i in range(eleSum):
    #删除末尾元素以首位相接
    eleListCart[i].pop()
    eleListFract[i].pop()
    tempEleListPolar=[]
    # print("it's ele {}".format(i))
    for n in range(N):
        tempListForN=[]
        # print('it\'s {}'.format(n))
        for j in range(int(eleNum[i])-1):
            eleData3=copy.deepcopy(eleListCart[i][j])
            eleData3[0]=angleRate*n+eleListFract[i][j][0]*angleRate
            eleData3[2]=radius+eleData3[2]
            # eleData3[2] = radius
            tempListForN.append(eleData3)
            # print(eleData3[0],'theta')
            pass
        copyList=copy.deepcopy(tempListForN) #解决append地址不变的问题！！！
        for item in copyList:
            tempEleListPolar.append(item)
        pass

    eleListPolar.append(tempEleListPolar)

    pass


# 极坐标[θ,b,ρ]改为直角坐标[a,b,c],再平移
outListCart=[] #最终的直角坐标
outEleNum=len(eleListPolar[0]) #最终每个元素的数量（必须数量一样！！！！）

for i in range(eleSum):
    tempList=[]
    for j in range(outEleNum):
        tempOutData=copy.copy(eleListPolar[i][j])
        theta=tempOutData[0]
        ro=tempOutData[2]
        tempOutData[0]=math.cos(theta)*ro+radius
        tempOutData[2]=math.sin(theta)*ro+radius

        # print(tempOutData)
        tempList.append(tempOutData)
        pass
    tempListCopy=copy.deepcopy(tempList)
    outListCart.append(tempListCopy)
    pass

# 增加边界距离
outa=radius*2+15
outb=b
outc=radius*2+15

# print(outa,outb,outc)
#写入新的POSCAR

newPOSCAR=open('pipPOSCAR_N'+str(N),'w')
newPOSCAR.writelines(Plines[:2])
newPOSCAR.writelines('    '+str(outa)+'    0.0000000000000000    0.0000000000000000\n')
newPOSCAR.writelines('     0.0000000000000000    '+str(outb)+'    0.0000000000000000\n')
newPOSCAR.writelines('     0.0000000000000000    0.0000000000000000   '+str(outc)+'\n')
newPOSCAR.writelines(Plines[5])
newPOSCAR.writelines('     '+str(outEleNum)+'     '+str(outEleNum)+'\n')
newPOSCAR.writelines(Plines[7])
for element in outListCart:
    for item in element:
        lineText='  '+str(item[0]/outa)+'  '+str(item[1]/outb)+'  '+str(item[2]/outc)
        newPOSCAR.writelines(lineText+'\n')
        pass
    pass

def printPOSCAR(Plines,start=1,end=41):
    '''
    打印完整POSCAR
    :param Plines: 输入Plines
    :return: non
    '''
    for i in range(start-1,end):
        print(Plines[i],end='')
        pass
    pass

def printEleList(ele):
    '''
    打印元素列表
    :param eleList:
    :return:
    '''
    print('start:')
    for i in ele:
        for j in i:
            print(j)
            pass
        print('======one ele over======')
        pass
    print('end')
    pass


if __name__=="__main__":
    # printPOSCAR(Plines)
    # printEleList(eleListPolar)
    # printEleList(eleListFract)
    # printEleList(eleListCart)
    # printEleList(outListCart)
    print('')
pass

initPOSCAR.close()
newPOSCAR.close()