import time
t=time.time()
print (t)
t=time.localtime(t)
t = list((t.tm_year, t.tm_mon,t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec,t.tm_wday, t.tm_yday,t.tm_isdst))
t[0]=2011
print (t)
t=tuple(t)
t=time.mktime(t)
print (t)
