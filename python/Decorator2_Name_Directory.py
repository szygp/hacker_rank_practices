import operator

def person_lister(f):
    def inner(people):
        people.sort(key = lambda x: (int(operator.itemgetter(2)(x))))
        #sort里key的输入是每个元素即person 即为x, lambda是不记名函数， x是它的输入，冒号右边是它的输出，(2)(x)代表的是输入x中第3个元素
        outputs = [f(person) for person in people]
        return outputs
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')