'''
The software aims to be an open-source package with basic, and advanced Image Processing features.
Copyright (C) 2014	Indian Institute of Remote Sensing, Dehradun

The original authors of this program (in alphabetical order) are:

---------------------------------------------------------------------------------------------------------------------------------------
Sno.		NAME											Email( AT gmail DOT com)			Role(s)
---------------------------------------------------------------------------------------------------------------------------------------
1.				Siddhant Shrivastava				sidhu94												Classification, Spatial, Polygons
----------------------------------------------------------------------------------------------------------------------------------------

    
    Compatible with Python 2.7 ( NOT COMPATIBLE with Python(>3))

	Dependencies: GDAL, NumPy, SciPy, OpenCV, Spectral Python, Tkinter, scikit-learn, scikit-fuzz

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

import numpy as np
import matplotlib.pyplot as plt
import tifwork as tw
import scipy.misc
from PIL import Image
import FastFCMeans as ffc
import FastCMeans as fc 

def fuzz(color,filename):
	#filename = 'liss4.tif'
	dataset = tw.openTIF(filename)
	cols, rows,bands,bandArray = tw.detailsTIF(dataset)
	bandArray = tw.getBand(dataset,bands,bandArray)

	intBandArray = np.array(bandArray,dtype = float)

	c = len(color)

	#print bands
	#print intBandArray.shape

	scipy.misc.imsave('hello.jpg',intBandArray)

	#(L, C, U, LUT, H) = FastFCMeans(intBandArray,c,q)
	(L,C,U,LUT,H) = ffc.FastFCMeans(intBandArray[:,:,0],c,2)

	im = intBandArray[:,:,0]

	#Visualize the fuzzy membership functions

	plt.figure('Fig 1')
	#plt.subplot(2,1,1)

	#Visualize the segmentation

	Lrgb = np.zeros((np.size(L),3),'uint8')

	Lflat = L.ravel()

	Lflat = Lflat[:,np.newaxis]



	#correct things from here

	#color = [(0,255,0),(0,0,255),(255,0,0),(0,0,0),(255,255,255),(34,65,0),(0,45,87),(100,100,100),(50,50,50),(12,54,77),(43,65,99)]

	for i in range(0,c):
		(temp,b) =np.nonzero(Lflat == i)
		Lrgb[temp] = color[i]
	
	

	#print im.shape

	Lrgb = np.reshape(Lrgb,(im.shape)+(3,))

	imArray = np.copy(Lrgb.astype('uint8'))
	print imArray.shape
	scipy.misc.imsave('1.jpg',imArray)
	plt.imshow(imArray)
	plt.show()

	#If necessary, unpack the membership functions to produce membership maps



