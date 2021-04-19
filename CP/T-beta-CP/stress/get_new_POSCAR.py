import os
import sys
'''
把POSCAR的a进行比例变换
第一个参数是初始比例，如1.05
第二个参数是目标比例，如1.20
第三个参数决定是否复制其他文件，1是，0否
'''

init=float(sys.argv[1])#初始的比例
aim=float(sys.argv[2])#目标比例
ismv=int(sys.argv[3])#是否复制其他文件

percent_aim=((aim-1)*100)//1 #得到目标比例的百分比数字，如5%
percent_aim=str(percent_aim)+'%'
percent_init=((init-1)*100)//1
percent_init=str(percent_init)+'%'

os.system('cd {}/geo2'.format(percent_init))

POSCAR0=open('CONTCAR','r')

data=POSCAR0.readlines()
line_a=data[2]
a=line_a[4:23]
a=float(a) #a的当前数值

a_new=a/init*aim
line_a_new=line_a[:4]+str(a)+'0'+line_a[23:]
data[2]=line_a_new


os.system('mkdir ../../{}'.format(percent_aim))
os.system('mkdir ../../{}/geo1'.format(percent_aim))
if ismv:
    # os.system('cd {}/geo2'.format(percent_init))
    os.system('cp POTCAR INCAR KPOINTS vasp.lsf cellcar ../../{}/geo1'.format(percent_aim))
    print('directory {} has been created\nPOTCAR INCAR KPOINTS vasp.lsf cellcar has been moved')
os.system('cd ../../{}/geo1'.format(percent_aim))

POSCAR_new=open('POSCAR','w')
POSCAR_new.writelines(data)
POSCAR_new.close()
POSCAR0.close()
print('POSCAR about {} has been created'.format(percent_aim))

