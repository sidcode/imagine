
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

import tktable


    



global mastercount
global slavecount
mastercount=0
slavecount=0

abca=[]
defa=[]
clicks=[]

x=0
y=0

global list_Master
global list_Slave
list_Master=[]
list_Slave=[]
global keyx
keyx=False

keyyx=False

global Xmain , Ymain
Xmain = 0 
Ymain = 0

def solve():
	global order
	global abca, defa
	if order==2:

		#def quadsolve():
		print clicks
		
		arr=clicks[:]
		p=np.array([[(arr[0][0])**2,(arr[0][1])**2,arr[0][0], arr[0][1],arr[0][0]*arr[0][1], 1], [(arr[1][0])**2, (arr[1][1])**2,arr[1][0], arr[1][1], arr[1][0] * arr[1][1], 1], [(arr[2][0])**2, (arr[2][1])**2,arr[2][0], arr[2][1], arr[2][0]*arr[2][1], 1], [(arr[3][0])**2,(arr[3][1])**2,arr[3][0], arr[3][1],arr[3][0]*arr[3][1], 1],[(arr[4][0])**2,(arr[4][1])**2,arr[4][0], arr[4][1],arr[4][0]*arr[4][1], 1],[(arr[5][0])**2,(arr[5][1])**2,arr[5][0], arr[5][1],arr[5][0]*arr[5][1], 1]])
		q=np.array([arr[6][0], arr[7][0], arr[8][0], arr[9][0], arr[10][0], arr[11][0]])
		abca=np.linalg.solve(p,q)
		
		
		print abca
		
		p=np.array([[(arr[0][0])**2,(arr[0][1])**2,arr[0][0], arr[0][1],arr[0][0]*arr[0][1], 1], [(arr[1][0])**2, (arr[1][1])**2,arr[1][0], arr[1][1], arr[1][0] * arr[1][1], 1], [(arr[2][0])**2, (arr[2][1])**2,arr[2][0], arr[2][1], arr[2][0]*arr[2][1], 1], [(arr[3][0])**2,(arr[3][1])**2,arr[3][0], arr[3][1],arr[3][0]*arr[3][1], 1],[(arr[4][0])**2,(arr[4][1])**2,arr[4][0], arr[4][1],arr[4][0]*arr[4][1], 1],[(arr[5][0])**2,(arr[5][1])**2,arr[5][0], arr[5][1],arr[5][0]*arr[5][1], 1]])
		q=np.array([arr[6][1], arr[7][1], arr[8][1], arr[9][1], arr[10][1], arr[11][1]])
	   
		defa=np.linalg.solve(p,q)
		
		print defa
	if order==1:
		#def linsolve():
		
		print clicks
		arr=clicks[:]
		p=np.array([[arr[0][0],arr[0][1], 1], [arr[1][0], arr[1][1], 1], [arr[2][0], arr[2][1], 1]])
		q=np.array([arr[3][0], arr[4][0], arr[5][0]])
		abca=np.linalg.solve(p,q)
		
		print abca
		
		p=np.array([[arr[0][0],arr[0][1], 1], [arr[1][0], arr[1][1], 1], [arr[2][0], arr[2][1], 1]])
		q=np.array([arr[3][1], arr[4][1], arr[5][1]])
		defa=np.linalg.solve(p,q)
		
		print defa
		
		X1=(arr[0][0])*abca[0]+()()
		   
	if order==3: 
		#def cubicsolve():
		print clicks
		arr=clicks[:]
		p=np.array([[(arr[0][0])**3,(arr[0][1])**3,(arr[0][0])**2,(arr[0][1])**2,((arr[0][0])**2)*(arr[0][1]),(arr[0][0])*(arr[0][1])**2,(arr[0][0])(arr[0][1]),arr[0][0],arr[0][1], 1], [(arr[1][0])**3,(arr[1][1])**3,(arr[1][0])**2,(arr[1][1])**2,((arr[1][0])**2)*(arr[1][1]),(arr[1][0])*(arr[1][1])**2,(arr[1][0])*(arr[1][1]),arr[1][0],arr[1][1], 1], [(arr[2][0])**3,(arr[2][1])**3,(arr[2][0])**2,(arr[2][1])**2,((arr[2][0])**2)*(arr[2][1]),(arr[2][0])*(arr[2][1])**2,(arr[2][0])*(arr[2][1]),arr[2][0],arr[2][1], 1],[(arr[3][0])**3,(arr[3][1])**3,(arr[3][0])**2,(arr[3][1])**2,((arr[3][0])**2)*(arr[3][1]),(arr[3][0])*(arr[3][1])**2,(arr[3][0])*(arr[3][1]),arr[3][0],arr[3][1], 1],[(arr[4][0])**3,(arr[4][1])**3,(arr[4][0])**2,(arr[4][1])**2,((arr[4][0])**2)*(arr[4][1]),(arr[4][0])*(arr[4][1])**2,(arr[4][0])*(arr[4][1]),arr[4][0],arr[4][1], 1],[(arr[5][0])**3,(arr[5][1])**3,(arr[5][0])**2,(arr[5][1])**2,((arr[5][0])**2)*(arr[5][1]),(arr[5][0])*(arr[5][1])**2,(arr[5][0])*(arr[5][1]),arr[5][0],arr[5][1], 1],[(arr[6][0])**3,(arr[6][1])**3,(arr[6][0])**2,(arr[6][1])**2,((arr[6][0])**2)*(arr[6][1]),(arr[6][0])*(arr[6][1])**2,(arr[6][0])*(arr[6][1]),arr[6][0],arr[6][1], 1],[(arr[7][0])**3,(arr[7][1])**3,(arr[7][0])**2,(arr[7][1])**2,((arr[7][0])**2)*(arr[7][1]),(arr[7][0])*(arr[7][1])**2,(arr[7][0])*(arr[7][1]),arr[7][0],arr[7][1], 1],[(arr[8][0])**3,(arr[8][1])**3,(arr[8][0])**2,(arr[8][1])**2,((arr[8][0])**2)*(arr[8][1]),(arr[8][0])*(arr[8][1])**2,(arr[8][0])*(arr[8][1]),arr[8][0],arr[8][1], 1],[(arr[9][0])**3,(arr[9][1])**3,(arr[9][0])**2,(arr[9][1])**2,((arr[9][0])**2)*(arr[9][1]),(arr[9][0])*(arr[9][1])**2,(arr[9][0])*(arr[9][1]),arr[9][0],arr[9][1], 1]])
		q=np.array([arr[10][0], arr[11][0], arr[12][0],arr[13][0],arr[14][0],arr[15][0],arr[16][0],arr[17][0],arr[18][0],arr[19][0]])
		abca=np.linalg.solve(p,q)
		
		print abca
		
		p=np.array([[(arr[0][0])**3,(arr[0][1])**3,(arr[0][0])**2,(arr[0][1])**2,((arr[0][0])**2)*(arr[0][1]),(arr[0][0])*(arr[0][1])**2,(arr[0][0])(arr[0][1]),arr[0][0],arr[0][1], 1], [(arr[1][0])**3,(arr[1][1])**3,(arr[1][0])**2,(arr[1][1])**2,((arr[1][0])**2)*(arr[1][1]),(arr[1][0])*(arr[1][1])**2,(arr[1][0])*(arr[1][1]),arr[1][0],arr[1][1], 1], [(arr[2][0])**3,(arr[2][1])**3,(arr[2][0])**2,(arr[2][1])**2,((arr[2][0])**2)*(arr[2][1]),(arr[2][0])*(arr[2][1])**2,(arr[2][0])*(arr[2][1]),arr[2][0],arr[2][1], 1],[(arr[3][0])**3,(arr[3][1])**3,(arr[3][0])**2,(arr[3][1])**2,((arr[3][0])**2)*(arr[3][1]),(arr[3][0])*(arr[3][1])**2,(arr[3][0])*(arr[3][1]),arr[3][0],arr[3][1], 1],[(arr[4][0])**3,(arr[4][1])**3,(arr[4][0])**2,(arr[4][1])**2,((arr[4][0])**2)*(arr[4][1]),(arr[4][0])*(arr[4][1])**2,(arr[4][0])*(arr[4][1]),arr[4][0],arr[4][1], 1],[(arr[5][0])**3,(arr[5][1])**3,(arr[5][0])**2,(arr[5][1])**2,((arr[5][0])**2)*(arr[5][1]),(arr[5][0])*(arr[5][1])**2,(arr[5][0])*(arr[5][1]),arr[5][0],arr[5][1], 1],[(arr[6][0])**3,(arr[6][1])**3,(arr[6][0])**2,(arr[6][1])**2,((arr[6][0])**2)*(arr[6][1]),(arr[6][0])*(arr[6][1])**2,(arr[6][0])*(arr[6][1]),arr[6][0],arr[6][1], 1],[(arr[7][0])**3,(arr[7][1])**3,(arr[7][0])**2,(arr[7][1])**2,((arr[7][0])**2)*(arr[7][1]),(arr[7][0])*(arr[7][1])**2,(arr[7][0])*(arr[7][1]),arr[7][0],arr[7][1], 1],[(arr[8][0])**3,(arr[8][1])**3,(arr[8][0])**2,(arr[8][1])**2,((arr[8][0])**2)*(arr[8][1]),(arr[8][0])*(arr[8][1])**2,(arr[8][0])*(arr[8][1]),arr[8][0],arr[8][1], 1],[(arr[9][0])**3,(arr[9][1])**3,(arr[9][0])**2,(arr[9][1])**2,((arr[9][0])**2)*(arr[9][1]),(arr[9][0])*(arr[9][1])**2,(arr[9][0])*(arr[9][1]),arr[9][0],arr[9][1], 1]])
		q=np.array([arr[10][1], arr[11][1], arr[12][1],arr[13][1],arr[14][1],arr[15][1],arr[16][1],arr[17][1],arr[18][1],arr[19][1]])
		defa=np.linalg.solve(p,q)
		
		print defa
	   



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


