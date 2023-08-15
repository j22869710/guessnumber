import random
h = input('請輸入隨機數上限: ')
h = int(h)
l = input('請輸入隨機數下限:')
l = int(l)
r = random.randint(l , h)
number = 0
while True:
	number += 1
	a = input('請輸入數字: ')
	a = int(a)
	if r == a:
		print('終於猜對了')
		print('你已猜了', number, '次')
		break
	elif r > a:
		print('解答比你現在的答案大')
	elif r < a:
		print('解答比你現在的答案小')
	print('你已猜了', number, '次')