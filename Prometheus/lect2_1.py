#!usr/bin/python
#-*- coding: utf-8 -*-
"""
Вхідні дані: 3 дійсних числа -- аргументи командного рядка.

Вихідні дані: результат обчислення формули
f = (1/(c * (2 * math.pi)**0.5)) * math.exp(-((a - b)**2)/(2 * (c**2)))
"""
import math
import sys 
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
f = (1/(c * (2 * math.pi)**0.5)) * math.exp(-((a - b)**2)/(2 * (c**2)))
print f
