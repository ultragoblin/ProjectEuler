__author__ = 'guardian'
result = 59
file = open('p67_triangle', 'r')
triangle = []
for row in file:
	triangle.append(row.strip().split(' '))
	print(triangle[len(triangle) - 1])




