import random
q=[]
w2=[]
w1=[]
print('Введите количество элементов проверяемого списка')
a=int(input())
for i in range(a):
    q.append(random.randint(-100,100))
    if q[i]%2==0:
        w2.append(i)
    else:
        w1.append(i)
print(q)
print('*'*40)
print('Количество четных чисел - ',len(w2),'\nКоличество нечетных чисел - ',len(w1))
