import sys as s

a = s.stdin.readline().rstrip()
b = s.stdin.readline().rstrip()
love = ''

for i in range(8):
    love += a[i]
    love += b[i]

while len(love) > 2:
    result = ''

    for i in range(len(love) - 1):
        temp = int(love[i]) + int(love[i+1])
        result += str(temp % 10)
    love = result

print(love)

# 재귀함수 버전

import sys as s

a = s.stdin.readline().rstrip()
b = s.stdin.readline().rstrip()

def create_love_string(a, b):
    love = ''
    for i in range(8):
        love += a[i]
        love += b[i]
    return love

def calculate_love(love):
    if len(love) == 2:
        return love
    else:
        result = ''
        for i in range(len(love) - 1):
            temp = int(love[i]) + int(love[i+1])
            result += str(temp % 10)
        return calculate_love(result)

love = create_love_string(a, b)
print(calculate_love(love))