def simple_function(msg=None):
    '''
    Example of optional argument
    :param msg:
    :return: None
    '''
    print(f"This is sample message received from caller '{msg or 'no message'}'")

def multi_key_param(msg,sender=None):
    '''
    Example of mandatory and optional parameter
    :param msg:
    :param sender:
    :return:
    '''
    print(f"This is sample message received '{msg or 'no message'}' sender {sender or 'anonymous'}")

if __name__ == '__main__':
    simple_function("test message")
    simple_function()
    multi_key_param("test_message")
    # Below function call will throw error since we are not passing the mandatory argument
    multi_key_param()