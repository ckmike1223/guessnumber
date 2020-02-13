import random #random is a module
start = input('Please decide your starting value: ')
end = input('Please decide your ending value: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
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