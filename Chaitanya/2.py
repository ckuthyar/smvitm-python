count = 0
limit = 20

for a in range(1, 100):
    for b in range(a, 100):
        c = (a**2 + b**2)**0.5
        if c.is_integer():
            print(f"{a}, {b}, {int(c)}")
            count += 1
            if count == limit:
                break
    if count == limit:
        break
