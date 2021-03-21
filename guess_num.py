import random

r = random.randint(1, 100)
while True:
	num = input('please gusee the number: ')
	num = int(num)
	if num == r:
		print('Bingo')
		break
	elif num < r:
		print('Guess biger than you guessed')	
	elif num > r:
		print('Guess smaller than you guessed')	