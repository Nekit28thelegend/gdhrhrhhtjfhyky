def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        res = func(int_list)
        results[func.__name__] = res
    return results


def min_f(args):
    min_num = min(args)
    return min_num


def max_f(args):
    max_num = max(args)
    return max_num


def len_f(args):
    len_num = len(args)
    return len_num


def sum_f(args):
    sum_num = sum(args)
    return sum_num


def sort_f(args):
    sort_list = sorted(args)
    return sort_list


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))