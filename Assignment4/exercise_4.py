import re
i = input('Enter paragraph: ')
result1 = re.findall(r'\s\d{10}', i)
result2 = re.findall(r'\S84+\d{9}', i)
result = result1 + result2
result = ['[REDACTED]' for x in result]
print(result)