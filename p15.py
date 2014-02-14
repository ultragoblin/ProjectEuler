__author__ = 'guardian'

import datetime

grid_size = 20
grid = []


def c_paths(x, y):
	global grid_size
	if grid[x - 1][y] == 0:
		c_paths(x - 1, y)
	if grid[x][y - 1] == 0:
		c_paths(x, y - 1)
	grid[x][y] = grid[x - 1][y] + grid[x][y - 1]


for x in range(0, grid_size + 1):
	grid.append([])
	for y in range(0, grid_size + 1):
		if x == 0 or y == 0:
			grid[x].append(1)
		else:
			grid[x].append(0)
grid[0][0] = 1
c_paths(grid_size, grid_size)

print(grid[grid_size][grid_size])