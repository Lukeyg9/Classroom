x = 1

while x <= 100:
    square = x ** 2
    if square > 2000:
        break
    print(f"{x} = {square}")
    x += 1
