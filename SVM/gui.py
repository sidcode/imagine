import Tkinter as tk
from Tkinter import *
from tkMessageBox import *
import ttk
from PIL import Image
import tifwork
from tkFileDialog import askopenfilename
import sys
import matplotlib
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.figure import Figure
#from pylab import *
import cv,cv2
import scipy.misc
import numpy as np

def getData(fileName, num):
    #get dataset
    dataset = tifwork.openTIF(fileName)

    #get details of dataset
    (cols,rows,bands,bandArray) = tifwork.detailsTIF(dataset)

    #get all bands
    bandArray = tifwork.getBand(dataset,bands,bandArray)

    #input a band

    workData = bandArray[:,:,num-1]

    #show original image and plot it
    imdata = Image.fromarray(workData)
    imdata = imdata.convert('L')
    imdata.save('original.jpg')
    #plot(workData,'Original')
    filename = 'original.jpg'
    return filename
    
global index 
index = []
val=[]
def exit():
    root.destroy()

def index_return():
    global index
    return index[:,0]

def viewerwin(fileName):
	global index
	Root = tk.Tk()
	Root.wm_title("Rectifiction")        
        Root.geometry("1080x720")	
	frame8=tk.Frame(Root)	
	frame8.pack()
	f = Figure(figsize=(5,4), dpi=100)
	a = f.add_subplot(111)
	filename= 'sja.jpg'	
        img=mpimg.imread(filename)
        #grayScaleImage = cv2.cvtColor(img,cv.CV_BGR2GRAY)
        #print grayScaleImage        
        a.axis('off')
	a.imshow(img)
        overlayImage = np.ones_like(img)
        overlayImage +=254
        #over = np.copy(overlayImage)        
        #print overlayImage
        opacity = 1
        # a tk.DrawingArea
	canvas = FigureCanvasTkAgg(f, master=Root)
	canvas.show()        
	canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
	toolbar = NavigationToolbar2TkAgg( canvas, Root )
	toolbar.update()
	canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)        
        global polygon
        polygon = []
        closeFlag = False        
        def mouse_input_event(event):
            global polygon
            global index
            #print 'Event is ', event
            print 'input pixel loc is ',event.xdata,' ', event.ydata
            polygon.append([np.int(event.xdata),np.int(event.ydata)])
            a.plot(event.xdata,event.ydata,'b.')
            poly = plt.Polygon(polygon,closed = event.dblclick, fill = None, edgecolor ='b')
            f.gca().add_patch(poly)            
            if (event.dblclick == True):
                poly = plt.Polygon(polygon,closed = event.dblclick, fill = None, edgecolor ='b')
            	f.gca().add_patch(poly)
            	canvas.show()
                polygon.pop()
                polygon = [polygon]
                print polygon               
                cv2.drawContours(overlayImage,np.array(polygon),0,255)
                maskImage = np.zeros_like(img)
                cv2.drawContours(maskImage,np.array(polygon),0,255,-1)
                extractedImage = np.bitwise_and(over,maskImage)
                #print extractedImage.shape
                rows,cols,bands = extractedImage.shape
                #print extractedImage                
                index = extractedImage > 0                                
                #extract = extractedImage.reshape((rows*cols),bands)                
                print index[:,0]
                scipy.misc.imsave("poly1.jpg",extractedImage)
                polygon = []            	
            canvas.show()            
        f.canvas.mpl_connect('button_press_event',mouse_input_event)        
	def _quit():
	    	Root.destroy()  # this is necessary on Windows to pprevent
	button = tk.Button(master=Root, text='Quit', command=_quit)
	button.pack(side=tk.BOTTOM)
    	button = tk.Button(master=Root, text='Done', command=index_return)
	button.pack(side=tk.BOTTOM)
