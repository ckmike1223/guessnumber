import random #random is a module

r = random.randint(1, 100)
count = 0 #must be written outside the while loop
while True:
	count = count + 1 # count += 1
	num = input('Please guess a number: ') #input will always be saved as a string
	num = int(num) #casting
	if num == r:
		print('you are right!!')
		print ('this is your', count, 'attempts')
		break
	elif num > r:
		print('you number is greater than the answer')
	elif num < r:
		print('you number is smaller than the answer')
	print ('this is your', count, 'attempts')