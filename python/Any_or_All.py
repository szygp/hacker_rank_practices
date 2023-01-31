复杂版
n = int(input())
m = input()
list_number = list(map(str,m.split()))
list_number_int = list(map(int,m.split()))

result2 = all(list_number[i]==list_number[i][::-1] for i in range(n))
result3 = all(list_number_int[i]> 0 for i in range(n))

if result3 and result2:
    print(True)
else:
    print(False)

简化版
m,n = input(), input().split()
print (all(int(n[i]) > 0 for i in range(int(m))) and any(j == j[::-1] for j in n))