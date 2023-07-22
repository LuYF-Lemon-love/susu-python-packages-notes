import time

def how_much_time(func):
    def inner(*args, **kwargs):
        t_start = time.time()
        func(*args, **kwargs)
        t_end = time.time()
        print("一共花费了{0}秒时间".format(t_end - t_start, ))
    return inner
    
@how_much_time
def sleep_ns(n):
    time.sleep(n)
    print("%d秒结束了" % (5,))

def mylog(type):
    def decorator(func):
        def inner(*args, **kwargs):
            if type == "文件":
                print("文件中: 日志记录")
            else:
                print("控制台: 日志记录")
            func(*args, **kwargs)
        return inner
    return decorator

@mylog("文件")
def func(a, b):
    print("func: ", a, b)

sleep_ns(5)
print("*" * 42)
func(100, 200)