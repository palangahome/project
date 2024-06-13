import random
q=[]
print('Введите количество элементов в списке')
a=int(input())
for i in range(a):
    q.append(random.randint(-100,100))
print(q)
print('Введите проверяемое целое число')
x=int(input())
j=0
q.append(x)
while q[j]!=q[a]:
    j=j+1
if j==a:
    print('Числа нет в списке')
else:
    print('Число есть в списке')

