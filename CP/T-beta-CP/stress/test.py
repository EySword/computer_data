POSCAR0=open('POSCAR','r')
'''
指定a的梯度生成新POSCAR
'''

data=POSCAR0.readlines()
# print(a)
line_a=data[3]
a=line_a[27:48]
print(type(a))
a=float(a)
print(a)