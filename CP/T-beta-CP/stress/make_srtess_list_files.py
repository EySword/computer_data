POSCAR0=open('POSCAR','r')
'''
指定a的梯度生成新POSCAR
'''

data=POSCAR0.readlines()
# print(a)
line_a=data[2]
a=line_a[4:23]
a=float(a)
a_list=[]
for n in range(1,7):
    a_list.append(a*(1+0.05*n))   #这里指定梯度
# print(a_list)

for n in range(1,7):
    line_a_new=line_a[:4]+str(a_list[n-1])+'0'+line_a[23:]
    # print(line_a_new)
    data[2]=line_a_new
    decade=n//10
    unit=n%10
    filename='POSCAR-'+str(decade)+str(unit)
    POSCAR_new=open(filename,'w')
    POSCAR_new.writelines(data)
    POSCAR_new.close()
    print(filename+'has been created')

POSCAR0.close()
