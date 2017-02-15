# 1. Прочитать теорию (ссылки в материалах) о работе с файлами в python. 
#И реализовать две функции: write_to_file(data) и read_file_data(). 
#Которые соотвественно: пишут данные в файл и читают данные из файла.
def write_to_file(data):
	f = open('text.txt', 'w')
	f.write(data)
	f.close()

def read_file_data(namefile):
	f = open(namefile, 'r')
	print(f.read())
print('1. _____________')
write_to_file('Hello, world!\nHello, Nikita!')
read_file_data('text.txt')

# 2. Прочитать теорию о работе с json. 
#Реализовать следующую логику: получать при помощи requests данные сайта https://jsonplaceholder.typicode.com/, 
#выводить в консоль все пары "ключ-значение", сохранять полученный json в файл.
import requests
import json
r = requests.get('https://jsonplaceholder.typicode.com/')
print('2.1. _____________')
print(r.status_code)
print(r.headers['content-type'])
print(r.headers)
print('2.1. exit elements')
for key, value in r.headers.items():
	print(key, ':', value)
print('2.2. _____________')
def write_to_file_dict(**kwargs):
	f = open('text1.txt', 'w')
	f.write(json.dumps(kwargs))
	f.close()

write_to_file_dict(**r.headers)
read_file_data('text1.txt')

# 3. Обратиться с странице https://habrahabr.ru/. 
#Получить текст страницы. 
#При помощи регулярных выражений нужно получить все ссылки со страницы на другие.
#(https?://[\w,\/,\.,\-]*)
import re
r = requests.get('https://habrahabr.ru/')

result = re.findall(r'https?://[\w,\/,\.,\-]*', str(r.content))
print('3.---------------------')
for i in result:
	print(i)






