'''
The software aims to be an open-source package with basic, and advanced Image Processing features.
Copyright (C) 2014	Indian Institute of Remote Sensing, Dehradun

The original authors of this program (in alphabetical order) are:

---------------------------------------------------------------------------------------------------------------------------------------
Sno.		NAME											Email( AT gmail DOT com)			Role(s)
---------------------------------------------------------------------------------------------------------------------------------------
1.				Pragun Vinayak							pragunvinayak								GUI, Contrast, Histogram
----------------------------------------------------------------------------------------------------------------------------------------

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
from osgeo import gdal
import PIL.Image as Image
import numpy as np
import math
import sys
import math
sys.path.append('./GUI/')
import imageGUI
def linearx(array):
    array1=np.array(array,'uint16')
    min=np.amin(array1)
    max=np.amax(array1)
    array1=((array1-min)*255)/(max-min)
    return array1


def log(array):
    array1=np.array(array,'uint64')
    array1=(array1+1)
    array1=np.log(array1)
    lmin=np.amin(array1)
    lmax=np.amax(array1)
    array1=((array1-lmin)*255)/(lmax-lmin)
    return array1

def exp(array):
    array1=np.array(array,'uint64')
    array1=np.exp(array1)
    lmin=np.amin(array1)
    lmax=np.amax(array1)
    array1=((array1-lmin)*255)/(lmax-lmin)
    return array1


def linearp(array1,slope,c):
    array1=np.array(array1,'uint64')    
    array1=(slope*array1)+c
    return array1

def piecewise(array):
    (x1 , x2 , x3 ,x4) = (1,2,3,4)
    array_pw=np.array(array,'uint64')    
    index=array_pw >=x1 
    index1=array_pw <= x2   
    c_index=index & index1   
    newarray=array_pw[c_index]   
    slope=(float)(y2-y1)/(x2-x1)    
    c=(float)(x2*y1-x1*y2)/(x2-x1)   
    array_op=linearp(newarray,slope,c)    
    array_pw[c_index]=array_op  
    return array_pw

def cont(fileName,num):
 

	gdal.AllRegister()

	

	dataset =gdal.Open(fileName,gdal.GA_ReadOnly)

	if dataset is None:
	    print 'Could Not Open' + fileName
	    #Alternatively Raise an Event here
	    sys.exit(1)

	cols = dataset.RasterXSize
	rows = dataset.RasterYSize
	bands = dataset.RasterCount
	rgbArray = np.zeros((rows,cols,bands),'uint8')
	print cols 
	print rows
	print bands
	dic = {1:linearx , 2 : log , 3:exp , 4:piecewise}
	dic1 = {1:'linear' , 2 : 'log' , 3:'exp' , 4:'piecewise'}
	for x in range(1,bands+1):
	    band=dataset.GetRasterBand(x)
	    array=band.ReadAsArray()	
	    rgbArray[:,:,x-1] =  dic[num](array)
	    
	combi= np.zeros((rows,cols,3),'uint8')
	count=1

	for i in range(0,bands):
	    for j in range(0,bands):
		for k in range(0,bands):
		    if( (not i == j) and (not j ==k) and (not k == i) ):
		        combi[:,:,0]=rgbArray[:,:,i]
		        combi[:,:,1]=rgbArray[:,:,j]
		        combi[:,:,2]=rgbArray[:,:,k]
		        combImage= Image.fromarray(combi)
		        combImage.save('temp/Contrast/'+dic1[num]+str(count)+'.jpeg')
			imageGUI.imdisplay('temp/Contrast/'+dic1[num]+str(count)+'.jpeg','Contrast'+str(count),1)
		        count=count+1
		        

#img = Image.fromarray(rgbArray)
#img.save('jpegTry.jpeg')
#img.show()

#I=plt.imread('liss4.tif')	
