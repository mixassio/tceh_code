# 1. Написать декоратор, который отменяет выполнение функции и пишет: ИМЯ_ФУНКЦИИ не будет вызвана
def Decorator_no_exec(func):
    def inner(text):
        print('This func no exec:', func.__name__)  
    return inner

@Decorator_no_exec  
def shout(text):
    print(text.upper(), '!!!!')

shout('hei')

# 2. Реализовать декоратор, который измеряет скорость выполнения функций. 
#Написать три разные функции, задекорировать их и проверить
def Decorator_time_exec(func):
    def inner(a,b):
        import time
        print('timing of the function ', func.__name__)
        c = time.time()#засекаем время до начала выполнения функции
        func(a,b)
        d = time.time()#засекаем время после выполнения функции
        print('Running time: {}'.format(d-c))
    return inner

@Decorator_time_exec  
def shout(a,b):
    print((a+b).upper(), '!!!!')

@Decorator_time_exec  
def My_SQRT(a,b):
    import math
    for i in range(1,a):
        for j in range(1,b):
            d = 0
            d = math.sqrt(i) + math.sqrt(j)
    print(d)

shout('hi','ju')
My_SQRT(10000,20000)


# 3. Написать генероторное выражение, которое включает в себя все четные числа от 0 до 100
a = (i for i in range(0,101,2)) # Создаем генератор
l = [j for j in a] # Создаем список итерируясь по генератору



# 4. Написать генератор, который возвращает бесконечную последовательность случайных чисел, 
#таких что следующее не меньше прошлого
class Generate_Random(object):
    def __init__(self):
        import random
        self.before = 0
    def __iter__(self): # Добавляем "итерируемости" объекту
        return self
    def __next__(self):# Переопределяем метод некст
        import random, sys
        self.after = random.randint(0, sys.maxsize)# Используем генератор случайных чисел
        if self.before > self.after: # Проверяем что следующее число больше
            while self.before > self.after: # Если меньше, вызываем генератор ещё раз
                self.after = random.randint(0, sys.maxsize) # ряд быстро сходится к максимуму, что делать?
        self.before = self.after
        return self.after

r = Generate_Random()
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())




# 5. Написать генератор, который принимает на вход дату и на каждый вызов выдает следующий день
def Next_day(year, month, day):
    import datetime
    cur_day = datetime.date(year, month, day)
    return cur_day + datetime.timedelta(days=1)

print(Next_day(2016,12,31))















