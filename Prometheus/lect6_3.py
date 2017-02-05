#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Розробити функцію saddle_point(matrix),
яка приймає 1 аргумент -- прямокутну матрицю цілих чисел, задану у вигляді списка списків,
та повертає тьюпл із координатами "сідлової точки" переданої матриці або логічну константу False, якщо такої точки не існує.

Сідловою точкою вважається такий елемент матриці, який є мінімальним (строго менше за інші) у своєму рядку та максимальним (строго більше за інші) у своєму стовпці, наприклад:
матриця:
1 2 3
0 2 1
"1" в лівому верхньому кутку (за координатами (0;0)) є сідловою точкою матриці.

Вважати, що передані дані є коректними, тобто матриця не містить інших значень крім цілих чисел, а всі вкладені списки мають однакову довжину. Результуючий тьюпл містить два числа -- порядкові номери сідлової точки в рядку (індекс його списка у зовнішньому списку) та в стовпці (індекс у внутрішньому списку).
"""

def saddle_point(matrix):	
	if len(matrix) == 1:
		return (0, 0)
	for i in range(len(matrix)):
		flag = True
		min_raw = min(matrix[i])
		if matrix[i].count(min_raw) == 1:
			k = matrix[i].index(min_raw)
			for j in range(len(matrix)):
				if min_raw <= matrix[j][k] and j != i:
					flag = False
			if flag:
				return (i, k)
	return False
def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = ' X '
	print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	test(saddle_point([[1,2,3],[3,2,1]]), False)
	test(saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]]),  (1, 2))
	test(saddle_point([[21]]),  (0, 0))

if __name__ == '__main__':
	main()
