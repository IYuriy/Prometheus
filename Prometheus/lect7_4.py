#!usr/bin/python
#-*- coding: utf-8 -*-
"""
Розробити функцію create_calendar_page(month,year), яка приймає 2 аргументи -- цілі числа -- місяць (нумерація починається з 1) і рік,
та повертає оператором return 1 рядок, який містить сторінку календаря на цей місяць.

Якщо місяць та рік не задані, використати сьогоднішні значення.
Зайві пробіли в кінці під-рядків або всього рядка, як і зайві порожні рядки недопустимі.

"""


import calendar

class LabCalendar(calendar.TextCalendar):

	def formatday(self, day, weekday, width):
		if day == 0:
			s = ''
		else:
			s = '%02i' % day
		return s.center(width)

	def formatmonth(self, year, month, w=0, l=0):
		w = max(2, w)
		l = max(1, l)
		s = '-' * 20 +'\n' * l
		s += self.formatweekheader(w).upper().rstrip()
		s += '\n' * l
		s += '-' * 20
		s += '\n' * l
		for week in self.monthdays2calendar(year, month):
			s += self.formatweek(week, w).rstrip()
			s += '\n' * l
		return s
			
def create_calendar_page(month, year):
	cal = LabCalendar()
	return cal.formatmonth(year, month)

print create_calendar_page(12, 1993)

