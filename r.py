import random
r = random.randint(1 , 100)
while True:
	a = input('請輸入數字: ')
	a = int(a)
	if r == a:
		print('終於猜對了')
		break
	elif r > a:
		print('解答比你現在的答案大')
	elif r < a:
		print('解答比你現在的答案小')