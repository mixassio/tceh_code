# 1. Написать функцию, которая выбрасывает одно из трех исключений: ValueError, TypeError или  RuntimeError случайным образом. 
# В месте вызова функции обрабатывать все три исключения
def myfunc_3_1():
    import random
    l = [7,'hjk', '8']
    a = random.choice(l)
    try:
        b = int(a)
        a = a + 'a'
        raise RuntimeError('RuntimeError')
    except ValueError:
        print('ValueError - error value')
    except TypeError:
        print('TypeError - error type')
    except RuntimeError:
        print('RuntimeError - error runtime')
myfunc_3_1()


# 2. Написать функцию, которая принимает на вход список, если в списке все объекты - int, сортирует его. Иначе выбрасывает ValueError
def myfunc_3_2(my_list):
    rez_list = []
    try:
        for i in my_list:
            i = int(i)
            rez_list.append(i)
        rez_list.sort()
        return rez_list
    except ValueError:
        print('ValueError - list in not int elements')
# tests
l = [1,2,5,7,3,4]
myfunc_3_2(l)
l = [1,2,5,7,3,4,'str']
myfunc_3_2(l)



# 3. Написать функцию, которая принимает словарь, преобразует все ключи словаря к строкам и возвращает новый словарь
def myfunc_3_3(my_dict):
    rez_dict = {}
    for key, value in my_dict.items():
        new_key = str(key)
        rez_dict.update({new_key:value})
    return rez_dict
my_dict = {1 : 4, 'd' : 'er', 2 : 'rr'}
myfunc_3_3(my_dict)

# 4. Написать функцию, которая принимает список чисел и возвращает их произведение
def myfunc_3_4(my_list):
    rez = 1
    for i in my_list:
        rez *= i
    return rez
# test
l = [1, 2, 5, 7, 3, 4]
myfunc_3_4(l)


# 5. Написать три функции: do_work, handle_success, handle_error. 
#do_word(my_list, success_callback, error_callback) принимает на вход три аргумента: 
#список, функцию для обработки успеха и функцию для обработки ошибки. 
#Ее задача проверить, что все значения в списке идут по-возрастанию. 
#Если все верно: вызываем success_callback, иначе: error_callback. 
#Функция handle_success пишет в консоль информацию об успешном выполнении. 
#Функция handle_error выбрасывает ValueError

def handle_success():
    print('Программа выполнена успешно')

def handle_error():
    try:
        raise ValueError('Ошибка в значении')
    except ValueError:
        print('ValueError - Ошибка в значении')

def do_work(my_list, success_callback, error_callback):
	prew_elem = 0
	for ind in range(len(my_list)):
		if my_list[ind] > prew_elem:
			prew_elem = my_list[ind]
			if my_list[ind] == len(my_list) - 1:
				success_callback()
		else:
			error_callback()
			break
	




     











