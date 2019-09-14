def simple_function(msg):
    '''
    This function accepts one argument
    :param msg:
    :return:
    '''
    print(f"This is sample message received from caller '{msg}'")

if __name__ == '__main__':
    simple_function("test message")
    simple_function(msg="using named parameters")