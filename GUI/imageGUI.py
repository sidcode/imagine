
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

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.figure import Figure
import matplotlib.cm as cm
#from tkFileDialog import askopenfilename

# implement the default mpl key bindings
#import Image, ImageTk

   
def imdisplay(filename,title,x=0):
    openImFile(filename,title,x)

def openImFile(filename,title,x):
    Root1 = tk.Tk()
    Root1.wm_title(title)
    Root1.geometry("600x600")
    fx = Figure(figsize=(5,4), dpi=100)
    ax = fx.add_subplot(111)
    img=mpimg.imread(filename)
    if (x == 0):
	    ax.imshow(img)
    else:
    	    ax.imshow(img,cmap = cm.Greys_r)
    
    canvasx = FigureCanvasTkAgg(fx, master=Root1)
    canvasx.draw()
    canvasx.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    toolbar = NavigationToolbar2TkAgg( canvasx, Root1 )
    toolbar.update()
    canvasx._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def on_key_event(event):
        print('you pressed %s'%event.key)
        key_press_handler(event, canvasx, toolbar)
       	
    def _quitx():
        Root1.quit()     # stops mainloop
        Root1.destroy()
        button1 = tk.Button(master=Root1, text='Quit', command=_quitx)
        button1.pack(side=tk.BOTTOM)
        
    fx.canvas.mpl_connect('key_press_event', on_key_event)
    

# a tk.DrawingArea
