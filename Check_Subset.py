n_test_cases = int(input())
for i in range(n_test_cases):
    n_A = int(input())
    set_A =set(map(int,input().split()))
    n_B = int(input())
    set_B = set(map(int,input().split()))
    print(set_A.issubset(set_B))
