a = []
while True:
    i = (input('Enter number or break to quit: '))
    if i == '':
        break
    i = int(i)
    a.append(i)
largest = a[0]
for x in a:
    if x > largest:
        largest = x
print(f'Largest: {largest}')
smallest = a[0]
for y in a:
    if y < smallest:
        smallest = y
print(f'Smallest: {smallest}')