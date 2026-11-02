import re
i = input('Enter a paragraph: ')
result = re.findall(r'\d+', i)
num = [int(x) for x in result]
print(sum(num))