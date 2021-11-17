import time
t1=time.time()
time.sleep(3)
t2=time.time()

t3 =t2-t1
t3 = time.localtime(t3)
print(t3.tm_sec)