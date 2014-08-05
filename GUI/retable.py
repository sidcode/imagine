
import Tkinter as tk
from Tkinter import *
from tkMessageBox import *
import ttk
import tkFileDialog
from PIL import Image
import tifwork
import sys
import matplotlib


matplotlib.use('TkAgg')
from Tkinter import *
from tkFileDialog import askopenfilename
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.figure import Figure
from pylab import *
#import Image, ImageTk
import tktable


    



global mastercount
global slavecount
mastercount=0
slavecount=0


global list_Master
global list_Slave
list_Master=[]
list_Slave=[]
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

global keyy
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

val=[]

def exit():
    root.destroy()



def imdisplay(filename):        

        filename = '2.gif'

	global Root1
	Root1 = tk.Toplevel(root)
	Root1.wm_title("Image Display")
        Root1.geometry("600x600")
	
        global keyy
        resetkeyy()
	
        openImFile(filename)
        

def openImFile(filename):    
    
    
    global fx
    global ax
    fx = Figure(figsize=(5,4), dpi=100)
    ax = fx.add_subplot(111)    
    img=mpimg.imread(filename)
    ax.imshow(img)

# a tk.DrawingArea
    global canvasx
    canvasx = FigureCanvasTkAgg(fx, master=Root1)
    canvasx.show()
        
    canvasx.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2TkAgg( canvasx, Root1 )
    toolbar.update()
    canvasx._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
	
    def on_key_event(event):	
        print('you pressed %s'%event.key)
        key_press_handler(event, canvasx, toolbar)        

       
    fx.canvas.mpl_connect('button_press_event',mouse_input_eventx)
    fx.canvas.mpl_connect('key_press_event', on_key_event)
        
    def _quitx():
        Root1.quit()     # stops mainloop
	Root1.destroy()  # this is necessary on Windows to pprevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    button1 = tk.Button(master=Root1, text='Quit', command=_quitx)
    button1.pack(side=tk.BOTTOM)
    button = tk.Button(master=Root1, text='select', command=clickx)
    button.pack(side=tk.BOTTOM)


def viewerwin2():        
	global Root4
	Root4.quit()
	Root4.destroy()
	
	global Root1
	Root1 = tk.Toplevel(root)
	Root1.wm_title("Open Master Image")
        Root1.geometry("600x600")
	
        global keyy
        resetkeyy()
		
	frame=tk.Frame(Root1)
	frame1=tk.Frame(frame)
	frame2=tk.Frame(frame)
	button = tk.Button(frame1, width=5, height=2, text='Open',command=open_rectification_Slave)
	button.pack()			
	frame1.pack(side=tk.LEFT)
	frame2.pack(side=tk.LEFT)
	frame.pack()
        

	
def viewerwin():
	
	global Root
	Root = tk.Toplevel(root)
	Root.wm_title("Open Slave Image")
        Root.geometry("600x600")
        global keyx
        resetkeyx()
	
	
	frame=tk.Frame(Root)
	frame1=tk.Frame(frame)
	frame2=tk.Frame(frame)
	button = tk.Button(frame1, width=5, height=2, text='Open',command=open_rectification_Master)
	button.pack()
	
	button1 = tk.Button(frame2, width=5, height=2, text='Proceed',command=openref)
	button1.pack()
   
		
	frame1.pack(side=tk.LEFT)
	frame2.pack(side=tk.LEFT)
	frame.pack()



def click():
    setkeyx()
    
        
def mouse_input_event(event):
    if valueofkey():
        global mastercount
        global slavecount
        mastercount=mastercount+1
        print 'input pixel loc is ',event.xdata,' ', event.ydata
        a.plot(event.xdata, event.ydata,'b.')
        tktable.write_to_table_master(np.round(event.xdata),np.round(event.ydata),mastercount,slavecount)
        list_Master.append([np.round(event.xdata), np.round(event.ydata)])
        print list_Master
        resetkeyx()
    canvas.show() 
    
      		


