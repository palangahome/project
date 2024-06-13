def taxi(s,b=0):
    if b>0:
        result=s*1000//140*0.25+4+b*0.1
        print(f'Стоимость поездки {result}, в тч багаж {b*0.1}')
        return result
    else:
        result=s*1000//140*0.25+4
        print(f'Стоимость поездки {result}, без багажа')
        return result
    

while True:
    s=float(input('Планируемое расстояние'))
    if s!=0:
        b=int(input('Есть ли багаж? Укажите кг'))
        taxi(s,b)
    else:
        break