'''
найти степень m числа n => n**m
- это ускоренная версия
'''

def get(n,m):
	if m == 1:
		return n
	elif m%2 == 0:
		r = get(n, m//2)
		return r * r
	else:
		r = get(n, m//2)
		return r * r * n

print(get(2,5))
