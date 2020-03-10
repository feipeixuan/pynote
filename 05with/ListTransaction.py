
class ListTransaction:

    def __init__(self):
        print ("init")

    def __enter__(self):
        print ("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if(exc_type is not None):
            print ("kkkk")
            print (exc_val)
        else:
            print ("normal")
        print ("exit")

obj=ListTransaction()
with obj as f:
    raise Exception("exec")