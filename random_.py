import random
'''
комментарий для функции
'''

def sp(a,b):
    s=[]
    for i in range(10):
        num=random.uniform(a,b)
        s.append(num)
    return s
for i in range(3):
    x=float(input(f'Введите начало {i+1} диапазона'))
    y=float(input(f'Введите конец {i+1} диапазона'))
    z=sp(x,y)
    print(z)
