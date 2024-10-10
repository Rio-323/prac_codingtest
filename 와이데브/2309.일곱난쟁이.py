import itertools

arr = [int(input()) for _ in range(9)]
result = next(sorted(c) for c in itertools.combinations(arr, 7) if sum(c) == 100)
# next 함수가 하나씩 조합을 확인할 수 있게 도와줌

print("\n".join(map(str,result)))

# def combinations(arr, r):
#     result = []
    
#     def backtrack(start, path):
#         if len(path) == r:
#             result.append(path)
#             return
#         for i in range(start, len(arr)):
#             backtrack(i + 1, path + [arr[i]])
    
#     backtrack(0, [])
#     return result

# arr = [int(input()) for _ in range(9)]

# # 직접 구현한 combinations 함수로 7개 조합을 구함
# for combination in combinations(arr, 7):
#     if sum(combination) == 100:
#         result = sorted(combination)
#         break

# print("\n".join(map(str, result)))