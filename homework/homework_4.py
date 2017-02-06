"""Реализовать класс Person, у которого должно быть два публичных поля: age и name. 
Также у него должен быть следующий набор методов: know(person), который позволяет добавить другого человека в список знакомых. 
И метод is_known(person), который возвращает знает ли знакомы ли два человека"""
class Person:
	pers_known = ()
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def know(self, person):
		if person.name in self.pers_known:
			print('{} and {} have friendly'.format(self.name, person.name))
		else:
			self.pers_known = self.pers_known + (person.name,)
	def is_known(self, person):
		if person.name in self.pers_known:
			return True
		else:
			return False

A = Person('Alice', 22)
B = Person('Bill', 25)
C = Person('Chedd', 30)
A.know(B)
A.know(C)
A.know(B)
B.know(A)
B.know(C)
print(A.is_known(B))
print(C.is_known(B))
print(A.pers_known)
print(B.pers_known)
print(C.pers_known)



"""Есть класс, который выводи информацию в консоль: `Printer`, у него есть метод: log(*values). 
Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *"""

class Printer:
	def log(self, *args):
		for i in args:
			print(i, end=' ')
	def FormattedPrinter(self, *args):
		print('*'*100)
		for j in args:
			self.log(j)
		print('\n')
		print('*'*100)
a = Printer()
a.FormattedPrinter(1,2,3,4,'dfg')


"""Написать класс Animal и Human, сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые). 
Другие - нет. За что будет отвечать метод is_dangerous(animal)"""

class Human:
	def __init__(self, cityzen, natio, age):
		self.cityzen = cityzen
		self.natio = natio
		self.age = age


class Animal:
	def __init__(self, danger):
		self.danger = danger
	def is_dangerous(self):
		if self.danger == True:
			print('Be careffulle, animal is dangerous')
		else:
			print('It"s all right!')
fish = Animal(False)
Lion = Animal(True)
fish.is_dangerous()
Lion.is_dangerous()
