keyyx=False    

def valueofkey2():
	global keyyx
	return keyyx

def setkeyy():
    global keyy
    keyy=True   

def resetkeyy():
    global keyy    
    keyy=False   

def resetkeyyx():
    global keyyx    
    keyyx=False   


    
def valueofkey2():
    global keyyx
    return keyyx
    
val=[]
def setkeyyx():
	global keyyx
	keyyx=True
	
def exit():
    root.destroy()

def viewerwin2():        
    global Root4
    global order
    global r1
    order=r1.get()
    order = int(order)
    print 'order=',order
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
    button.pack(side=tk.LEFT)  
    button2=tk.Button(frame1, width=5, height=2, text='GO', command=solve)         
    button2.pack(side=tk.LEFT) 
    
    button3=tk.Button(frame1, width=10, height=2, text='POINT SHOW',command=setkeyyx)         
    button3.pack(side=tk.LEFT) 
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
    
        
#slave
def mouse_input_event(event):
    global x,y    
    global order
    global clicks
    if valueofkey():
        global mastercount
        global slavecount
        mastercount=mastercount+1
        print 'input pixel loc is ',event.xdata,' ', event.ydata
        a.plot(event.xdata, event.ydata,'rx')
        if valueofkey2():
			x=event.xdata
			y=event.ydata
			print x, y 
			print "\n"
        tktable.write_to_table_master(np.round(event.xdata),np.round(event.ydata),mastercount,slavecount)
        clicks.append([event.xdata,event.ydata])
        list_Master.append([np.round(event.xdata), np.round(event.ydata)])
        print "List slave \n", list_Master
        print "\n"
        resetkeyx()
    if keyyx:
		print "yoyo\n yoyo \n yooy\n"
		global Xmain
		global Ymain
		if order==1:
			Xmain=abca[0]*(x)+abca[1]*(y)+abca[2]
			Ymain=defa[0]*(x)+defa[1]*(y)+defa[2]   
			mouse_input_eventx(event)	
		if order==2:
			Xmain=abca[0]*(x)**2+abca[1]*(y)**2+abca[2]*(x)+abca[3]*(y)+abca[4]*(x)*(y)+abca[5]
			Ymain=defa[0]*(x)**2+defa[1]*(y)**2+defa[2]*(x)+defa[3]*(y)+defa[4]*(x)*(y)+defa[5]   
			mouse_input_eventx(event)	
		if order==3:
			Xmain=abca[0]*(x)**3+abca[1]*(y)**3+abca[2]*(x)**2+abca[3]*(y)**2+abca[4]*(x)**2*(y)+abca[5]*(x)*(y)**2+abca[6]*(x)*(y)+abca[7]*(x)+abca[8]*(y)+abca[9]
			Ymain=defa[0]*(x)**3+defa[1]*(y)**3+defa[2]*(x)**2+defa[3]*(y)**2+defa[4]*(x)**2*(y)+defa[5]*(x)*(y)**2+defa[6]*(x)*(y)+defa[7]*(x)+defa[8]*(y)+defa[9]
			mouse_input_eventx(event)	
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
        print 'event is ', event
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
	global clicks
	global x,y
	global Xmain
	global Ymain
	global mastercount
	global slavecount
	if valueofkey2():
		
		print Xmain,"\n" , Ymain
		ax.plot(Xmain, Ymain,'rx') 
		print 'fyfdflih'
		tktable.write_to_table_master(np.round(Xmain),np.round(Ymain),mastercount,slavecount)
		resetkeyyx()
	if valueofkey1():
			
			slavecount=slavecount+1
			print 'input pixel loc is ',event.xdata,' ', event.ydata
			ax.plot(event.xdata, event.ydata,'rx')
			tktable.write_to_table_slave(np.round(event.xdata),np.round(event.ydata),slavecount,mastercount)
			clicks.append([event.xdata,event.ydata])
			list_Slave.append([np.round(event.xdata), np.round(event.ydata)])
			print list_Slave
			resetkeyy()        
	canvasx.show() 

