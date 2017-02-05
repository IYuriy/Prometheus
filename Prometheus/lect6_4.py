#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
Розробити функцію find_most_frequent(text),
яка приймає 1 аргумент -- текст довільної довжини, який може містити літери латинського алфавіту, пробіли та розділові знаки (,.:;!?-);
та повертає список слів (у нижньому регістрі), які зустрічаються в тексті найчастіше.

Слова, записані через дефіс, вважати двома словами (наприклад, "hand-made"). Слова у різних відмінках, числах та з іншими перетвореннями (наприклад, "page" та "pages") вважаються різними словами. Регістр слів -- навпаки, не має значення: слова "page" та "Page" вважаються 1 словом.

Якщо слів, які зустрічаються найчастіше, декілька -- вивести їх в алфавітному порядку.
"""
import re

def find_most_frequent(text):
	dict_find = {}
	list_find = []
	text = re.sub('[%s]' % ',.:;!?-', ' ', text.lower()).split()

	for word in text:
		dict_find.setdefault(word, 0)
		dict_find[word] += 1

	if len(dict_find) == 0:
		return []
	max_id = max(value for key, value in dict_find.items())

	for word, count in dict_find.items():
		if count == max_id:
			list_find.append(word)
	return list_find

def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = ' X '
	print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	test(find_most_frequent('Hello,Hello, my dear!'), ['hello'])
	test(find_most_frequent('to understand recursion you need first to understand recursion...'),  ['recursion', 'to', 'understand'])
	test(find_most_frequent('Mom! Mom! Are you sleeping?!!!'), ['mom'])
if __name__ == '__main__':
	main()	
