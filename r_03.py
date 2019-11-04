'''
проверить палиндромность строки
'''

def get(s):
	n = len(s)
	if n <= 1:
		return True
	else:
		return (s[0]==s[-1]) and get(s[1:-1])

s = 'радар'
print('Палиндром' if get(s) else 'Не палиндром')
