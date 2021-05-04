a='  0.1846304986686029  0.1510873441856226  0.9403188312619921'

b=a.lstrip().split('  ')

numbers = list(map(float, b))
print(type(numbers[1]))
# print(b)

c=[[1,2],5,3,2,4]
# d=c.pop()
e=c.reverse()
print(e,c)