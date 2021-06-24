#https://skillsmart.ru/algo/lvl1/f70a.html
def white_walkers(s):
    # строку разбить на подстроки по цифрам в начале и в конце
    # оставить список подстрок с суммой цифр = 10
    # во всех подстроках должно быть ровно три символа =
    list_numbers = string_split_numbers(s)
    list_10 = list_sum_start_end_equal(list_numbers, 10)
    in_each = list_in_each_count(list_10, "=", 3)
    return in_each

    # functional style
    # return list_in_each_count(
    #     list_sum_start_end_equal(
    #         string_split_numbers(s), 10), "=", 3)


def list_in_each_count(l1d, sym, cnt):

    # в каждом элементе списка sym встречается cnt раз

    if len(l1d):
        bingo = True
    else:
        bingo = False

    for i in l1d:
        if i.count(sym) != cnt:
            bingo = False
            break

    return bingo


def string_split_numbers(s):
    # разбить строку по подстрокам -
    # должны начинаться и заканчиваться цифрой
    # https://drakonhub.com/ide/doc/forall/133

    l1d_ = []
    left = 0

    for i in range(len(s)):
        if s[i].isdigit():
            if left:
                subs = s[left:i + 1]
                l1d_.append(subs)
            left = i

    return l1d_


def list_sum_start_end_equal(l1d_in_, dig_sum):
    # вернуть список строк, начало и конец цифра,
    # сумма цифр == dig_sum

    l1d_ret = []

    for l in l1d_in_:
        if l[0].isdigit() and l[-1].isdigit():
            if (int(l[0]) + int(l[-1])) == dig_sum:
                l1d_ret.append(l)

    return l1d_ret
