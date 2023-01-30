from itertools import product

K, M = input().split()
M = int(M)
my_list = []

for i in range(int(K)):
    x = list(map(int, input().split()))
    from itertools import product

    K, M = input().split()
    M = int(M)
    my_list = []

    for i in range(int(K)):
        x = list(map(int, input().split()))
        my_list.append(x[1:])

    list_product = list(product(*my_list))

    max_number = 0
    for j in list_product:
        number = sum([pow(i, 2) for i in j])
        max_number = max(max_number, number % M)

    print(max_number)

list_product = list(product(*my_list))

max_number = 0
for j in list_product:
    number = sum([pow(i, 2) for i in j])
    max_number = max(max_number, number % M)

print(max_number)