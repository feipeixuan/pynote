
def pow(x,y,z):
    print(x+y)



def partial(func, *args, **keywords):
    """New function with partial application of the given arguments
    and keywords.
    """
    if hasattr(func, 'func'):
        args = func.args + args
        tmpkw = func.keywords.copy()
        tmpkw.update(keywords)
        keywords = tmpkw
        del tmpkw
        func = func.func

    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        # args 参数以及绑定在函数内部
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc

a=partial(pow,2,z=4)
print(a.func) #return func 时返回的是func 这个函数
print(a.args)
print(a.keywords)
a(55)
print(a.args)
print(a.keywords)
#print(dir(pow))