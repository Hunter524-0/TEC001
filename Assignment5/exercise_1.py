i = []
while True:
    a = input('Enter numbers: ')
    if a == '':
        break
    a = int(a)
    i.append(a)
i.sort(reverse=True)
print(i[0:5])