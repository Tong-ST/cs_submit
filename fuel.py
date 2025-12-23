while True:
    try:
        fuel = input("Fraction: ")
        x, y = fuel.split("/")
        if (int(x) > int(y)) or (int(x) < 0):
            raise ValueError()
        converted_fuel = round((int(x) / int(y)) * 100)
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        break
if converted_fuel >= 99:
    print("F")
elif converted_fuel <= 1:
    print("E")
else:
    print(f"{converted_fuel}%")