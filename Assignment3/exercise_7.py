phrase = input('Enter phrase: ')
def acronym(phrase):
    a = phrase.split()
    b = ''
    for i in a:
        if i:
            b = b + i[0].upper()
    return b
print(acronym(phrase))