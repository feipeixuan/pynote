



def logger_say(func):
    def proxy(*args):
        func(args[0],args[1])
        print(args)

    return proxy

@logger_say
def say_hello(name,content):
    print(content)

say_hello("fei",1)