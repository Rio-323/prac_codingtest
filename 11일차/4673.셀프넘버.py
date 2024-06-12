def d(n):
    result = int(n)
    while n > 0:
        result += n % 10
        n //= 10

    return result


all_num = [False] * 10001

for i in range(1, 10001):
    dn = d(i)

    if dn <= 10000:
        all_num[dn] = True

self_num = [i for i in range(1, 10001) if not all_num[i]]  # all_num[i]가 False인 값
print('\n'.join(map(str, self_num)))