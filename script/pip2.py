import math

"""
读取a，b，c
根据元素对每个原子进行分组，格式为P=[[a,b,c],[]]  c坐标需要调整，调整为以0为中心的
通过a与N计算出周长
得到半径r
建立关于原子的极坐标[[ρ,θ],[,]]，默认ρ为r
算出每个原子a坐标对应在极坐标里的角度
ρ=r+c
极坐标改为直角坐标
直角坐标中加入原来的b
平移坐标
增加边界距离
"""

initPOSCAR=open('POSCAR','r')
Plines=initPOSCAR.readlines()

N=2
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
eleListPolar=[] #极坐标列表
angleRate=2*math.pi/N
for i in range(eleSum):
    #删除末尾元素以首位相接
    eleListCart[i].pop()
    eleListFract[i].pop()
    tempEleListPolar=[]
    for n in range(N):
        for j in range(int(eleNum[i])-1):
            eleData3=eleListCart[i][j]
            # eleData3[0]=angleRate*n+eleListFract[i][j][0]*angleRate
            eleData3[2]=radius+eleData3[2]
            tempEleListPolar.append(eleData3)
            pass
        pass
    eleListPolar.append(tempEleListPolar)
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
    for i in ele:
        for j in i:
            print(j)
            pass
        print('===========')
        pass
    pass

if __name__=="__main__":
    # printPOSCAR(Plines,9,24)
    printEleList(eleListPolar)
    print('')
    printEleList(eleListFract)

pass

initPOSCAR.close()