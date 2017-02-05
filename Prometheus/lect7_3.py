#!usr/bin/python
#-*- coding: utf-8 -*-
"""
Розробити класс SuperStr, який наслідує функціональність стандартного типу str і містить 2 нових методи:

    метод is_repeatance(s), який приймає 1 аргумент s та повертає True або False в залежності від того, чи може бути поточний рядок бути отриманий цілою кількістю повторів рядка s. Повернути False, якщо s не є рядком. Вважати, що порожній рядок не містить повторів.
    
	метод is_palindrom(), який повертає True або False в залежності від того, чи є рядок паліндромом. Регістрами символів нехтувати. Порожній рядок вважати паліндромом.

"""
class SuperStr(str):

	def is_repeatance(self, s):
		if type(s) is not str or s == '' or self == '':
			return False
		return self.replace(s, '') == ''
	
	def is_palindrom(self):
		return self.lower() == self.lower()[::-1]		
	
s = SuperStr('123123123123')
print s.is_repeatance('123') # True
print s.is_repeatance('123123') # True
print s.is_repeatance('123123123123') # True
print s.is_repeatance('12312') # False
print s.is_repeatance(123) # False
print s.is_palindrom() # False
print s # 123123123123 (рядок)
print int(s) # 123123123123 (ціле число)
print s + 'qwe' # 123123123123qwe
p = SuperStr('123_321')
print p.is_palindrom() # True
