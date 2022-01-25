import cv2
import numpy as np
import math

def connectParallel(arr,pt1,pt2,width):
	row,col = pt1.shape
	for i in range (row):
		arr=line(arr,pt1[i][0],pt1[i][1],pt2[i][0],pt2[i][1],width)
	return arr
def creatcir(arr, a,b,r,width):
	row,col,fr= arr.shape
	for i in range(0,row):
		for j in range (0,col):
			r2=r+width;
			p1=math.pow((i-a),2)+math.pow((j-b),2)
			if p1>=(r*r) and p1<=(r2*r2):
				arr[i,j,0]=1
				arr[i,j,1]=1
				arr[i,j,2]=1
	return arr
def creatdot(arr,a,b):
	arr[a-1:a,b-1:b,0]=1
	return arr
def dot(arr,pts):
	row,col= pts.shape
	for i in range(row):
		arr=creatdot(arr,pts[i][0],pts[i][1])
	return arr
def line(arr,x1,y1,x2,y2,width):
	row,col,fr= arr.shape
	if y1-y2==0:
		arr[min(x1,x2):max(x1,x2),y1-width:y1,:]=1
	elif x1-x2==0:
		arr[x1-width:x1,min(y1,y2):max(y1,y2),:]=1
	else:
		m=(y2-y1)/(x2-x1)
		for x in range(min(x1,x2),min(x1,x2)):
			y=(m*x)+(y1-(x1*m))
			z=round(y)
			if z<col :
				arr[x-width:x,z,0]=1
				arr[x-width:x,z,1]=1
				arr[x-width:x,z,2]=1
		m=(y2-y1)/(x2-x1)
		for y in range(min(y1,y2),max(y2,y1)):
			x= y/m-y1/m+x1
			z=round(x)
			if z<row:
				arr[z,y-width:y,0]=1
				arr[z,y-width:y,1]=1
				arr[z,y-width:y,2]=1
	return arr
def creathand(arr,a,b,c,d,w):
	arr=line(arr,a,b,c,d,w) 
	cv2.imshow('clock',arr)
def hourhand(arr,hrs,mint,sec,pts,c1,c2):
	hrs=hrs*5+int(mint/12)
def connectedLines(arr,pts,con,width):
	row,col= pts.shape
	for i in range(1,row):
		arr=line(arr,pts[i][0],pts[i][1],pts[i-1][0],pts[i-1][1],width)
	if con ==True :
		arr=line(arr,pts[row-1][0],pts[row-1][1],pts[0][0],pts[0][1],width)
	return arr
