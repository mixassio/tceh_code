# 1. Написать функцию, которая спрашивает пользователя число и степень числа, возвращает число в степени.
def my_func_2_1(a, b):
    return a ** b

# 3. Написать функцию, которая принимает список, и возвращает словарь в формате: "тип данных: количество объектов" 
#count_types([1, 4, 'd']) -> {<class 'int'>: 2, <class 'str'>: 1}
def my_func_2_3(l):
    mY_dict = {}
    my_list = []
    for i in l:
        my_list.append(type(i))
    for i in my_list:
        mY_dict.update({i:my_list.count(i)})
    return mY_dict
my_func_2_3([1,2,'fg',[1,2],[3,5,6]])

# 4. Написать функцию, которая принимает два словаря, сравнивает их ключи, выдает в консоль сколько у них общих ключей
def my_func_2_4(a, b):
    count = 0
    for k1 in a:
        for k2 in b:
            if k1 == k2:
                count += 1
    return count
a = {1: 5, 3: 'jf', 4: 'der', 5: 2, 'gy': 8}
b = {1: 'i9', 2: '90', 3: 3, 'gy': 7, 5: 'rty'}
my_func_2_4(a, b)


# 5. Написать функцию, которая принимает любое количество аргументов, 
#она вернуть список типов, принятых аргументов 
#find_types(1, 's', []) -> [<class 'int'>, <class 'str'>, <class 'list'>]
def my_func_2_5(*args):
    c = []
    for a in find_types:
        c.uppend(str(type(a)))
    return c

# 6. Написать функцию, которая принимает на вход список списков (матрицу) 
#и выводит ее в виде матрицы (один ряд на одной строке) в консоль
def my_func_2_6(*args):
    for element in args:
        print(element)

# 7. Написать функцию, которая принимает любое количество аргументов - списков, 
#она должна возвращать список из всех объектов списков, но каждый объект должен быть уникальным 
#join_lists([1, 2], ['a', 2], ['c', 1]) -> [1, 2, 'a', 'c']
def my_func_2_7(*lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result