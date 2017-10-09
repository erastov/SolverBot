def bwt(top_list, code, index, solve, s):
    """Create pretty message for output bwt compress"""
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


def arifm(code, code_str, sorted_freqs, sorted_ranges, new_ranges, calc):
    """Create pretty message for output arifm compress"""
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