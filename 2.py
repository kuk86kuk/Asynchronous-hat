#111. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
# проверить тип и содержание соответствующих переменных.
#Затем с помощью онлайн-конвертера преобразовать строковые представление в формат
# Unicode и также проверить тип и содержимое переменных.
words = ('разработка', 'сокет', 'декоратор')
words_u = (u'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', u'\u0441\u043e\u043a\u0435\u0442', u'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440')
for i in words:
    print(type(i), i)

for i in words_u:
    print(type(i), i)

#2. Каждое из слов «class», «function», «method» записать в байтовом
# типе без преобразования в последовательность кодов  (не используя методы
# encode и decode) и определить тип, содержимое и длину соответствующих переменных.
words_d = (b'class', b'function', b'method')
for i in words_d:
    print(type(i), i)
#3. Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе.
for s in ['attribute','класс','функция','type']:
    try:
        print(s,type(s),s.encode('ascii'), ' - encoding to bytes successful ')
    except:
        print(s,type(s),' - not valid input for bytes string')
#4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
# строкового представления в байтовое и выполнить обратное преобразование
# (используя методы encode и decode).
for s in ['разработка','администрирование','protocol','standard']:
    p=s.encode('utf-8','replace')
    q=p.decode('utf-8')
    print(s,p,q)
#5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
#  байтовового в строковый тип на кириллице.
import subprocess
for sites in ['yandex.ru','youtube.com']:
  args=['ping',sites]
  subproc_ping=subprocess.Popen(args,stdout=subprocess.PIPE)
  for line in subproc_ping.stdout:
  #    print(line)
      print(line.decode('cp866').encode('utf-8').decode('utf-8'))

#6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
# программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.\
import locale
def_co=locale.getpreferredencoding()
print(def_co)
f=open('file.txt','w')
f.writelines(['сетевое программирование\n', 'сокет\n', 'декоратор\n'])
print(f)
f.close()
#выдает <_io.TextIOWrapper name='file.txt' mode='w' encoding='cp1251'>
print(f)
#no error
with open('file.txt', encoding='cp1251') as f_n:
    for el_str in f_n:
        print(el_str)
#выдает ошибку на windows, т.к. файл в другой кодировке:
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 0: invalid continuation byte
with open('file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str)
######+