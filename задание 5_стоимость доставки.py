def express_dostavka(a):
    
    if a==1:
        cost=10.95
        print('Сумма доставки равна:')
    elif a>1:
        cost=round(10.95+(a-1)*2.95,2)
        print('Сумма доставки равна:')
    elif a<1:
        print('Товар отсутствует в корзине')
        cost=0
    return cost

print('Количество позиций в заказе:')
x=int(input())
y=express_dostavka(x)
print(y)