def open_rectification_Master():    
    

    
    fileName=tkFileDialog.askopenfilename(title='select image to be rectified')
    
    global f
    global a
    f = Figure(figsize=(5,4), dpi=100)
    a = f.add_subplot(111)    
    img=mpimg.imread(fileName)
    a.imshow(img)

# a tk.DrawingArea
    global canvas
    canvas = FigureCanvasTkAgg(f, master=Root)
    canvas.show()
        
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2TkAgg( canvas, Root )
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
   
    def on_key_event(event):	
        print('you pressed %s'%event.key)
        key_press_handler(event, canvas, toolbar)        
    print "Tkable"
     
    f.canvas.mpl_connect('button_press_event',mouse_input_event)
    f.canvas.mpl_connect('key_press_event', on_key_event)
        
    def _quit():
        Root.quit()     # stops mainloop
	Root.destroy()  # this is necessary on Windows to pprevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    button1 = tk.Button(master=Root, text='Quit', command=_quit)
    button1.pack(side=tk.BOTTOM)
    button = tk.Button(master=Root, text='select', command=click)
    button.pack(side=tk.BOTTOM)
    tktable.sample_test() 
def clickx():
    setkeyy()
       
def mouse_input_eventx(event):
    if valueofkey1():
        global mastercount
        global slavecount
        slavecount=slavecount+1
        print 'input pixel loc is ',event.xdata,' ', event.ydata
        ax.plot(event.xdata, event.ydata,'b.')
        tktable.write_to_table_slave(np.round(event.xdata),np.round(event.ydata),slavecount,mastercount)
        list_Slave.append([np.round(event.xdata), np.round(event.ydata)])
        print list_Slave
        resetkeyy()
        
    canvasx.show() 
    
def open_rectification_Slave():    
    
    fileName=tkFileDialog.askopenfilename(title='select slave image to be rectified')
    
    global fx
    global ax
    fx = Figure(figsize=(5,4), dpi=100)
    ax = fx.add_subplot(111)    
    img=mpimg.imread(fileName)
    ax.imshow(img)

# a tk.DrawingArea
    global canvasx
    canvasx = FigureCanvasTkAgg(fx, master=Root1)
    canvasx.show()
        
    canvasx.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2TkAgg( canvasx, Root1 )
    toolbar.update()
    canvasx._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
	
    def on_key_event(event):	
        print('you pressed %s'%event.key)
        key_press_handler(event, canvasx, toolbar)        

       
    fx.canvas.mpl_connect('button_press_event',mouse_input_eventx)
    fx.canvas.mpl_connect('key_press_event', on_key_event)
        
    def _quitx():
        Root1.quit()     # stops mainloop
	Root1.destroy()  # this is necessary on Windows to pprevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    button1 = tk.Button(master=Root1, text='Quit', command=_quitx)
    button1.pack(side=tk.BOTTOM)
    button = tk.Button(master=Root1, text='select', command=clickx)
    button.pack(side=tk.BOTTOM)

 	
def openref():
	
            
    global Root4
    Root4=tk.Tk()
    Root4.title('Choose Polynomial order')
    Root4.geometry('200x200')
    var = IntVar()
    r1=Spinbox(Root4,from_=0,to=100)
    r1.pack()
    buttona = tk.Button(master=Root4, text='GO', command=viewerwin2)
    buttona.pack(side=tk.BOTTOM)
    """R1 = Radiobutton(a, text="Order 0", variable=var, value=0)
    R1.pack( anchor = W )

    R2 = Radiobutton(a, text="Order 1", variable=var, value=1)
    R2.pack( anchor = W )

    R3 = Radiobutton(a, text="Order 2", variable=var, value=2)
    R3.pack( anchor = W)

    label = Label(a)
    label.pack()
        
        
    L1 = Label(a, text="other")
    L1.pack( side = LEFT)
    E1 = Entry(a, bd =5)

    E1.pack(side = RIGHT)
    selection=E1.get()"""
        
    a.mainloop()
            
	
    image=Image.open(im)
    image1=ImageTk.PhotoImage(image)
    imagesprite=c.create_image(500,500,image=image1)
    return im
	

    

		

