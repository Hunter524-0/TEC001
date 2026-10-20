while True:
    i = float(input('Enter inches: '))
    cm = i * 2.54
    if i < 0:
        break
    print(f'{cm:.2f} cm')