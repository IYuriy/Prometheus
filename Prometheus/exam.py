def print_maze(maze, x, y):
	for i in range(len(maze)):
		s = ''
		for j in range(len(maze)):
			if i == x and j == y:
				s += 'X'
			elif maze[i][j] == 1:
				s += '#'
			else:
				s += '.'
		print s
	print ' '

class MazeRunner(object):
    
	def __init__(self, maze, start, finish):
		self.__maze = maze
		self.__rotation = (1,0)
		self.__x = start[0]
		self.__y = start[1]
		self.__finish = finish

	def go(self):
		x = self.__x + self.__rotation[0]
		y = self.__y + self.__rotation[1]

		if x > len(self.__maze)-1 \
			or y > len(self.__maze)-1 \
			or x < 0 or y < 0 \
			or self.__maze[x][y] == 1:
			return False
		self.__x = x
		self.__y = y
		print_maze(self.__maze, self.__x, self.__y)
		return True
    
	def turn_right(self):
		left_rotation = {
			(0,1) : (1,0),
			(1,0) : (0,-1),
			(0,-1) : (-1,0),
			(-1,0) : (0,1),
		}
		self.__rotation = left_rotation[self.__rotation]
		return self
    
	def turn_left(self):
		right_rotation = {
			(1,0) : (0,1),
			(0,-1) : (1,0),
			(-1,0) : (0,-1),
			(0,1) : (-1,0),
		}
		self.__rotation = right_rotation[self.__rotation]
		return self
    
	def found(self):
		return self.__x == self.__finish[0] and self.__y == self.__finish[1]


def maze_controller(self):
	import random
	counter = 0
	while not self.found() and counter < 100000:
		self.go()
		counter += 1
		x = random.choice([0, 1])
		if x == 0:
			self.turn_right()
		else:
			self.turn_left()


