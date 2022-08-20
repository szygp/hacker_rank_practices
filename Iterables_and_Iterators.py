from itertools import combinations
a = 0
b = 0
N = int(input())
list_N = input().split()
M = int(input())

for j in combinations(list_N, M):
    a+=1
    if 'a' in j:
        b +=1
print(b/a)