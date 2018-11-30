"""19) Даны четыре действительных числа: x1,y1, x2, y2. 
Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). 
Считайте четыре действительных числа и выведите результат работы этой функции."""
import math

def distance(x1, y1, x2, y2):
	dist = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
	return dist



int_x1 = int(input('Input x1: '))
int_y1 = int(input('Input y1: '))
int_x2 = int(input('Input x2: '))
int_y2 = int(input('Input y2: '))


print('Distance between (x1,y1) and (x2,y2): {}'.format(distance(int_x1, int_y1, int_x2, int_y2)))