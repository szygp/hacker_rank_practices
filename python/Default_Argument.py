def print_from_stream(n, x=None):
    if x == None:
        for i in range(0, n * 2, 2):
            print(i)
    else:
        for j in x:
            print(j)


def odd_stream(n):
    # oddstream = []
    # for i in range(1,n*2,2):
    #     oddstream.append(i)
    # return oddstream
    return [i for i in range(1, n * 2, 2)]


# 生成表达式是针对List或tuple的动态表达

n = int(input())
for i in range(n):
    category, m = input().split()
    if category == 'even':
        print_from_stream(int(m))
    else:
        print_from_stream(int(m), odd_stream(int(m)))
