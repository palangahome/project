def add_one(a, b):
    return a + b + 1

#А можно эту запись заменить эквивалентным лямбда-выражением:

add_one = lambda a, b: a + b + 1


# напечатаем квадраты чисел от 1 до 5
my_list = list(map(lambda x: x**2, [1, 2, 3, 4, 5]))

print(my_list)
> [1, 4, 9, 16, 25]


# отфильтруем список с целью получить только чётные значения
my_list = list(filter(lambda x: x % 2 == 0, [11, 22, 33, 44, 55, 66]))

print(my_list)
> [22, 44, 66]



#zip()
#Упаковывает итерируемые объекты в один список кортежей. При работе ориентируется на объект меньшей длины:

word_list = ['Elf', 'Dwarf', 'Human']
digit_tuple = (3, 7, 9, 1)
ring_list = ['ring', 'ring', 'ring', 'ring', 'ring']

my_list = list(zip(word_list, digit_tuple, ring_list))

print(my_list)
> [('Elf', 3, 'ring'), ('Dwarf', 7, 'ring'), ('Human', 9, 'ring