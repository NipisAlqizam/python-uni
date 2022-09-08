# циклы I уровень
# Составить таблицу значений функции y = (1, x<=-1; -x, -1<x<=1; -1, x>1) на отрезке -1,5<=x<=1,5 с шагом h=0,1
h = 0.1 
left = -1.5
right = 1.5
count = int((right-left)/h)

print('Таблица значений функции y = (1, x<=-1; -x, -1<x<=1; -1, x>1) на отрезке -1,5<=x<=1,5 с шагом h=0,1:')
print('x'+' '*7+'y')

for i in range(count):
	x = left+i*h
	if x <= -1:
		print(f'{x:> .1f}   -1')
	elif x <= 1:
		print(f'{x:> .1f} {x:> .1f}')
	else:
		print(f'{x:> .1f}    1')
