# a = set(map(int, input().split()))
# all_superset = True
# for i in range(int(input())):
#     B = set(map(int, input().split()))
#     if not a.issuperset(B):
#         all_superset = False
#         break
# print(all_superset)


def all_of(inputs):
    result_all = True
    for i in inputs:
        if not i:
            result_all = False
            break
    return result_all


def any_of(inputs):
    result_any = False
    for i in inputs:
        if i:
            result_any = True
            break
    return result_any


def none_of(inputs):
    result_none = True
    for i in inputs:
        if i:
            result_none = False
            break
    return result_none


if __name__ == '__main__':
    import random

    data = random.randint(0, 1)
    print(data)

    data = list(map(bool, [random.randint(0, 1) for i in range(10)]))

    print(all_of(data))
    print(any_of(data))
    print(none_of(data))
    pass
