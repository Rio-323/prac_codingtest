def fibonaci(n):
    numbers = []

    for i in range(n + 1):
        if i < 2:
            numbers.append(i)
        else:
            numbers.append(numbers[i - 2] + numbers[i - 1])

    return numbers[-1]

n = int(input())

print(fibonaci(n))


# 간결 버전
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

# n = int(input())
# print(fibonacci(n))
