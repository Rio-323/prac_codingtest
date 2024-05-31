import sys
a = sys.stdin.readline()

for i in range(int(a)):
    b, c = map(str, sys.stdin.readline().split())
    b = int(b)
    for i in c:
        print(i * b, end="")
    print()

# 이 문제는 입력에 관해서 헷갈려서 오래걸린 문제.. 코딩테스트 입력값 생각하는게 가장 어려운 듯
# 2
# 3 ABC
# 5 /HTP 입력 값이 이런 식으로 주어졌는데
# 저 2는 ABC와 HTP 이렇게 2번 입력하기 위해 입력한 것 나는 처음에 그냥 문자열을 넣어주지 않은 것으로 알았다.



