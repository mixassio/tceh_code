import random
A = [['Какой язык мы изучаем?','Python'],
     ['Как называется язык запросов к БД?','SQL'],
     ['Уж не в амперах ли измеряется сила тока?','В амперах'],
     ['Между кем и кем была русско-японская война?','Между Россией и Японией'],
     ['Какой сейчас год?','2017'],
     ['Сколько девушек в нашей группе?','Не считал'],
     ['Как называется команда подсчета длины строки?','len'],
     ['Что светит на небе ночью?','Луна'],
     ['В какой стране мы живём?','Россия'],
     ['Ноутбук какой фирмы использует наш преподаватель?','apple']]
print(random.randint(0,9))
inp = ''
a = 0
b = 0
print('Поиграем в загадки? Для выхода из программы напишите в ответе EXIT.')
while str.upper(inp) != 'EXIT':
	i = random.randint(0,9)
	inp = str(input(A[i][0]))
	if str.upper(inp) == str.upper(A[i][1]):
		a += 1
		print('Правильно!')
	else:
		b += 1
		print('Неправильно!')
print('Спасибо, что уделили время! Правильных ответов {}, неправильных ответов {}'.format(a, b))




