a = float(input("Введіть масу цукерок    "))
x = float(input("Введіть ціну 1кг цукерок    "))
b = int(input("Введіть кількість пляшок лимонаду    "))
y = float(input("Введіть ціну 1 пляшки лимонаду    "))

c = a*x + b*y

print ("Вартість покупки: ", int(round(c,2)), "грн", int(round((round(c,2)-int(round(c,2)))*100,0)),"коп")