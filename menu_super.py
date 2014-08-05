from Tkinter import *
import tkMessageBox
import tkFileDialog
import math
import numpy
import tkColorChooser
import sys
import tifwork
import numpy as np
import PIL.Image as Image
import matplotlib
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.figure import Figure
import cv,cv2
import scipy.misc
import svms
import matplotlib.cm as cm
global bandArray
global bands
global target
global data
global count_target
count_target = 0
global prev
prev = 0

data = None
def getData(fileName, num):
    #get dataset
    global bandArray
    global bands
    global target
    global data
    dataset = tifwork.openTIF(fileName)

    #get details of dataset
    (cols,rows,bands,bandArray) = tifwork.detailsTIF(dataset)

    #get all bands
    bandArray = tifwork.getBand(dataset,bands,bandArray)

    #input a band
    print rows, cols
    workData = bandArray[:,:,num-1]
    if (data == None):
	    data = np.array([]).reshape(0,bands)
	    target = np.array([])
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



def viewerwin(fileName):
	global bandArray
	global index

	def index_return():
	    global data
	    global target
	    global count_target
	    global prev
	    if (count_target == 0):
	    	target = np.append(target, np.zeros(data.shape[0]))
	    	prev = data.shape[0]
            else:
		next = data.shape[0] - prev
		target = np.append(target, (np.ones(next)*count_target))
		prev = data.shape[0]
	    count_target += 1
    	    print 'index_return data ' ,data.shape
	    print 'index_return target' ,target.shape
	    _quit()
	Root = Tk()
	Root.wm_title("Training Data")        
        Root.geometry("800x600")	
	frame8=Frame(Root)	
	frame8.pack()
	f = Figure(figsize=(5,4), dpi=100)
	a = f.add_subplot(111)
	filename= getData(fileName, 1)	
        img=mpimg.imread(filename)
        print img.shape
        #grayScaleImage = cv2.cvtColor(img,cv.CV_BGR2GRAY)
        #print grayScaleImage        
        a.axis('off')
	a.imshow(img,cmap = cm.Greys_r)
        overlayImage = np.ones_like(img)
        overlayImage +=254
        over = np.copy(overlayImage)        
        #print overlayImage
        opacity = 1
        # a tk.DrawingArea
	canvas = FigureCanvasTkAgg(f, master=Root)
	canvas.show()        
	canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
	toolbar = NavigationToolbar2TkAgg( canvas, Root )
	toolbar.update()
	canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)        
        global polygon
        polygon = []
        closeFlag = False        
        def mouse_input_event(event):
            global polygon
            global index
            global bandArray
            global data
            #print 'Event is ', event
            print 'input pixel loc is ',event.xdata,' ', event.ydata
            polygon.append([np.int(event.xdata),np.int(event.ydata)])
            a.plot(event.xdata,event.ydata,'r.')
            poly = plt.Polygon(polygon,closed = event.dblclick, fill = None, edgecolor ='r')
            f.gca().add_patch(poly)            
            if (event.dblclick == True):
                poly = plt.Polygon(polygon,closed = event.dblclick, fill = None, edgecolor ='r')
            	f.gca().add_patch(poly)
            	canvas.show()
                polygon.pop()
                polygon = [polygon]
                print polygon               
                cv2.drawContours(overlayImage,np.array(polygon),0,255)
                maskImage = np.zeros_like(img)
                cv2.drawContours(maskImage,np.array(polygon),0,255,-1)
                extractedImage = np.bitwise_and(over,maskImage)

                rows,cols = extractedImage.shape
                #print extractedImage                
                index = extractedImage > 0      

                #print workData[index]
                extract = bandArray.reshape((rows*cols),bands)   
                index = index.reshape((rows*cols))                
                print extract
                print index
		data =  np.vstack([data,extract[index]])
                print 'data shape' , data.shape
                scipy.misc.imsave("poly1.jpg",extractedImage)
                polygon = []            	
            canvas.show()            
        f.canvas.mpl_connect('button_press_event',mouse_input_event)        
	def _quit():
	    	Root.destroy()  # this is necessary on Windows to pprevent
	
    	button = Button(master=Root, text='Done', command=index_return)
	button.pack(side=BOTTOM)


filename=''
#iteration=0
index=''

def supervi(typ):
  global filename	
  #global iteration  
  global box1
  global root
  root=Tk()
  root.geometry('350x350')
  root.title('Supervised Classification')
  count=0
  
  global i
  i=0

  def end(): 
    global root
    root.destroy()
    
  def showfilename(filen):
    tkMessageBox.showinfo('File Chosen',filen)

  def help_tab():
    tkMessageBox.showinfo("Help","You are too dumb")

  def browse():
    global filename 
    filename=tkFileDialog.askopenfilename(filetypes=[("TIF File","*.tif")])
    showfilename(filename)
    print filename

  def changecolor():
    if ( filename == ''):
    	browse()
    viewerwin(filename)

    
  def endfield():
    global add
    add.destroy()
    stopaddition.destroy()
    global add2
    add2=Button(framebutton,text='Add More',command=addfield )
    add2.pack()

    
  def createfield(name,framename):
    
    name=Entry(framename,width=5)
    name.pack()

  def addfield():
    global i
    global l2
    global box1
    i=i+1
    
    def changecolor2():
      if ( filename == ''):
      	browse()
      viewerwin(filename)
    outerframe=Frame(frame2)
    l1=Label(outerframe,text=str(i+1),width=10)
    l1.pack(side=LEFT)

    l2=Entry(outerframe,width=5)
    l2.pack(side=LEFT)
    l3=Button(outerframe,text='Area',command=changecolor2,width=10)
    l3.pack(side=LEFT)
    outerframe.pack(side=TOP)
   

  def supervised():
	global filename
	global target
	global data
	global count_target	
	print 'data' , data.shape
	print 'target' , target.shape
	svms.svmwork(filename,data,target,typ)	
         
  # create a toplevel menu
  menubar = Menu(root)
  filemenu2=Menu(menubar,tearoff='0')

  filemenu3=Menu(menubar,tearoff='0')
  filemenu3.add_command(label='Open',command=browse)
  filemenu3.add_command(label='Close',command=end)
  menubar.add_cascade(label='Import File',menu=filemenu3)


  # create a pulldown menu, and add it to the menu bar

  menubar.add_cascade(label="Help", menu=filemenu2)

  filemenu2.add_command(label="About Software", command=help_tab)

  root.config(menu=menubar)

  #display buttons
  showimg=Button(root,text='Display Image',command= supervised)
  showimg.pack()

  #creating labels
  frame1=Frame(root)
  lu=Label(frame1,text='Cluster No.',width=10)
  lu.pack(side=LEFT)
  lu1=Label(frame1,text='Name',width=10)
  lu1.pack(side=LEFT)

  lu2=Label(frame1,text='Cluster Area',width=10)
  lu2.pack(side=LEFT)

  frame1.pack(side=TOP)

  global frame2
  frame2=Frame(root)
  #print text

  outerframe=Frame(frame2)
  l1=Label(outerframe,text=str(i+1),width=10)
  l1.pack(side=LEFT)

  l2=Entry(outerframe,width=5)
  l2.pack(side=LEFT)
  l3=Button(outerframe,text='Area',command=changecolor,width=10)
  l3.pack(side=LEFT)
  outerframe.pack(side=TOP)
      
  frame2.pack(side=TOP)
  #submit value
  framebutton=Frame(root,pady=30)
  global add
  add=Button(framebutton,text='Add',command=addfield)
  add.pack(side=LEFT)
  framebutton.pack(side=TOP)
  root.mainloop()
  
#supervi('linear')
