# 为函数添加一个统计运行时长的功能
import time
import threading
 
def how_much_time(func):
    def inner():
        t_start = time.time()
        func()
        t_end = time.time()
        print("一共花费了{0}秒时间".format(t_end - t_start))
    return inner
 
def sleep_5s():
    time.sleep(5)
    print("%d秒结束了" % (5))
 
def sleep_6s():
    time.sleep(6)
    print("%d秒结束了" % (6))
 
sleep_5s = how_much_time(sleep_5s)
sleep_6s = how_much_time(sleep_6s)
 
t1 = threading.Thread(target=sleep_5s)
t2 = threading.Thread(target=sleep_6s)
t1.start()
t2.start()