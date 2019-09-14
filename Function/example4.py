def multi_key_param(sender=None,msg):
    '''
    Example to show the order of mandatory and optional parameters.
    Error SyntaxError: non-default argument follows default argument will be throwed.
    :param msg:
    :param sender:
    :return:
    '''
    print(f"This is sample message received '{msg or 'no message'}' sender {sender or 'anonymous'}")

if __name__ == '__main__':
    multi_key_param("test_message")