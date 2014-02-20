__author__ = 'guardian'
result = 59
file = open('p67_triangle', 'r')
triangle = []
for row in file:
    triangle.append([])
    for item in row.strip().split(' '):
        triangle[len(triangle) - 1].append(int(item))

triangle.reverse()
for rowi in range(0, len(triangle)):
    print(triangle[rowi])
    for i in range(len(triangle[rowi]) - 1, 0, -1):
        triangle[rowi + 1][i - 1] += max(triangle[rowi][i - 1], triangle[rowi][i])