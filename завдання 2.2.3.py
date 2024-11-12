while True:
    a = float(input ("Введіть ширину прямокутника a = "));
    b = float(input ("Введіть довжину прямокутника b = "));
    if (a<=0 or b<=0):
        print ("Введіть правильні значення >=0");
    else:
        break;

P = (a+b)*2;

print ("P = (", a ,"+", b ,")*2 = ", P);