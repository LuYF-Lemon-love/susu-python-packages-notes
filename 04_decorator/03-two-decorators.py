# 为函数添加一个统计运行时长的功能以及日志记录功能
import time
import threading
 
def how_much_time(func):
    print("how_much_time 外层开始")
    def inner():
        print("how_much_time 内层开始")
        t_start = time.time()
        func()
        t_end = time.time()
        print("一共花费了{0}秒时间".format(t_end - t_start))
        print("how_much_time 内层结束")
    print("how_much_time 外层结束")
    return inner
 
def mylog(func):
    print("mylog 外层开始")
    def inner():
        print("mylog 内层开始")
        func()
        print("mylog 内层结束")
    print("mylog 外层结束")
    return inner
 
@mylog
@how_much_time
def sleep_5s():
    print("sleep_5s 开始")
    time.sleep(5)
    print("%d秒结束了" % (5))
    print("sleep_5s 结束")
 
sleep_5s()