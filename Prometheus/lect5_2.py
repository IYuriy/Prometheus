#!usr/bin/python
#-*- coding: utf-8 -*-
"""
Розробити функцію counter(a, b),
яка приймає 2 аргументи -- цілі невід'ємні числа a та b,
та повертає число -- кількість різних цифр числа b, які містяться у числі а.
"""

def counter(a, b):
	k = 0
	b_list = []
	a_list = []
	for i in str(b):
		b_list.append(i)
	for j in str(a):
		a_list.append(j)
	

	for num_a in set(a_list):
		for num_b in set(b_list):
			if num_a == num_b:
				k = k + 1
	return k
