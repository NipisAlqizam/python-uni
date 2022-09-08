# Разветвления I уровень
# На плоскости расположена окружность радиусом r с центром в начале координат. Ввести заданные координаты точки и определить, лежит ли она на окружности.
# Решить задачу при r=2 для точек с координатами (0;2), (1,5; 0,7), (1;1), (3;0)

eps = 10**-3

def is_on_circle(r, x, y):
	return abs(x*x+y*y-r*r) <= eps

run_default_tests = input('Запустить стандартные тесты? [Дн] ')
if len(run_default_tests) > 0 and run_default_tests[0].lower() in 'нn':
	r = float(input('r='))
	a = float(input('a='))
	b = float(input('b='))

	if is_on_circle(r, a, b):
		print(f'Точка ({a:.2};{b:.2}) лежит на окружности с радиусом {r:.2}')
	else:
		print(f'Точка ({a:.2};{b:.2}) не лежит на окружности с радиусом {r:.2}')
else:
	r = 2.
	points = [(0.,2.), (1.5, 0.7), (1.,1.), (3.,0.)]
	for point in points:
		if is_on_circle(r, point[0], point[1]):
			print(f'Точка ({point[0]:.2};{point[1]:.2}) лежит на окружности с радиусом {r:.2}')
		else:
			print(f'Точка ({point[0]:.2};{point[1]:.2}) не лежит на окружности с радиусом {r:.2}')