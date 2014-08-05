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
global fx,ax
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.figure import Figure
import pylab
#import Image, ImageTk
import tktable

# read image to array

# create a new figure
#figure()
# don't use colors
#gray()
# show contours with origin upper left corner
#contour(im, origin='image')
#axis('equal')
#axis('off')

gdal.AllRegister()

global counter
counter=0

global num,den
num=1
den=1

global click2
click2=[]

global click3
click3=[]

global keyx
keyx=False
def valueofkey():
    global keyx
    return keyx

def setkeyx():
    global keyx    
    keyx=True    

def resetkeyx():
    global keyx    
    keyx=False 

global keyy,bandF
global status,lcom,a,frame4
status='Status :'+'Pending'
keyy=False
def valueofkey1():
    global keyy
    return keyy

def setkeyy():
    global keyy
    keyy=True   

def resetkeyy():
    global keyy    
    keyy=False   
# defining functions for showing image and its enhacement

def linearp(array1,slope,c):
    array1=np.array(array1,'uint64')    
    array1=(slope*array1)+c
    print array1
    return array1

def logp(array1,slope,c):
	array1=np.array(array1,'uint64')  
	array1=(array1 + 1)  
	array1=(slope*array1)+c
	print array1
	return array1
	
def expp(array1,slope,c):
	array1=np.array(array1,'uint64')   
	array1=(slope*array1)+c
	print array1
	return array1

def piecewise(x1,x2,y1,y2,array):
	array_pw=np.array(array,'uint64')
	global opt1
	listvalue=opt1.get()
	print listvalue
    
	index=array_pw >=x1
	print "index"
	print index
	index1=array_pw <= x2
	print "index1"
	print index1
	c_index=index & index1
	print "newarray"
	newarray=array_pw[c_index]
	print newarray
	
	if(listvalue == 'Linear'):
		slope=(float)(y2-y1)/(x2-x1)
		print slope
    
		c=(float)(x2*y1-x1*y2)/(x2-x1)
		print c
		array_op=linearp(newarray,slope,c)
		print "array_op"
		print array_op
		array_pw[c_index]=array_op
		print "arra_pw"    
		print array_pw
		print "printed"
		return array_pw
		
	elif(listvalue=='Logarithmic'):
		y2=np.log(y2)
		y1=np.log(y1)
		x1=np.log(x1)
		x2=np.log(x2)
		
		slope=(float)(y2-y1)/(x2-x1)
		print slope
    
		c=(float)(x2*y1-x1*y2)/(x2-x1)
		print c
		array_op=logp(newarray,slope,c)
		print "array_op"
		print array_op
		array_pw[c_index]=array_op
		print "arra_pw"    
		print array_pw
		print "printed"
		return array_pw
		
	elif(listvalue=='Exponential'):
		y2=np.exp(y2)
		y1=np.exp(y1)
		x1=np.exp(x1)
		x2=np.exp(x2)
		
		slope=(float)(y2-y1)/(x2-x1)
		print slope
    
		c=(float)(x2*y1-x1*y2)/(x2-x1)
		print c
		array_op=expp(newarray,slope,c)
		print "array_op"
		print array_op
		array_pw[c_index]=array_op
		print "arra_pw"    
		print array_pw
		print "printed"
		return array_pw
		
	else:
		global num,den
		print num,den
		power_n=float(num)/den
		y2=np.power(y2,power_n)
		y1=np.power(y1,power_n)
		x1=np.power(x1,power_n)
		x2=np.power(x2,power_n)
		
		slope=(float)(y2-y1)/(x2-x1)
		print slope
    
		c=(float)(x2*y1-x1*y2)/(x2-x1)
		print c
		array_op=linearp(newarray,slope,c)
		print "array_op"
		print array_op
		array_pw[c_index]=array_op
		print "arra_pw"    
		print array_pw
		print "printed"
		return array_pw

def numbands(filename_extract):
	dataset =gdal.Open(filename_extract,gdal.GA_ReadOnly)
	if dataset is None:
		print 'Could Not Open' + filename
		#Alternatively Raise an Event here
		sys.exit(1)
	bands = dataset.RasterCount
	return bands
	
	

def finaloutcome(filename2,x1,x2,y1,y2,filesavedas):
	dataset =gdal.Open(filename2,gdal.GA_ReadOnly)
	if dataset is None:
		print 'Could Not Open' + filename
		#Alternatively Raise an Event here
		sys.exit(1)

	cols = dataset.RasterXSize
	rows = dataset.RasterYSize
	bands = dataset.RasterCount
	print 'Number of bands :'
	print bands
	rgbArray = np.zeros((rows,cols,bands),'uint16')


	for x in range(1,bands+1):
		band=dataset.GetRasterBand(x)
		array=band.ReadAsArray()
    
