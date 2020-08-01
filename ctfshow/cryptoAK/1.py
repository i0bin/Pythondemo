from decimal import *


flag = 'flag{xxxxxx}'

def check(data,key):
	verify = False
	getcontext().prec = data^0x36d
	sign = str(Decimal(data) / Decimal(key))
	for d in range(1,data-2):
		if d == int(sign[d*2:(d+1)*2]):
			verify = True
		else:
			verify = False
			break
	return verify



if __name__ == '__main__':
	data = 1
	key = 1
	for data in range(1,100):
		for key in range(100,1000):
			if check(data,key):
				print(data,key)