def rgbselect():
   
    fileName=tkFileDialog.askopenfilename()
    if(fileName == ''):
        pass
    else:
        print(fileName)
        dataset=(tifwork.openTIF(fileName))

    w=tk.Tk()
  
    def bandPrint():
        if(not(opt1.get() and opt2.get() and opt3.get())):
           showerror("Error", "All bands not selected")
        elif(opt1.get()==opt2.get() or opt1.get()==opt3.get() or opt2.get()==opt3.get()):
            showerror("Error", "Two same bands selected")
        else:
            bandArr = tifwork.getBand(dataset,bands,bandArray)
            tifwork.selectBand(bandArr,rows,cols,opt1.get(),opt2.get(),opt3.get())
    
    frame4 = tk.Frame(w)
#    frame4.grid()
    frame2=tk.Frame(frame4)
#    frame2.grid()
    frame3=tk.Frame(frame4)
#    frame3.grid()
    frame5 = tk.Frame(w)
#    frame5.grid()
    w.title("Band Selection")
    (cols,rows,bands,bandArray) = tifwork.detailsTIF(dataset)

    
    optionList=[]
    for k in range(1, bands+1):
        optionList.append(k)

    x1=tk.Label(frame2, text="Red")
    x1.pack(side=tk.TOP, pady = 5 , padx = 5 )
    opt1= ttk.Combobox(frame3,values=optionList, width=5)
    opt1.pack(side = tk.TOP , pady = 5,padx = 5 )
    
    x2=tk.Label(frame2, text="Blue")
    x2.pack(side = tk.TOP , pady = 5 , padx = 5 )
    opt2= ttk.Combobox(frame3 , values=optionList, width=5)
    opt2.pack(side = tk.TOP , pady = 5 , padx = 5 )

    x3=tk.Label(frame2, text="Green")
    x3.pack(side = tk.TOP , pady = 5 , padx = 5 )
    opt3= ttk.Combobox(frame3, values=optionList,  width=5)
    opt3.pack(side = tk.TOP , pady = 5 , padx = 5 )

    frame2.pack(side=tk.LEFT, pady = 5 , padx = 5 )
    frame3.pack(side=tk.LEFT, pady = 5 , padx = 5 )
    frame4.pack(side= tk.TOP, pady = 5 , padx = 5 )

    button = tk.Button(frame5, width=10, text="Show", command=bandPrint)
    button.pack(side = tk.TOP , pady = 5 , padx = 5 )
    frame5.pack(side=tk.TOP , pady = 5 , padx = 5 )
    
#opens the root window
root=tk.Tk()

root.title("Image Processing")

frame1 = tk.Frame(root, width=800)

#to display the frame
frame1.pack()

#keeps only the frame
root.overrideredirect(0)
root.resizable(0,0)

photo3 = tk.PhotoImage(file="2.gif")
button3 = tk.Button(frame1, width=100, height=100, image=photo3)
button3.pack(side=tk.LEFT, padx=2, pady=2)
button3.image = photo3


photo2 = tk.PhotoImage(file="1.gif")
button2 = tk.Button(frame1, width=100, height=100, image=photo2, command=rgbselect)
button2.pack(side=tk.LEFT, padx=2, pady=2)
button2.image = photo2

button5 = tk.Button(frame1, width=20, height=6, text='Geometric correction',justify=tk.LEFT,command=viewerwin)
button5.pack(side=tk.LEFT, padx=2, pady=2)


photo1 = tk.PhotoImage(file="3.gif")
button1 = tk.Button(frame1, width=100, height=100, image=photo1, command=exit)
button1.pack(side=tk.LEFT, padx=2, pady=2)
button1.image = photo1

imdisplay('3.jpg')

root.mainloop()

