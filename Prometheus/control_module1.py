#!usr/bin/python
#-*- coding: utf-8 -*-
"""
Дешифрувати повідомлення, зашифроване шифром Бекона

Для кодування повідомлень Френсіс Бекон запропонував кожну літеру тексту замінювати на групу з п'яти символів «А» або «B» (назвемо їх "ab-групами"). Для співставлення літер і кодуючих ab-груп в даному завданні використовується ключ-ланцюжок aaaaabbbbbabbbaabbababbaaababaab, в якому порядковий номер літери відповідає порядковому номеру початку ab-групи.

Наприклад: літера "а" - перша літера алфавіту; для визначення її коду беремо 5 символів з ключа, починаючи з першого: aaaaa. Літера "c" - третя в алфавіті, отже для визначення її коду беремо 5 символів з ключа, починаючи з третього: aaabb.

Таким чином, оригінальне повідомлення перетворюється на послідовність ab-груп і може далі бути накладене на будь-який текст відповідної довжини: А позначається нижнім регістром, В - верхнім.

Наприклад, початкове повідомлення - Prometheus.

1. Кодуємо його через ab-послідовності:
p = abbab
r = babab
o = aabba
m = bbaab
e = abbbb
t = babba
h = bbbab
e = abbbb
u = abbaa
s = ababb
Результат: abbab babab aabba bbaab abbbb babba bbbab abbbb abbaa ababb

2. Підбираємо текст приблизно такої ж довжини, в якому сховаємо наше повідомлення: Welcome to the Hotel California Such a lovely place Such a lovely place

3. Для зручності розбиваємо його на групи по 5 символів і відкидаємо зайву частину (щоб при декодуванні не отримувалися зайві п'ятірки). Співставимо ab-рядок і текст-сховище для порівняння:
abbab babab aabba bbaab abbbb babba bbbab abbbb abbaa ababb
Welco metot heHot elCal iforn iaSuc halov elypl aceSu chalo vely

4. Змінюємо регістр символів, кодуючи A та B:
abbab babab aabba bbaab abbbb babba bbbab abbbb abbaa ababb
wELcO MeToT heHOt ELcaL iFORN IaSUc HALoV eLYPL aCEsu cHaLO vely

5. Повертаємо початкові пробіли на місце:
wELcOMe To The HOtEL caLiFORNIa SUcH A LoVeLY PLaCE sucH a LOvely

Для дешифрування повідомлення необхідно виконати зворотні дії.
"""
import sys
import re

a = sys.argv[1]
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
k = a.replace(" ", "")
step = 5
m = t = ""

for i in range(0, len(k), step):
	if (i + step) <= len(k):
		p = m +  " " + k[i:i+step] 
		m = p
j = re.sub(r'[a-z]', 'a', p.lstrip())
p = re.sub(r'[A-Z]', 'b', j)
n = p.replace(" ", "")

for r in range(0, len(n), step):
	d = t +  " " + alphabet[key.index(n[r:r+step])]
	t = d
print d.replace(" ", "")
