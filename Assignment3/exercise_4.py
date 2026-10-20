import random
a = random.randint(1, 10)
print('Guess number 1 - 10')
while True:
    i = int(input('Guess: '))
    if i < a:
        print('Low')
    elif i > a:
        print('High')
    else:
        print('Correct')
        break