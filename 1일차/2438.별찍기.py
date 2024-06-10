# num = int(input("숫자를 입력하세요 : "))
import sys
num = int(sys.stdin.readline()) # 백준은 입력을 이런식으로 받아야 함.

for i in range(1, num + 1): # for i in range(num + 1) 형식으로 하게되면 0 부터 시작해서 한칸이 비어있게 됨.
    print('*' * i)
