#!usr/bin/python
#-*- coding: utf-8 -*-
"""
Розробити функцію convert_n_to_m(x, n, m),
яка приймає 3 аргументи -- ціле число (в системі числення з основою n) або рядок x, що представляє таке число, та цілі числа n та m (1 <= n, m <= 36),
та повертає рядок -- представлення числа х у системі числення m.

У випадку, якщо аргумент х не є числом або рядком, або не може бути представленням цілого невід'ємного числа в системі числення з основою n, повернути логічну константу False.

В системах числення з основою більше десяти для позначення розрядів із значенням більше 9 використовувати літери латинського алфавіту у верхньому регістрі від A до Z. У вхідному x можуть використовуватися обидва регістри.

"""
def convert_n_to_m(x, n, m):
	digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	number = ''

	if (type(x) in [int, long]) and (x >= 0):
		x = str(x)

	try:
		x = int(x, n)
	except:
		return False

	if x == 0:
		return 0
	if m == 1:
		return '0' * x

	while x:
		number = digits[x % m] + number
		x = x / m

	return number

def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = ' X '
	print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	test(convert_n_to_m([123], 4, 3), False)
	test(convert_n_to_m("0123", 5, 6),  '102')
	test(convert_n_to_m("123", 3, 5),  False)
	test(convert_n_to_m(123, 4, 1), '000000000000000000000000000')
	test(convert_n_to_m(-123.0, 11, 16), False)
	test(convert_n_to_m("A1Z", 36, 16), '32E7')

if __name__ == '__main__':
	main()
