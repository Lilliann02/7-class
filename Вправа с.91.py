def max (x, y) :
    if x > y : 
        return x
    else: 
        return y


x1 = float(input("x1="))
x2 = float(input("x2="))
x3 = float(input("x3="))
x4 = float(input("x4="))

m = max(max(x1,x2),max(x3,x4))

print("Найбільше значення з чисел {0}, {1}, {2}, {3} --> {4}".format(x1,x2,x3,x4,m))