import operator
from collections import namedtuple

Range = namedtuple('Range', 'left right')


def main():
    word = 'ABACABA'
    n = len(word)
    code, sorted_freqs, sorted_ranges, new_ranges = arithm_encode(word)
    calc = arithm_decode(n, code, sorted_ranges)

    print(pretty_msg_arifm(code, sorted_freqs, sorted_ranges, new_ranges, calc))

    # top_list, code, index = bwt_encode(word)
    # solve, s = bwt_decode(code, index)
    # print(pretty_msg_bwt(top_list, code, index, solve, s))


def pretty_msg_bwt(top_list, code, index, solve, s):
    msg = ['-----Кодирование-----\n\n']
    sorted_top_list = sorted(top_list, reverse=False)

    for i, j in zip(top_list, sorted_top_list):
        msg.append('{0} {1}\n'.format(i, j))

    msg.append('\nКод: ' + str(code))
    msg.append('\nИндекс: ' + str(index + 1))
    msg.append('\n\n-----Декодирование-----\n\n')
    ind = 1
    for i in solve:
        msg.append('{1}. {0}\n'.format(i, ind))
        ind += 1
    msg.append('\nСлово: ' + s)
    return ''.join(msg)


def pretty_msg_arifm(code, code_str, sorted_freqs, sorted_ranges, new_ranges, calc):
    msg = ['-----Кодирование-----\n\nЧастоты:\n']

    for letter, freq in sorted_freqs:
        msg.append('{0}: {1:f}\n'.format(letter, freq))

    msg.append('\nДиапозоны:\n')
    for letter, rangee in sorted_ranges:
        msg.append('{0}: ({1:f}; {2:f})\n'.format(letter, rangee.left, rangee.right))

    msg.append('\nОтрезки:')
    for letter, rangee, left_str, right_str in new_ranges:
        msg.append('\n{0}: ({1:f}; {2:f})\n'.format(letter, rangee.left, rangee.right))
        msg.append('Low = {0}\n'.format(left_str))
        msg.append('High = {0}\n'.format(right_str))

    msg.append('\nКод: ' + code_str + ' = ' + str(code))
    msg.append('\n\n-----Декодирование-----\n\n')
    s = ''.join(letter for letter, null in calc)
    msg.append('Слово: {0}\n'.format(s))
    msg.append('Разбор:\n')
    for letter, resh in calc:
        msg.append('{0}: код = {1}\n'.format(letter, resh))

    return ''.join(msg)


def get_ranges(word):
    n = len(word)
    freqs = {i: word.count(i) / n for i in word}
    sorted_freqs = sorted(freqs.items(), key=operator.itemgetter(1), reverse=True)
    ranges = dict()
    left = 0

    for letter, freq in sorted_freqs[:-1]:
        right = left + freq
        ranges[letter] = Range(left, right)
        left = right
    ranges[sorted_freqs[-1][0]] = Range(left, 1.0)

    return ranges, sorted_freqs


def arithm_encode(word):
    ranges, sorted_freqs = get_ranges(word)
    sorted_ranges = sorted(ranges.items(), key=operator.itemgetter(1), reverse=False)
    left = 0
    right = 1
    new_ranges = list()

    for letter in word:
        new_right = left + (right - left) * ranges[letter].right
        new_left = left + (right - left) * ranges[letter].left
        left = new_left
        right = new_right
        left_str = '{0:f} + ({1:f} - {0:f}) * {2:f}'.format(left, right, ranges[letter].right)
        right_str = '{0:f} + ({1:f} - {0:f}) * {2:f}'.format(left, right, ranges[letter].left)
        new_ranges.append(tuple([letter, Range(left, right), left_str, right_str]))

    code = (left + right)/2
    code_str = '({0:f} + {1:f}) / 2'.format(left, right, code)

    return code, code_str, sorted_freqs, sorted_ranges, new_ranges


def arithm_decode(n, code, ranges):
    calc = []
    for i in range(n):
        for letter, rangee in ranges:
            if rangee.left <= code < rangee.right:
                new_code = (code - rangee.left) / (rangee.right - rangee.left)
                calc_str = '({0:f} - {1:f}) / ({2:f} - {1:f}) = {3:f}'.format(code, rangee.left, rangee.right, new_code)
                calc.append(tuple([letter, calc_str]))
                code = new_code
                break
    return calc


def bwt_encode(word):
    top_list = [word[i:] + word[:i] for i in range(len(word))]
    sorted_top_list = sorted(top_list, reverse=False)
    code = [i[-1] for i in sorted_top_list]
    index = sorted_top_list.index(word)
    return top_list, ''.join(code), index


def bwt_decode(code, index):
    start_list = list(code)
    cur_list = start_list
    solve = [cur_list]
    n = len(code)
    for i in range(n - 1):
        sort_list = sorted(cur_list, reverse=False)
        solve.append(sort_list)
        cur_list = [start_list[i] + sort_list[i] for i in range(n)]
        solve.append(cur_list)
    cur_list.sort()
    solve.append(cur_list)
    return solve, cur_list[index]

if __name__ == "__main__":
    main()
