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
import cv,cv2
import scipy.misc

val=[]
def exit():
    root.destroy()

def viewerwin():
	Root = tk.Tk()
	Root.wm_title("Rectifiction")
        
        Root.geometry("1080x720")
	
	
	frame8=tk.Frame(Root)
	frame9=tk.Frame(frame8)
	frame10=tk.Frame(frame8)
	button6 = tk.Button(frame9, width=5, height=2, text='Open',command=rgbselect2)
	button6.pack()
	
	button7 = tk.Button(frame10, width=5, height=2, text='Proceed',command=openref)
	button7.pack()
   
		
	frame9.pack(side=tk.LEFT)
	frame10.pack(side=tk.LEFT)
	frame8.pack()



	f = Figure(figsize=(5,4), dpi=100)
	a = f.add_subplot(111)
	filename="liss3.tif"
	
        img=mpimg.imread(filename)
        #grayScaleImage = cv2.cvtColor(img,cv.CV_BGR2GRAY)
        #print grayScaleImage
        
        a.axis('off')
	a.imshow(img)

        overlayImage = np.ones_like(img)
        overlayImage +=254
        

        over = np.copy(overlayImage)
        
        print overlayImage

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

	def on_key_event(event):
	    print('you pressed %s'%event.key)
            key_press_handler(event, canvas, toolbar)

            
        
        def mouse_input_event(event):
            global polygon
            #print 'Event is ', event
            print 'input pixel loc is ',event.xdata,' ', event.ydata
            polygon.append([np.int(event.xdata),np.int(event.ydata)])
            a.plot(event.xdata,event.ydata,'b.')
            
            

            poly = plt.Polygon(polygon,closed = event.dblclick, fill = None, edgecolor ='b')
            f.gca().add_patch(poly)

            if (event.dblclick == True):
                polygon.pop()
                polygon = [polygon]
                print polygon
               
                cv2.drawContours(overlayImage,np.array(polygon),0,255)
                maskImage = np.zeros_like(img)
                cv2.drawContours(maskImage,np.array(polygon),0,255,-1)
                extractedImage = np.bitwise_and(over,maskImage)
                print extractedImage.shape

                rows,cols,bands = extractedImage.shape

                #print extractedImage
                
                index = extractedImage > 0

                #extract = extractedImage.reshape((rows*cols),bands)
                
                print index[:,0]
                scipy.misc.imsave("poly1.jpg",extractedImage)
                
                

                polygon = []


            
            canvas.show()



            
        f.canvas.mpl_connect('button_press_event',mouse_input_event)
	f.canvas.mpl_connect('key_press_event', on_key_event)
        
        
	def _quit():
		Root.quit()     # stops mainloop
	    	Root.destroy()  # this is necessary on Windows to pprevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
	
	button = tk.Button(master=Root, text='Quit', command=_quit)
	button.pack(side=tk.BOTTOM)
    		


def rgbselect2():
	
    
    fileName=tkFileDialog.askopenfilename(title='select image to be rectified')
    if(fileName == ''):
        pass
    else:
        print(fileName)
        im=(tifwork.openTIF(fileName))
 

def openref():
	
    selection=" "
    fileName=tkFileDialog.askopenfilename(title='select reference image')
    if(fileName == ''):
        pass
    else:
        print(fileName)
        im=(tifwork.openTIF(fileName))   
        def sel():
            selection =str(var.get())
            print selection
     
        def printEntry():
			print selection  
            
        a=tk.Tk()
        a.title('Choose Polynomial order')
        a.geometry('500x500')
        var = IntVar()
        R1 = Radiobutton(a, text="Order 0", variable=var, value=0,command=sel)
        R1.pack( anchor = W )

        R2 = Radiobutton(a, text="Order 1", variable=var, value=1,command=sel)
        R2.pack( anchor = W )

        R3 = Radiobutton(a, text="Order 2", variable=var, value=2,command=sel)
        R3.pack( anchor = W)

        label = Label(a)
        label.pack()
        
        
        L1 = Label(a, text="other")
        L1.pack( side = LEFT)
        E1 = Entry(a, bd =5, command=printEntry)

        E1.pack(side = RIGHT)
        selection=E1.get()
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

root.mainloop()