#R-G-B
		rgbArray[:,:,x-1] = piecewise(x1,x2,y1,y2,array)
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
						combImage.save(filesavedas+str(count)+'.jpeg')
						count=count+1
		                

#end 

def finaloutcome2(filename2,x1,x2,y1,y2,filesavedas,band3):
	dataset =gdal.Open(filename2,gdal.GA_ReadOnly)
	if dataset is None:
		print 'Could Not Open' + filename
		#Alternatively Raise an Event here
		sys.exit(1)

	cols = dataset.RasterXSize
	rows = dataset.RasterYSize
	bands = dataset.RasterCount
	
	rgbArray = np.zeros((rows,cols,bands),'uint16')


	
	band=dataset.GetRasterBand(band3)
	array=band.ReadAsArray()
	print band3
	print 'hello'
	y=band3 -1
	print y
#R-G-B
	rgbArray[:,:,y] = piecewise(x1,x2,y1,y2,array)
	combi= np.zeros((rows,cols,3),'uint8')
	
	combi[:,:,y]=rgbArray[:,:,y]
	combImage= Image.fromarray(combi)
	combImage.save(filesavedas+'.jpeg')
	filesaveNAME=filesavedas+'.jpeg'
	import imageGUI
	imageGUI.imdisplay(filesaveNAME,filesaveNAME)
'''	for i in range(0,bands):
			for j in range(0,bands):
				for k in range(0,bands):
					if( (not i == j) and (not j ==k) and (not k == i) ):
						combi[:,:,0]=rgbArray[:,:,i]
						combi[:,:,1]=rgbArray[:,:,j]
						combi[:,:,2]=rgbArray[:,:,k]
						combImage= Image.fromarray(combi)
						combImage.save(filesavedas+str(count)+'.jpeg')
						count=count+1
f'''                

#end 



def exit():
    root.destroy()
def click():
    setkeyx()

def callback(event):
    print "clicked at", event.x, event.y
    
def mouse_input_event(event):
	global counter
	global click2
	global click3
	global canvas
	if valueofkey():
		print 'input pixel loc is ',event.xdata,' ', event.ydata
		ax.plot(event.xdata, event.ydata,'r.')
		resetkeyx()
		click2.append(event.xdata)
		click3.append(event.ydata)
		counter=counter+1
		print counter
		if(counter % 2 == 0):
			x1=click2[-2]
			x2=click2[-1]
			fx1=click3[-2]
			fx2=click3[-1]
		  
			polygon=([x1,fx1],[x2,fx2])
		  
			print x1,x2,fx1,fx2,polygon
		    	 
			poly = plt.Polygon(polygon,closed = event.dblclick, fill = None, edgecolor ='r')
			fx.gca().add_patch(poly)      
	canvas.show()
	if (counter % 2 == 0):
		getyvalues()
          
def showhist(filename,x):
  hist_display=tk.Frame(x) 
  im = array(Image.open(filename).convert('L'))	
  figure()
  a=hist(im.flatten(),128)
  print a
  show()
  hist_display.bind("<Button-1>", callback)
  hist_display.pack(side=TOP)

#filename=''  
global pt1,pt2,newpt1,newpt2	

