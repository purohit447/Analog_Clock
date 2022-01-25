import cv2
import numpy as np
import math
import datetime
from clockfunction import creatcir
from clockfunction import connectedLines,creathand
from clockfunction import dot
from clockfunction import line
from clockfunction import connectParallel
outer = []
hrs=[]
hrsout=[]
inner=[]
minhand=[]
hourhand=[]
arr=np.zeros((700,1200,3))
center =[350,650]
radius= 250
def clicks():
	for i in range (180,360,6):
		a=int(center[0]+(radius-20)*math.cos(i*math.pi/180))
		b=int(center[1]+(radius-20)*math.sin(i*math.pi/180))
		# print(a,b)
		a1=int(center[0]+(radius)*math.cos(i*math.pi/180))
		b1=int(center[1]+(radius)*math.sin(i*math.pi/180))
		# print(a,b)
		a2=int(center[0]+(radius-60)*math.cos(i*math.pi/180))
		b2=int(center[1]+(radius-60)*math.sin(i*math.pi/180))
		a3=int(center[0]+(radius-100)*math.cos(i*math.pi/180))
		b3=int(center[1]+(radius-100)*math.sin(i*math.pi/180))
		outer.append([a1,b1])
		inner.append([a,b])
		minhand.append([a2,b2])
		hourhand.append([a3,b3])
	for i in range (0,180,6):
		a=int(center[0]+(radius-20)*math.cos(i*math.pi/180))
		b=int(center[1]+(radius-20)*math.sin(i*math.pi/180))
		# print(a,b)
		a1=int(center[0]+(radius)*math.cos(i*math.pi/180))
		b1=int(center[1]+(radius)*math.sin(i*math.pi/180))
		# print(a,b)
		a2=int(center[0]+(radius-60)*math.cos(i*math.pi/180))
		b2=int(center[1]+(radius-60)*math.sin(i*math.pi/180))
		a3=int(center[0]+(radius-100)*math.cos(i*math.pi/180))
		b3=int(center[1]+(radius-100)*math.sin(i*math.pi/180))
		outer.append([a1,b1])
		inner.append([a,b])
		minhand.append([a2,b2])
		hourhand.append([a3,b3])
def clickshrs():
	for i in range (180,360,30):
		a=int(center[0]+(radius-60)*math.cos(i*math.pi/180))
		b=int(center[1]+(radius-60)*math.sin(i*math.pi/180))
		# print(a,b)
		a1=int(center[0]+(radius)*math.cos(i*math.pi/180))
		b1=int(center[1]+(radius)*math.sin(i*math.pi/180))
		# print(a,b)
		hrsout.append([a1,b1])
		hrs.append([a,b])
	for i in range (0,180,30):
		a=int(center[0]+(radius-60)*math.cos(i*math.pi/180))
		b=int(center[1]+(radius-60)*math.sin(i*math.pi/180))
		# print(a,b)
		a1=int(center[0]+(radius)*math.cos(i*math.pi/180))
		b1=int(center[1]+(radius)*math.sin(i*math.pi/180))
		# print(a,b)
		hrsout.append([a1,b1])
		hrs.append([a,b])

arr=creatcir(arr,350,650,250,1)
clicks()
clickshrs()
# print (outer)
# print (inner)
ou=np.array((outer))
ou=ou[::-1]
inn=np.array((inner))
inn=inn[::-1]
hr=np.array((hrs))
hr=hr[::-1]
hro=np.array((hrsout))
hro=hro[::-1]
minhand2=np.array((minhand))
minhand2=minhand2[::-1]
hourhand1=np.array((hourhand))
hourhand1=hourhand1[::-1]
arr=dot(arr,inn)
arr=dot(arr,hr)
arr=connectParallel(arr,inn,ou,4)
arr=connectParallel(arr,hr,hro,4)
while(True):
	tim=datetime.datetime.now().time()
	hrs=math.fmod(tim.hour,12)
	minute=tim.minute
	second = tim.second
	if(second==60):
		second=0;
	if hrs==12:
		hrs=0
	copy=arr.copy()
	hrs=hrs*5+int(minute/12)
	hour=int(hrs)
	# print(hrs)
	creathand(copy,center[0],center[1],inn[second][0],inn[second][1],1)
	creathand(copy,center[0],center[1],minhand2[minute-1][0],minhand2[minute-1][1],3)
	creathand(copy,center[0],center[1],hourhand1[hour][0],hourhand1[hour][1],6)
	if(cv2.waitKey(1000)==27):
		break
