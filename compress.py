import operator
from collections import namedtuple
import prettymsg

Range = namedtuple('Range', 'left right') # need struct for stores ranges


def main():
    """For tests"""
    word = 'ABACABA'
    n = len(word)
    code, code_str, sorted_freqs, sorted_ranges, new_ranges = arithm_encode(word)
    calc = arithm_decode(n, code, sorted_ranges)

    print(prettymsg.arifm(code, sorted_freqs, sorted_ranges, new_ranges, calc))

    # top_list, code, index = bwt_encode(word)
    # solve, s = bwt_decode(code, index)
    # print(pretty_msg_bwt(top_list, code, index, solve, s))


def get_ranges(word):
    """Generate range of frequencies for arifm compress"""
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
        left_str = '{0:f} + ({1:f} - {0:f}) * {2:f}'.format(left, right, ranges[letter].left)
        right_str = '{0:f} + ({1:f} - {0:f}) * {2:f}'.format(left, right, ranges[letter].right)
        left = new_left
        right = new_right
        new_ranges.append(tuple([letter, Range(left, right), left_str, right_str]))

    code = (left + right)/2
    code_str = '({0:f} + {1:f}) / 2'.format(left, right, code)

    return code, code_str, sorted_freqs, sorted_ranges, new_ranges


def arithm_decode(n, code, ranges):
    calc = []
    calc_str = str(code)
    for i in range(n):
        for letter, rangee in ranges:
            if rangee.left <= code < rangee.right:
                calc.append(tuple([letter, calc_str]))
                new_code = (code - rangee.left) / (rangee.right - rangee.left)
                calc_str = '({0:f} - {1:f}) / ({2:f} - {1:f}) = {3:f}'.format(code, rangee.left, rangee.right, new_code)
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
