# 1. Написать списковые выражения, которые:
# 1.1 создают список из строк всех нечетных чисел от 1 до 100
l = [a for a in range(1,100) if a % 2 !=0]
print(l)
# 1.2 создают список из объектов другого списка, кроме итерируемых
l1 = [1,2,3,'r','ee',[1,2],(1,2), None, False]
l2 = [b for b in l1 if not hasattr(b,'__iter__')]
print(l1)
print(l2)
# 1.3 создают список из фразы 'The quick brown fox jumps over the lazy dog', 
#где каждый объект списка - кортеж из: слова в верхнем регистре, 
#слова в случанйном регистре (qUIcK) и длины слова
import random
l3 = 'The quick brown fox jumps over the lazy dog'
l4 = [(str.upper(c), ''.join([random.choice([str.upper(d),str.lower(d)]) for d in c]), len(c)) for c in l3.split(' ')]
print(l4)


