def main():
    # n = len(word)
    # freq = {i: word.count(i)/n for i in word}
    # print(freq)

    code, index = encode('FEDOR ERASTOV')
    print(code, index)
    print(decode(code, index))


def encode(word):
    top_list = [word[i:] + word[:i] for i in range(len(word))]
    top_list.sort()
    code = [i[-1] for i in top_list]
    index = top_list.index(word)
    return ''.join(code), index


def decode(code, index):
    start_list = list(code)
    cur_list = start_list
    n = len(code)
    for i in range(n - 1):
        sort_list = sorted(cur_list, reverse=False)
        cur_list = [start_list[i] + sort_list[i] for i in range(n)]
    cur_list.sort()
    return cur_list[index]

if __name__ == "__main__":
    main()
