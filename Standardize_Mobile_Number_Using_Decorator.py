def wrapper(f):
    #对f进行wrapper（包装，新函数会对旧函数就行包装，增加点东西）
    def fun(l):
        f(' '.join(['+91',x[-10:-5],x[-5:]]) for x in l)
    return fun
#@wrapper def sort_phone(l)等于如下
# def sort_phone(l):
#     pass
# sort_phone = wrapper(sort_phone)
#python看到什么先记下来，后来调用的时候再去查

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
