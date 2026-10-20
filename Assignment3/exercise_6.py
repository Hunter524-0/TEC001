i = (input('Enter word: '))
length = len(i)
def mid(i):
    mid = length // 2
    if length % 2 == 0:
        return i[mid - 1:mid + 1]
    else:
        return i[mid]
print(mid(i))