__author__ = 'guardian'

start = 1000000
n = 0
count = 0
result = 0
db = {}

for start in range(1, 1000000):
	n = start
	i = 0

	while n != 1:
		if n in db.keys():
			i += db[n]
			break
		if n % 2 == 0:
			n /= 2
		else:
			n = 3 * n + 1
		i += 1

	if count < i:
		count = i
		result = start
	db[start] = i

print(count, result)