def getyvalues():
	global pt1,pt2,newpt1,newpt2
	
	def dispenhanimg():
		global filechosen
		global bandF
		print 'File inside loop correct'
		print filechosen
		pt1=np.round(click2[-2])
		pt2=np.round(click2[-1])
		newpt1=int(entry1.get())
		newpt2=int(entry2.get())
		saveas=entry_fn.get()
		print 'values obtained now'
		print pt1,pt2,newpt1,newpt2,saveas  
		finaloutcome2(filechosen,pt1,pt2,newpt1,newpt2,saveas,bandF)
		a.destroy()
	    	
	
	global a,frame4
	a=tk.Tk()
	a.geometry('300x300')
	global counter
	ename='Contrast enhancement :'+str(counter/2)
	
	a.title(ename)
	label=tk.Label(a,text='Fill the dn values to stretch')
	label.pack()
	
	
	
	text1='Original Pt1 :' + str(round(click2[-2]))
	text2='Original Pt2 :' + str(round(click2[-1]))
	
	frame1=tk.Frame(a)
	
	label1=tk.Label(frame1,text=text1)
	label1.pack(side=tk.LEFT)
	label3=tk.Label(frame1,text='Transform Pt1 :')
	label3.pack(side=tk.LEFT)
	entry1=tk.Entry(frame1,width=10)
	entry1.pack(side=tk.LEFT)
	frame1.pack(side=tk.TOP)
	
	frame2=tk.Frame(a)
	
	label2=tk.Label(frame2,text=text2)
	label2.pack(side=tk.LEFT)
	
	label4=tk.Label(frame2,text='Transform Pt2 :')
	label4.pack(side=tk.LEFT)
	entry2=tk.Entry(frame2,width=10)
	entry2.pack(side=tk.LEFT)
	
	frame2.pack(side=tk.TOP)
	
	optionList=['Linear','Non-linear(power n)','Exponential','Logarithmic']
	#TYpe of enhancement
	frame_type=tk.Frame(a)
	labeltp=tk.Label(frame_type,text='Type of enhancement :',pady = 5 , padx = 5)
	labeltp.pack(side=tk.LEFT)
	global opt1
	opt1= ttk.Combobox(frame_type, values=optionList)
	opt1.pack(side = tk.LEFT )
	frame_type.pack(side=tk.TOP)
	#end
	def getpower():
		global num,den
		num=entrypw1.get()
		den=entrypw2.get()
		print num,den
	
	label_nl1=tk.Label(a,text=' ---------------------------------')
	label_nl1.pack(side=tk.TOP)
	label_nl=tk.Label(a,text=' For non-linear of power n only :')
	label_nl.pack(side=tk.TOP)
	fw1=tk.Frame(a)
		
	lpw1=tk.Label(fw1,text='Enter Numerator')
	entrypw1=tk.Entry(fw1)
	lpw1.pack(side=tk.LEFT)
	entrypw1.pack(side=tk.LEFT)
	fw1.pack(side=tk.TOP)
		
	fw2=tk.Frame(a)
		
	lpw2=tk.Label(fw2,text='Enter Denominator')
	entrypw2=tk.Entry(fw2)
	lpw2.pack(side=tk.LEFT)
	entrypw2.pack(side=tk.LEFT)
	entrypw2.insert(0,'1')
	fw2.pack(side=tk.TOP)
		
	label_nl2=tk.Label(a,text=' --------------------------------')
	label_nl2.pack(side=tk.TOP)		
    
	frame4=tk.Frame(a)
	label_fn=tk.Label(frame4,text='Save File as :')
	label_fn.pack(side=tk.LEFT)
	
	entry_fn=tk.Entry(frame4)
	entry_fn.pack(side=tk.LEFT)
	frame4.pack(side=tk.TOP)

	frame3=tk.Frame(a)
	button6=tk.Button(frame3,text='SUBMIT',command=dispenhanimg)
	button6.pack(side=tk.LEFT)
	
	frame3.pack(side=tk.TOP)

	a.mainloop()


filechosen=''
def showhist2(filename,Root1,band):
	global bandF
	bandF=band
	global fx,ax
	print band
	fx = Figure()
	ax = fx.add_subplot(111)
	
	ax.xlim=([0,30])   
	global Rootx
	global filechosen
	filechosen=filename
	print filename
	resetkeyx()
	
	dataset =gdal.Open(filename,gdal.GA_ReadOnly)
	band_select=dataset.GetRasterBand(band)
	array_img=band_select.ReadAsArray()
	print array_img
	
	#img1=mpimg.imread(filename)
  #print img1
	ax.hist(array_img.flatten(),128)
	

        
	
   
	
	print ';sbhsbvbsjv sv obdi'
  #im = array(Image.open(filename).convert('L'))	
  #figure()
  
 

# a tk.DrawingArea
	global canvas
	canvas = FigureCanvasTkAgg(fx, master=Root1)
	canvas.show()
	      
	canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

	toolbar = NavigationToolbar2TkAgg( canvas, Root1 )
	toolbar.update()
	canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
	
	def on_key_event(event):	
		print('you pressed %s'%event.key)
		key_press_handler(event, canvas, toolbar)        

       
	fx.canvas.mpl_connect('button_press_event',mouse_input_event)
	fx.canvas.mpl_connect('key_press_event', on_key_event)
	      
	def _quitx():
		Root1.quit()     # stops mainloop
		Root1.destroy()  # this is necessary on Windows to pprevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
	button1 = tk.Button(master=Root1, text='Quit', command=_quitx)
	button1.pack(side=tk.BOTTOM)
	button = tk.Button(master=Root1, text='Select', command=click)
	button.pack(side=tk.BOTTOM)
	
	
	

	
'''

"""
def histeq(im,nbr_bins=256):

# get image histogram
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum() # cumulative distribution function
    cdf = 255 * cdf / cdf[-1] # normalize
# use linear interpolation of cdf to find new pixel values
    im2 = interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape), cdf

figure()
im2=histeq(im)
hist(im2,256)
show()

#plt.imshow(im2,cmap=plt.cm.gray)
#plt.savefig('output.jpeg')
#figure##()
#gray()
# show contours with origin upper left corner
#contour(im, origin='image')
#axis('equal')
#axis('off')"""

'''
