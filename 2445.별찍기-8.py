import sys
a = int(sys.stdin.readline())
num = (a * 2)

for i in range(1, num):
    if i <= a:
        print('*' * i + '  ' * (a - i) + '*' * i)

    elif i > a:
        print('*' * (num - i) + '  ' * (i - a) + '*' * (num - i))

# (a - i) / (i - a) 이런식으로 해야지 숫자값이 바껴도 출력값의 형태가 변하지 않는다.