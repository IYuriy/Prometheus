#!usr/bin/python
#-*- coding: utf-8 -*-
"""
Розробити функцію count_holes(n),
яка приймає 1 аргумент -- ціле число або рядок, який містить ціле число,
та повертає ціле число -- кількість "отворів" у десятковому записі цього числа друкованими цифрами (вважати, що у "4" та у "0" по одному отвору), або рядок ERROR, якщо переданий аргумент не задовольняє вимогам: є дійсним або взагалі не числом.
"""
def count_holes(n):
	dict_num = {'-': 0, '0': 1, '1': 0, '2': 0, '3': 0, '4': 1, '5': 0, '6': 1, '7': 0, '8': 2, '9': 1}
	str_num = '-0123456789'
	counter = 0
	if len(str(n)) != 0:
		for k in str(n):
			if k not in str_num:
				return 'ERROR'	
		a = str(int(n))
		for i in a:
			counter = counter + dict_num[i]
	else: 
		return 'ERROR'
	if type(n) == float:
		return 'ERROR'
	return counter
