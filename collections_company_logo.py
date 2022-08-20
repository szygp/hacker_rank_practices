if __name__ == '__main__':
    s = input()
    logo_dict = {}
    for letter in s:
        if letter in logo_dict:
            logo_dict[letter] += 1
        else:
            logo_dict[letter] = 1
    dict_rank = sorted(logo_dict.items(), key = lambda x: (-x[1], x[0]))
    for n, char in dict_rank[:3]:
        print(n, char)