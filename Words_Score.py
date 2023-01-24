def score_words(word):
    # k=0
    # for i in word:
    #     if i in ['a','e','i','o','u','y']:
    #         k+=1

    # if k%2 == 0:
    #     return 2
    # else:
    #     return 1

    return 2 if sum([1 if i in ['a', 'e', 'i', 'o', 'u', 'y'] else 0 for i in word]) % 2 == 0 else 1


def total_score(n, words):
    # s=0
    # for j in range(n):
    #     s += score_words(words[j])
    # return s
    return sum([score_words(j) for j in words])


n = int(input())
words = input().split()
print(total_score(n, words))