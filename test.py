import random
ran = random.randint(1, 100)
count = 0
while True:
	insert_ran = int(input('請輸入要猜的數字: '))
	count = count + 1
	if ran == insert_ran:
		print('你猜對了,你猜了', count,'次')
		break
	elif ran > insert_ran:
		print('你的答案要在更大一點喔')
	elif ran < insert_ran:
		print('你的答案要在更小一點喔')
