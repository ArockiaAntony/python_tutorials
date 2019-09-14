def simple_function(*args):
    '''
    This function accepts multiple arguments.
    :param msg:
    :return:
    '''
    print(f"This is sample message received from caller '{args[0]}'")


def simple_function_kw(**kwargs):
    '''
    This function accepts multiple arguments.
    :param msg:
    :return:
    '''
    print(f"This is sample message received from caller '{kwargs['msg']}'")


if __name__ == '__main__':
    simple_function("test message")
    simple_function("using named parameters")
    simple_function_kw(msg="test")