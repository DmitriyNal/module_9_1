def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        func_result = func(int_list)
        result[func.__name__] = func_result
    return result

if __name__ == '__main__':
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))