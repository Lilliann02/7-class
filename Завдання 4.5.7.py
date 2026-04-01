print(f"{'x':^7}{'y':^7}{'z':^7}(x or not y) and z")
for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            print(f"{str(x):^7}{str(y):^7}{str(z):^7}",(x or not y) and z)