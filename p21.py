__author__ = 'guardian'
import math

def sum_rec(key):
	global mults_tmp
	global mults
	sum = 0
	div = 1
	keys = mults.keys()
	if key == keys[0]:
		while mults_tmp[key] != 0:
			for i in keys:
				div *= i ** mults_tmp[i]
			sum += div
			div = 1
			mults_tmp[key] -= 1
		mults_tmp[key] = mults[key]
	else:





def divisor_sum(x):
	div = 2
	n = x
	sum = 1
	global mults
	mults = {}
	global mults_tmp
	while n != 1:
		if n % div == 0:
			n /= div
			print(n)
			if div in mults.keys():
				mults[div] += 1
			else:
				mults[div] = 1
		else:
			div += 1

	mults_tmp = mults
	div = 1
	keys = mults.keys()
	sum_rec(0)

	return sum


def amicable_sum(a):
	return divisor_sum(a)


divisor_sum(3900)
result = 0
# max_number = 220
# for x in range(2,max_number+1):
# 	print('x:', x)
# 	result += amicable_sum(x)
