while True:
    вік = float(input("Введіть вік (10р-100р): "))
    if вік >= 10 and вік <= 100:    break
    
while True:
    зріст  = float(input(" Введить зріст (100-250cм): "))
    if зріст >= 100 and зріст <= 250:    break
    
while True:
    статура  = int(input("Введіть значення статури (1-тонкокістна статура, 2-ширококістна):  "))
    if статура == 1 or статура == 2:    break
    
if вік<=40:
    a=зріст-110
else:
    a=зріст-100
if статура==1:
    a=a*0.9
else: 
    a=a*1.1
    
print("Ідеальна маса = ({0}-{1})*{2} = {3}".format(зріст,110 if вік<=40 else 100, 0.9 if статура==1 else 1.1, a))
