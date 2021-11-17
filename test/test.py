import time
d =[]
q = time.time()
d.append(list((2,'name2',3,q,'checkout2',299,2990)))
print(d)
s = d[0][1]
f = open(f'Omakasa/Data/customer/{s}', 'w')
for a in d[0] :
   g = f.write(str(a)+'\n')
f.close()
f= open(f'Omakasa/Data/customer/{s}', 'r')
e = f.read()
f.close()
e = e.split('\n')
e[0]=int(e[0])
e[2]=int(e[2])
e[3]=float(e[3])
e[5]=int(e[5])
r = time.localtime(e[3])

print (e)
print(r.tm_hour)