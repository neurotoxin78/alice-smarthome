#coding: utf8
import re
import pymorphy
import pymorphy.utils

text = u'''
Сяпала Калуша по напушке и увазила бутявку. И волит:
— Калушата, калушаточки! Бутявка!
Калушата присяпали и бутявку стрямкали. И подудонились.
А Калуша волит:
— Оее, оее! Бутявка-то некузявая!
Калушата бутявку вычучили.
Бутявка вздребезнулась, сопритюкнулась и усяпала с напушки.
А Калуша волит:
— Бутявок не трямкают. Бутявки дюбые и зюмо-зюмо некузявые. От бутявок дудонятся.
А бутявка волит за напушкой:
— Калушата подудонились! Калушата подудонились! Зюмо некузявые! Пуськи бятые!
'''

r = re.compile('[\W+-]',re.U)
words = r.split(text.upper())

# тут нужно прописать путь до папки со словарями
morph = pymorphy.get_morph('dicts/converted/ru')

for word in words:
    if word:
        print word
        info = morph.get_graminfo(word)
        for form in info:
            pymorphy.utils.pprint(form)