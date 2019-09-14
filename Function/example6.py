def simple_function(arg1,*args,arg2,**kwargs):
    '''
    This function accepts multiple arguments.
    :param msg:
    :return:
    '''
    print(arg1)
    print(arg2)
    print(args)
    print(kwargs)


if __name__ == '__main__':
    simple_function("test","sample","arg2",msg="testing message")