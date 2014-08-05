from PIL import Image
import numpy
import pylab
#from PIL import Image
from numpy import *
import tifwork as tw
import scipy.misc


arr=array(Image.open('guiTry.jpeg'))
(row,col,z) = arr.shape
arr2 = numpy.zeros(arr.shape,int)
print arr.shape

print arr[:,:,0].min(),arr[:,:,0].mean(),arr[:,:,0].max()
print arr[:,:,1].min(),arr[:,:,1].mean(),arr[:,:,1].max()
print arr[:,:,2].min(),arr[:,:,2].mean(),arr[:,:,2].max()
# standard deviation from each band for each class will be required
# the deviation will be about the mean of the brightness value of all the bands
# 12 , 54, 67 
# mean = 44 


classes  = [[(0,17),(0,65),(0,57)], [(17,47),(0,65),(0,57)]]
print classes[0][0][1]
print arr[0,0,0] in range(classes[0][0][0],classes[0][0][1])
x = 0 
y = 0

for x in range (0,row):
	for y in range (0,col):
		if ((arr[x,y,0] in range(classes[0][0][0],classes[0][0][1])) and (arr[x,y,1] in range(classes[0][1][0],classes[0][1][1])) and(arr[x,y,2] in range(classes[0][2][0],classes[0][2][1]))):
			arr[x,y,:] = (255,0,0)
		if ((arr[x,y,0] in range(classes[1][0][0],classes[1][0][1])) and (arr[x,y,1] in range(classes[1][1][0],classes[1][1][1])) and(arr[x,y,2] in range(classes[1][2][0],classes[1][2][1]))):
			arr[x,y,:] = (0,255,0)
		else:
			arr[x,y,:] = (255,255,255)

scipy.misc.imsave('haha.jpg',arr)
'''
[12 , 13
87,   23]
[32 , 13
84,   23]
[62 , 13
87,   23]

'''

