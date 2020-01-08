try:
    open("abc.txt",'r')
    print(a)
except BaseException as msg:
    print(msg)