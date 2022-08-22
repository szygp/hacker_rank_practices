cube = lambda x: x ** 3


# complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers

    list_f = [0, 1]
    for i in range(2, n):
        list_f.append(list_f[i - 1] + list_f[i - 2])
        # list_f[i]=list_f[i-1]+list_f[i-2] list_f[i] can't write this list[i] don't exist
    return (list_f[0:n])


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))