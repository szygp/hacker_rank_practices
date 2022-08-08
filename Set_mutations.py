n_setA = int(input())
setA = set(map(int, input().split()))
N = int(input())
for i in range(N):
    command, newset = input().split()[0], set(map(int, input().split()))
    getattr(setA, command)(newset)
print(sum(setA))
