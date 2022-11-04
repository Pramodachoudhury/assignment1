#----------12-------------
"""t1=float(input('enter a value :'))
t2=float(input('enter a value :'))
g1=float(input('enter a value :'))
g1=float(input('enter a value :'))
import math
term=(math.sin(t1)*math.sin(t2))
term1=(math.cos(t1)*math.cos(t2)*math.cos(g1-12))
distance=6371.01*math.acos(term+term1)
print('the distance is :',distance)"""
#----------13------------------
"""f=float(input('enter a number in feet :'))
#i=float(input('enter number in inch :'))
#formula is x*12(inches)*2.54 cms
feets=f*12*2.54
#inches=i*2.54
#cm=feets+inches
print('the feets is :',feets)
#print('the inches is :',inches)
#print('the centemeter is :',cm)"""
#-----------16----------------
"""r=float(input('enter a number of radius :'))
pi=3.14
v=pi*r**2
a=3/4*pi*r**3
print('the radius of volume is :',v)
print('the radius of area is :',a)"""
#----------18-------------------
"""r=float(input('enter a radius of a cylinder :'))
h=float(input('enter a height cylinder :'))
pi=3.14
#V=πr2h
v=pi*r**2*h
print('the volume of a cylinder is :',v)"""
#---------------19-------------------
"""import math
vi=int(input('enter the speed :'))
d=int(input('enter the distance :'))
a=int(input('enter the acceleration :'))
vf=math.sqrt((vi**2)+2*(a*d))
print(vf)"""
#----------------20------------------
"""v=12
r=8.314
p=20000000
t=293.15
n=(p*v)/(r*t)
print(n)"""
#-----------21--------------------
"""b=int(input('enter the length of a triangle :'))
h=int(input('enter the height of a triangle :'))
a=(b*h)/2
print('the area of a triangle is:',a)"""
#--------------22------------
"""import math
s1=float(input('enter a 1st length of a triangle :'))
s2=float(input('enter a 2nd length of a triangle :'))
s3=float(input('enter a 3rd length of a triangle :'))
s=(s1+s2+s3)/2
a=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print(s)
print(a)"""
#--------------23--------------
"""import math
n=int(input('enter a length of a polygon :'))
s=int(input('enter a number of sides :'))
a=n*(s**2)/(4*math.tan(math.pi/n))

print(a)"""
#---------24----
"""d=int(input('enter a days :'))
h=int(input('enter a hours :'))
m=int(input('enter a minutes :'))
sec=int(input('enter a seconds :'))
s=((d*86400)+(h*3600)+(m*60)+sec)
print(s)"""
#-------------25-----------
"""sec = int(input('enter the sec :'))
day= sec // 86400
q1 = sec % 86400
hour = q1//3600
q2 = q1 % 3600
m = q2//60
q3 = q2%60
print('{}:{}:{}:{}'.format(day,hour,m,q3,sep='/n'))"""
S