maze_example1 = {
    'm': [
        [0,1,0,0,0],
        [0,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,0],
        [0,0,0,1,0],
    ],
    's': (0,0),
    'f': (4,4)
}
maze_runner = MazeRunner(maze_example1['m'], maze_example1['s'], maze_example1['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 1'

maze_example2 = {
    'm': [
        [0,0,0,0,0,0,0,1],
        [0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0],
        [1,1,1,1,0,1,0,1],
        [0,0,0,0,0,1,0,1],
        [0,1,0,1,1,1,1,1],
        [1,1,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,0],
    ],
    's': (7,7),
    'f': (0,0)
}
maze_runner = MazeRunner(maze_example2['m'], maze_example2['s'], maze_example2['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 2'

maze_example3 = {
    'm': [
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
    ],
    's': (0,5),
    'f': (10,5)
}
maze_runner = MazeRunner(maze_example3['m'], maze_example3['s'], maze_example3['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 3'

maze_example4 = {
    'm': [
        [0,0,0,0,1,0,1,0,0,0,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [1,1,0,1,0,0,0,1,0,1,1],
        [0,1,0,1,0,1,0,1,0,1,0],
        [0,1,0,0,0,1,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
    ],
    's': (0,5),
    'f': (4,5)
}
maze_runner = MazeRunner(maze_example4['m'], maze_example4['s'], maze_example4['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 4'

maze_example6 = {
    'm': [
        [1,0,1,0,1],
        [1,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,1],
        [1,0,1,0,1],
    ],
    's': (2,0),
    'f': (2,4)
}
maze_runner = MazeRunner(maze_example6['m'], maze_example6['s'], maze_example6['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 6'

maze_example7 = {
    'm': [
        [0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,1,0],
        [0,1,0,0,1,0,1,0],
        [0,1,1,1,1,0,1,0],
        [0,0,0,0,0,0,1,0],
        [1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0],
    ],
    's': (3, 2),
    'f': (7, 0)
}
maze_runner = MazeRunner(maze_example7['m'], maze_example7['s'], maze_example7['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 7'

maze_example8 = {
    'm': [
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
    ],
    's': (0,1),
    'f': (0,3)
}
maze_runner = MazeRunner(maze_example8['m'], maze_example8['s'], maze_example8['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 8'

maze_example10 = {
    'm': [
        [1,0,0,0,1,0,0,1],
        [1,0,1,0,1,1,0,1],
        [1,0,1,0,0,0,0,1],
        [1,1,1,1,1,0,1,1],
        [1,0,0,0,0,0,0,1],
        [1,1,1,0,1,1,1,1],
        [1,0,0,0,0,0,0,0],
        [1,0,1,0,1,0,1,0],
    ],
    's': (0, 3),
    'f': (7, 5)
}
maze_runner = MazeRunner(maze_example10['m'], maze_example10['s'], maze_example10['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 10'

maze_example5 = {
    'm': [
        [0,0,0,1,1,0,1,1,0,0,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,1,1,0,0,0,1,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,1,1,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
    ],
    's': (0,5),
    'f': (4,5)
}
maze_runner = MazeRunner(maze_example5['m'], maze_example5['s'], maze_example5['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 5'

maze_example9 = {
    'm': [
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,0,1,1,1,1,1,1,0],
        [0,1,0,0,1,0,1,0,1,0,0],
        [0,1,0,1,1,0,1,0,1,1,1],
        [0,1,0,0,1,0,1,0,0,0,0],
        [0,1,1,0,1,0,1,0,1,1,0],
        [0,1,0,0,1,0,1,0,1,0,0],
        [0,1,0,1,1,0,1,0,1,0,1],
        [0,1,0,0,1,0,1,0,1,0,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
    ],
    's': (0, 5),
    'f': (2, 5)
}
maze_runner = MazeRunner(maze_example9['m'], maze_example9['s'], maze_example9['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 9'

maze_example11 = {
    'm': [
        [0,0,0,1,0,0,0,0,0,0,0],
        [0,1,0,1,0,1,1,1,1,1,0],
        [0,1,0,1,0,1,0,0,0,1,0],
        [0,1,0,0,0,1,0,1,1,1,0],
        [0,1,1,1,1,1,0,1,0,0,0],
        [0,1,0,0,1,1,0,1,1,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,1,1,1,0,1,0],
        [0,0,0,1,0,0,0,1,0,1,0],
        [0,0,0,1,0,1,0,1,0,1,0],
        [0,0,0,0,0,1,0,0,0,0,0],
    ],
    's': (4, 8),
    'f': (9, 1)
}
maze_runner = MazeRunner(maze_example11['m'], maze_example11['s'], maze_example11['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 11'

maze_example12 = {
    'm': [
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,1,0,1,0,0,0,1,0,1,0],
        [0,1,0,1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1,0,1,0],
        [0,1,0,1,1,1,0,1,0,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
    ],
    's': (6, 4),
    'f': (10, 5)
}
maze_runner = MazeRunner(maze_example12['m'], maze_example12['s'], maze_example12['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 12'

maze_example13 = {
    'm': [
        [0,1,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,1,1,1],
        [0,1,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,1,0,0,0,0,0,1,0,1,0],
        [0,1,1,1,1,1,0,1,0,1,0],
        [0,0,0,0,0,0,0,1,0,1,0],
        [0,1,0,1,1,1,0,1,0,1,0],
        [0,1,0,0,0,0,0,1,0,1,0],
        [0,1,1,1,1,1,1,1,0,1,0],
        [0,0,0,0,0,0,0,0,0,1,0],
    ],
    's': (10, 5),
    'f': (6, 4)
}
maze_runner = MazeRunner(maze_example13['m'], maze_example13['s'], maze_example13['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 13'

maze_example14 = {
    'm': [
        [1,0,1,1,1,0,1,1,1,0,1],
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,0,0,1,1,1,0,0,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1,1,1,0,1],
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
    ],
    's': (10, 1),
    'f': (7, 7)
}
maze_runner = MazeRunner(maze_example14['m'], maze_example14['s'], maze_example14['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 14'

maze_example15 = {
    'm': [
        [0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,1,0,1,0,1,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0],
        [0,1,0,0,0,1,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,0,1,0,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,1,0,0,0,1,0],
        [0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,1,0,1,0,1,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0],
    ],
    's': (1, 1),
    'f': (9, 9)
}
maze_runner = MazeRunner(maze_example15['m'], maze_example15['s'], maze_example15['f'])
maze_controller(maze_runner)
print maze_runner.found(), 'Var 15'
