from math import*

def S_circle(r):
    return pi*r*r

def S_square(a):
    return a*a 

number = input(''' Введіть : \n 
1 - Якщо бажаєте знайти суму площ кругів ;  \n
2 - Якщо бажаєте знайти суму площ квадратів : \n
''' )
r1 = float(input('r1 = '))
r2 = float(input('r2 = '))
a1 = float(input('a1 = '))
a2 = float(input('a2 = '))

sum_S_circle = S_circle(r1) + S_circle(r2)
sum_S_square = S_square(a1) + S_square(a2)

if number == '1':
    print('Сумарна площа кіл:', round(sum_S_circle, 2))
else:
    print('Cумарна площа квадратів:', round(sum_S_square, 2))
    
if sum_S_circle != sum_S_square:
    print('Різниця сум площ: ', round(abs(sum_S_circle-sum_S_square),2))
else:
    print('Суми площ рівні')

