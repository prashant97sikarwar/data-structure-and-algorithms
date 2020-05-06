n = int(input())
print('*',end='')
for i in range(1,(n//2)):
	print(' ',end='')
for i in range((n//2)+1):
	print('*',end='')
print()
for i in range((n//2)-1):
	print('*',end='')
	for i in range(1,(n//2)):
		print(' ',end='')
	print('*')
for i in range(n):
	print('*',end='')
print()
for i in range((n//2)-1):
	for i in range(n//2):
		print(' ',end='')
	print('*',end='')
	for i in range(1,(n//2)):
		print(' ',end='')
	print('*')
for i in range((n//2)+1):
	print('*',end='')
for i in range(1,(n//2)):
	print(' ',end='')
print('*')


