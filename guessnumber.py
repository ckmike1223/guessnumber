import random #random is a module

r = random.randint(1, 100)
while True:
	num = input('Please guess a number: ') #input will always be saved as a string
	num = int(num) #casting
	if num == r:
		print('you are right!!')
		break
	elif num > r:
		print('you number is greater than the answer')
	elif num < r:
		print('you number is smaller than the answer')