def key_input_eventx(event):
    if valueofkey1():
        global mastercount
        global slavecount
        slavecount=slavecount+1
        print 'input pixel loc is ',event.xdata,' ', event.ydata
        ax.plot(event.xdata, event.ydata,'bx')
        tktable.write_to_table_slave(np.round(event.xdata),np.round(event.ydata),slavecount,mastercount)
        list_Slave.append([np.round(event.xdata), np.round(event.ydata)])
        print list_Slave
        resetkeyy()
        
    canvasx.show() 
def open_rectification_Slave():    
    
    fileName=tkFileDialog.askopenfilename(title='select reference image')
    
    global fx
    global ax
    fx = Figure(figsize=(5,4), dpi=100)
    ax = fx.add_subplot(111)    
    img=mpimg.imread(fileName)
    ax.imshow(img)
    print 'hi'
# a tk.DrawingArea
    global canvasx
    global x,y
    
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
    global poly
    global r1
    """selection=" "
    #fileName=tkFileDialog.askopenfilename()
    if(fileName == ''):
        pass
    else:
        print(fileName)
        im=(tifwork.openTIF(fileName))   
        def sel():
            selection =str(var.get())
            print selection
     
        def printEntry():
            print selection """ 
            
    global Root4
    Root4=tk.Tk()
    Root4.title('Choose Polynomial order')
    Root4.geometry('200x200')
    var = IntVar()
    r1=Spinbox(Root4,from_=1,to=3)
    r1.pack()
    
    print poly
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
s
    E1.pack(side = RIGHT)
    selection=E1.get()"""
        
    Root4.mainloop()
            
    '''
    image=Image.open(im)
    image1=ImageTk.PhotoImage(image)
    imagesprite=c.create_image(500,500,image=image1)
    return im
    '''

    

        

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

photo3 = tk.PhotoImage(file="close.gif")
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

root.mainloop()

