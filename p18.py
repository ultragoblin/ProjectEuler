__author__ = 'guardian'
result = 0
file = open('p18_triangle', 'r')
triangle = []
for row in file:
    triangle.append(row.strip().split(' '))
    print(triangle[len(triangle) - 1])


def max_sum(row, column, cur_sum):
    global result
    if row == len(triangle) - 1:
        if cur_sum > result:
            result = cur_sum
        return
    summ = cur_sum + int(triangle[row + 1][column])
    max_sum(row + 1, column, summ)
    summ = cur_sum + int(triangle[row + 1][column + 1])
    max_sum(row + 1, column + 1, summ)


max_sum(0, 0, int(triangle[0][0]))
print(result)


