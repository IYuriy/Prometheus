#!usr/bin/python
#-*- coding: utf-8 -*-
"""
Розробити функцію bouquets(narcissus_price, tulip_price, rose_price, summ),
яка приймає 4 аргументи -- додатні дійсні числа (ціни за один нарцис, тюльпан та троянду, і суму грошей у кишені головного героя),
та повертає ціле число -- кількість варіантів букетів, які можна скласти з цих видів квітів, таких щоб вартість кожного букету не перевищувала summ.

Не забути, що букети з парною (загальною) кількістю квітів живим дівчатам не дарують. Тести із некоректними даними не проводяться.
"""
def bouquets(narcissus_price, tulip_price, rose_price, summ):

	bouquet = [narcissus_price, tulip_price, rose_price]
	bouquet.sort(None, None, True)
	a, b, c = bouquet[0], bouquet[1], bouquet[2]

	count = 0

	for i  in range(int(summ // a + 1)):
		 if a * i <= summ:
			for j in range(int((summ - a * i) // b + 1)):
				if a * i + b * j <= sum:
					for k in range(int((summ - a * i - b * j) // c + 1)):
						if (i + j + k) % 2:
							count += 1
	return count

def test(got, expected):
	if got == expected:
		prefix = ' OK'
	else:
		prefix = ' X'
	print '%s :prefix, got: %s, expected: %s' % (prefix, repr(got), repr(expected))

def main():
	test(bouquets(1,1,1,5), 34)
	test(bouquets(2,3,4,10), 12)
	test(bouquets(2,3,4,100), 4019)
	test(bouquets(200,300,400,100000), 3524556)

if __name__ == '__main__':
	main()
							

