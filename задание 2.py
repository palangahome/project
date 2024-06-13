import random
q=[]
print('Введите количество элементов в списке')
a=int(input())
for i in range(a):
    q.append(random.randint(-100,100))
print(q)
b=len(q)
c=0
for j in range(b):
    c=c+q[j]
print('Среднее арифметическое значение чисел равно\n',c/b)