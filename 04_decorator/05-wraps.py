import time
from functools import wraps

def how_much_time(func):
    def inner(*args, **kwargs):
        t_start = time.time()
        func(*args, **kwargs)
        t_end = time.time()
        print("函数文档:", func.__doc__)
        print("一共花费了{0}秒时间".format(t_end - t_start))
    return inner
    
@how_much_time
def sleep_ns_time(n):
    """sleep_ns_time 的文档"""
    time.sleep(n)
    print("%d秒结束了" % (5,))

def mylog(func):
    @wraps(func)
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print("函数文档(wraps):", func.__doc__)
        print("日志记录(wraps)...")
    return inner

@mylog
def sleep_ns_log(n):
    """sleep_ns_log 的文档(wraps)"""
    time.sleep(n)
    print("%d秒结束了" % (5,))

sleep_ns_time(5)
print("函数文档--->", sleep_ns_time.__doc__)
print("*" * 42)
sleep_ns_log(5)
print("函数文档(wraps)--->", sleep_ns_log.__doc__)