#!usr/bin/python
#-*- coding: utf-8 -*-
"""
Розробити функцію find_fraction(summ),
яка приймає 1 аргумент -- невід'ємне ціле число summ,
та повертає тьюпл, що містить 2 цілих числа -- чисельник та знаменник найбільшого правильного нескорочуваного дробу,
 для якого сума чисельника та знаменника дорівнює summ. Повернути False, якщо утворити такий дріб неможливо.

Тести із некоректними даними не проводяться.
"""

def find_fraction(summ):

	half = summ / 2.0
	if summ == 0:
		return False

	if summ % 2:
		a, b = half - 0.5, half + 0.5
	else:
		if half % 2:
			a, b = half - 2, half + 2
		else:
			a, b = half -1, half + 1

	if (a > 0 and b > 0):
		return (int(a), int(b))
	else:
		return False

print find_fraction(2) # False
print find_fraction(3) # (1, 2)
print find_fraction(10) # (3, 7)
print find_fraction(62) # (29, 33)
print find_fraction(150000001) # (75000000, 75000001)
