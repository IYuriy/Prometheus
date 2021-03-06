#!usr/bin/python
#-*- coding: utf-8 -*-
"""
Розробити функцію file_search(folder, filename),
яка приймає 2 аргументи -- список folder та рядок filename,
та повертає рядок -- повний шлях до файлу або папки filename в структурі folder.

Файлова структура folder задається наступним чином:

Список -- це папка з файлами, його 0-й елемент містить назву папки, а всі інші можуть представляти або файли в цій папці (1 файл = 1 рядок-елемент списку), або вкладені папки, які так само представляються списками. Як і в файловій системі вашого комп'ютера, шлях до файлу складається з імен всіх папок, в яких він міститься, в порядку вкладеності (починаючи з зовнішньої і до папки, в якій безпосередньо знаходиться файл), розділених "/".

Вважати, що імена всіх файлів є унікальними. Повернути логічне значення False, якщо файл не знайдено.
"""
def file_search(folder, filename):
	path = False	
	if filename in folder:
		path = folder[0] + '/' + filename
	else:
		for sub_folder in folder:
			if type(sub_folder) is list:
				sub = file_search(sub_folder, filename)
				if sub:
					path = folder[0] + '/' + sub
	return path
