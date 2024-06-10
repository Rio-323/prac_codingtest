import sys as s
str = s.stdin.readline().strip()

str_list = str.split('-')
result = ""

for i in str_list:
    result += i[0]

print(result)
