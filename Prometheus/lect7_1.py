#!usr/bin/python
#-*- coding: utf-8 -*-
"""
Розробити класс Sphere для представлення сфери у тривимірному просторі.

Забезпечити наступні методи класу:

- конструктор, який приймає 4 дійсних числа: радіус, та 3 координати центру кулі. Якщо конструктор викликається без аргументів, створити об'єкт сфери 
  із одиничним радіусом та центром у початку координат. Якщо конструктор викликається з 1 аргументом, створити об'єкт сфери з відповідним радіусом та центром у початку координат.

- метод get_volume(), який повертає дійсне число -- об'єм кулі, обмеженої поточною сферою.
- метод get_square(), який повертає дійсне число -- площу зовнішньої поверхні сфери.
- метод get_radius(), який повертає дійсне число -- радіус сфери.
- метод get_center(), який повертає тьюпл із 3 дійсними числами -- координатами центра сфери в тому ж порядку, в яком вони задаються в конструкторі.
- метод set_radius(r), який приймає 1 аргумент -- дійсне число, та змінює радіус поточної сфери, нічого не повертаючи.
- метод set_center(x,y,z), який приймає 3 аргументи -- дійсних числа, та змінює координати центра сфери, нічого не повертаючи. Координати задаються в тому ж порядку, що і в конструкторі.
-  метод is_point_inside(x,y,z), який приймає 3 аргументи -- дійсних числа -- координати деякої точки в просторі (в тому ж порядку, що і в конструкторі), та повертає логічне значення True або False в залежності від того, чи знаходиться ця точка всередині сфери.

"""

import math

class Sphere(object):

	def __init__(self, radius = 1, x_local = 0.0, y_local = 0.0, z_local = 0.0):
		self.set_radius(radius)
		self.set_center(x_local, y_local, z_local)

	def get_volume(self):
		return 4 * math.pi * math.pow(self.radius, 3)/3
	
	def get_square(self):
		return 4 * math.pi * math.pow(self.radius, 2)
	
	def get_radius(self):
		return self.radius 
	
	def get_center(self):
		return (self.x_local, self.y_local, self.z_local)

	def set_radius(self, radius):
		self.radius = radius
	
	def set_center(self, x_local, y_local, z_local):
		self.x_local = x_local
		self.y_local = y_local
		self.z_local = z_local
	def is_point_inside(self, a, b, c):
		return math.pow(self.radius, 2) >= math.pow((self.x_local - a), 2) +  math.pow((self.y_local - b), 2) + math.pow((self.z_local - c), 2)

s0 = Sphere(0.5) # test sphere creation with radius and default center
print s0.get_center() # (0.0, 0.0, 0.0)
print s0.get_volume() # 0.523598775598
print s0.is_point_inside(0, -1.5, 0) # False
s0.set_radius(1.6)
print s0.is_point_inside(0, -1.5, 0) # True
print s0.get_radius() # 1.6
