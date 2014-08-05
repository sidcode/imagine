'''
The software aims to be an open-source package with basic, and advanced Image Processing features.
Copyright (C) 2014	Indian Institute of Remote Sensing, Dehradun

The original authors of this program (in alphabetical order) are:

---------------------------------------------------------------------------------------------------------------------------------------
Sno.		NAME											Email( AT gmail DOT com)			Role(s)
---------------------------------------------------------------------------------------------------------------------------------------
1.				Pragun Vinayak							pragunvinayak								GUI, Contrast, Histogram
2.				Abhishek Kumar Roushan		abhishek.roushan12						Histogram, Contrast
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
from PIL import Image
from pylab import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random
import matplotlib.cm as cm
import cv2

from PIL import Image
from pylab import *
from Tkinter import *
import Tkinter as tk
from tkMessageBox import *
import ttk
import tkFileDialog
from PIL import Image
import tifwork
import sys
import matplotlib
import math
from osgeo import gdal
#import piecewise

matplotlib.use('TkAgg')
#global fx,ax
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.figure import Figure
import pylab
#import Image, ImageTk
#import tktable
import tifwork
import matplotlib.gridspec as gridspec




fileName=tkFileDialog.askopenfilename(filetypes=[('TIF','*.tif')])
if(fileName == ''):
	pass
else:
	print(fileName)
	dataset=(tifwork.openTIF(fileName))


def histeq(im,nbr_bins=256):

# get image histogram
	imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
	cdf = imhist.cumsum() # cumulative distribution function
	cdf = 255 * cdf / cdf[-1] # normalize
# use linear interpolation of cdf to find new pixel values
	im2 = interp(im.flatten(),bins[:-1],cdf)
    
	return im2.reshape(im.shape), cdf


def showallhist(imgname):
	im = array(Image.open(imgname).convert('L'))
	print im
	im3 = histeq(im)
	im_output=cv2.equalizeHist(im)
	
	combImage2= Image.fromarray(im_output)
	img2=combImage2.save(imgname+'_enhance_'+'.jpeg')
	

	
	print im_output
	
	ax1=plt.subplot(221)
	plt.xlim([0,255])
	plt.title('Histogram BEFORE Equalization')
	plt.xlabel('DN values')
	plt.ylabel('Number of pixels')
	
	ax2=plt.subplot(222)
	plt.xlim([0,255])
	plt.title('Histogram AFTER Equalization')
	plt.xlabel('DN values')
	plt.ylabel('NUmber of pixels')
	
	
	ax3=plt.subplot(223)
	plt.axis('off')
	plt.title('Image BEFORE Equalization')
	
	ax4=plt.subplot(224)
	plt.axis('off')
	plt.title('Image AFTER  Equalization')
	ax1.hist(im.flatten(),256)
	ax2.hist(im3,256)
	ax3.imshow(im,cmap=cm.Greys_r)
	ax4.imshow(im_output,cmap=cm.Greys_r)
	plt.tight_layout()
	
	plt.show()
	



	
def bandPrint():
	global entry_fn
	savefn=entry_fn.get()
	
	if(opt1.get()== ""):
		showerror("Error", "Two same bands selected")
	else:
		global fileName
		print fileName
		ch1 = int(opt1.get())
		dataset =gdal.Open(fileName,gdal.GA_ReadOnly)
		band_select=dataset.GetRasterBand(ch1)
		array_img=band_select.ReadAsArray()
		
		Image_of_band= Image.fromarray(array_img)
		img=Image_of_band.save(savefn +'.jpeg')
		imgn=savefn+'.jpeg'
		print 'completed'
		print img
		print array_img
		showallhist(imgn)
		
		
		#hist(im)
		
		#combImage.show()            

w=tk.Tk()

w.title("Histogram Equalization")
frame2=tk.Frame(w)
(cols,rows,bands,bandArray) = tifwork.detailsTIF(dataset)

    
optionList=[]
for k in range(1, bands+1):
	optionList.append(k)

x1=tk.Label(frame2, text="Select Band")
x1.pack(side=tk.LEFT, pady = 5 , padx = 5 )
opt1= ttk.Combobox(frame2,values=optionList, width=5)
opt1.pack(side = tk.LEFT , pady = 5,padx = 5 )

frame2.pack(side=tk.TOP, pady = 5 , padx = 5 )

frame6=tk.Frame(w)
lfn=tk.Label(frame6,text='Save file As :')
lfn.pack(side=tk.LEFT)
entry_fn=tk.Entry(frame6)
entry_fn.pack(side=tk.LEFT)



frame6.pack(side=tk.TOP)

button = tk.Button(w, width=20, text="Show Histogram Equalization", command=bandPrint)
button.pack(side = tk.TOP , pady = 5 , padx = 5 )

w.mainloop()  
# read image to array
#im = array(Image.open('x.jpg').convert('L'))
#figure()
# don't use colors
#gray()
# show contours with origin upper left corner
#contour(im, origin='image')
#axis('equal')
#axis('off')
#show()

"""

def showequalhist():
	pass

def displayimg(im):
	figure()
     # don't use colors
	gray()
# show contours with origin upper left corner
	contour(im, origin='image')
	axis('equal')
	axis('off')
	show()
"""

"""
def numbands(filename_extract):
	dataset =gdal.Open(filename_extract,gdal.GA_ReadOnly)
	if dataset is None:
		print 'Could Not Open' + filename
		#Alternatively Raise an Event here
		sys.exit(1)
	bands = dataset.RasterCount
	return bands


#GUI




#end of GUI
# create a new figure
#figure()
# don't use colors
#gray()
# show contours with origin upper left corner
#contour(im, origin='image')
#axis('equal')
#axis('off')
"""
