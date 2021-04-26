import os
import sys
'''
把POSCAR的a进行比例变换
第一个参数决定变a还是b方向
第二个参数是初始比例，如1.05
第三个参数是目标比例，如1.20
第四个参数决定是否复制其他文件，1是，0否
'''

direct=(sys.argv[1])#a/b
init=float(sys.argv[2])#初始的比例
aim=float(sys.argv[3])#目标比例
ismv=int(sys.argv[4])#是否复制其他文件



percent_aim=round(((aim-1)*100)/1) #得到目标比例的百分比数字，如5%
percent_aim=str(percent_aim)+'%'
percent_init=round(((init-1)*100)/1)
percent_init=str(percent_init)+'%'
#print(percent_init,percent_aim)#

#os.system('cd {}/geo2'.format(percent_init))
#os.system('cat 123>here' << "eof")#
CONTCARlocation='./'+percent_init+'/geo2/CONTCAR'
POSCAR0=open(CONTCARlocation,'r')


data=POSCAR0.readlines()

if direct == 'a':
    line_a=data[2]
    a=line_a[4:23]
    a = float(a)  # a的当前数值
    a_new = a / init * aim
    line_a_new = line_a[:4] + str(a_new) + '0' + line_a[23:]
    data[2] = line_a_new
elif direct == 'b':
    line_b = data[3]
    b = line_b[27:48]
    b = float(b)  # b的当前数值
    a_new = b / init * aim
    line_b_new = line_b[:27] + str(a_new) + '0' + line_b[48:]
    data[3] = line_b_new


os.system('mkdir ./{}'.format(percent_aim))
os.system('mkdir ./{}/geo1'.format(percent_aim))
os.system('mkdir ./{}/geo2'.format(percent_aim))
os.system('mkdir ./{}/scf'.format(percent_aim))
print('dir geo1, geo2, scf has been made')
if ismv:
    # os.system('cd {}/geo2'.format(percent_init))
    os.system('cp ./'+percent_init+'/geo2/POTCAR ./{}/geo1'.format(percent_aim))
    os.system('cp ./'+percent_init+'/geo2/vasp.lsf ./{}/geo1'.format(percent_aim))
    os.system('cp ./'+percent_init+'/geo2/KPOINTS ./{}/geo1'.format(percent_aim))
    os.system('cp ./'+percent_init+'/geo2/cellcar ./{}/geo1'.format(percent_aim))
    os.system('cp ./'+percent_init+'/geo2/INCAR ./{}/geo1'.format(percent_aim))

    os.system('cp ./'+percent_init+'/geo2/POTCAR ./{}/geo2'.format(percent_aim))
    os.system('cp ./'+percent_init+'/geo2/vasp.lsf ./{}/geo2'.format(percent_aim))
    os.system('cp ./'+percent_init+'/geo2/KPOINTS ./{}/geo2'.format(percent_aim))
    os.system('cp ./'+percent_init+'/geo2/cellcar ./{}/geo2'.format(percent_aim))
    os.system('cp ./'+percent_init+'/geo2/INCAR ./{}/geo2'.format(percent_aim))

    os.system('cp ./'+percent_init+'/geo2/POTCAR ./{}/scf'.format(percent_aim))
    os.system('cp ./'+percent_init+'/geo2/vasp.lsf ./{}/scf'.format(percent_aim))
    os.system('cp ./'+percent_init+'/geo2/KPOINTS ./{}/scf'.format(percent_aim))
    os.system('cp ./'+percent_init+'/geo2/INCAR ./{}/scf'.format(percent_aim))

    print('directory {} has been created\nPOTCAR INCAR KPOINTS vasp.lsf cellcar has been moved to geo1, geo2, scf')
    pass
#os.system('cd ../../{}/geo1'.format(percent_aim))

POSCAR_new=open('POSCAR','w')
POSCAR_new.writelines(data)
POSCAR_new.close()
POSCAR0.close()
os.system('mv POSCAR ./'+percent_aim+'/geo1')
print('POSCAR about {} has been created'.format(percent_aim))

