'''
The software aims to be an open-source package with basic, and advanced Image Processing features.
Copyright (C) 2014	Indian Institute of Remote Sensing, Dehradun

The original authors of this script/ program (in alphabetical order) are:

---------------------------------------------------------------------------------------------------------------------------------------
Sno.		NAME											Email( AT gmail DOT com)			Role(s)
---------------------------------------------------------------------------------------------------------------------------------------

1.				Shalaka Somani							shalaka195										GUI
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

import Tkinter as tk
from tkMessageBox import *
import ttk
import tkFileDialog
from PIL import Image
import tifwork
import guiEnhance as sg
import guiClass as cg
import sys
import imageGUI

def exit():
    root.destroy()
    sys.exit()
    
def rectification():
    import rectest


def rgbselect():
    fileName=tkFileDialog.askopenfilename(filetypes=[('tiff file','*.tif')])
    if(fileName == ''):
         showerror("Error", "Please select an image.")
         return
    else:
        print(fileName)
        dataset = tifwork.openTIF(fileName)

    w=tk.Tk()

    def bandPrint():
        if(not(opt1.get() and opt2.get() and opt3.get())):
           showerror("Error", "All bands not selected")
        elif(opt1.get()==opt2.get() or opt1.get()==opt3.get() or opt2.get()==opt3.get()):
            showerror("Error", "Same bands selected")
        else:
            bandArr = tifwork.getBand(dataset,bands,bandArray)
            tifwork.selectBand(bandArr,rows,cols,opt1.get(),opt2.get(),opt3.get())
            w.destroy()
    
    mainframe = tk.Frame(w)
#    frame4.grid()
    frame2=tk.Frame(mainframe)
#    frame2.grid()
    frame3=tk.Frame(mainframe)
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
    mainframe.pack(side= tk.TOP, pady = 5 , padx = 5 )

    button = tk.Button(frame5, width=10, text="Display Image", command=bandPrint)
    button.pack(side = tk.TOP , pady = 5 , padx = 5 )
    frame5.pack(side=tk.TOP , pady = 5 , padx = 5 )
    
#opens the root window
root=tk.Tk()

root.title("Image Processing Software")

frame1 = tk.Frame(root, width=1000)

#to display the frame
frame1.pack()

#keeps only the frame
root.overrideredirect(0)
root.resizable(0,0)

photo3 = tk.PhotoImage(file="iirs.gif")
button3 = tk.Button(frame1, width=100, height=100,image=photo3)
button3.pack(side=tk.LEFT, padx=2, pady=2)

photo2 = tk.PhotoImage(file="display.gif")
button2 = tk.Button(frame1, width=100, height=100, image=photo2, command=rgbselect)
button2.pack(side=tk.LEFT, padx=2, pady=2)

#enhancement
photo4 = tk.PhotoImage(file="enhancement.gif")
button4 = tk.Button(frame1, width=100, height=100, image=photo4,command  = sg.guiEn)
button4.pack(side=tk.LEFT, padx=2, pady=2)

#classification
photo5 = tk.PhotoImage(file="classification.gif")
button5 = tk.Button(frame1, width=100, height=100, image=photo5 , command = cg.classgui)
button5.pack(side=tk.LEFT, padx=2, pady=2)

#rectification
photo6 = tk.PhotoImage(file="rectification.gif")
button6 = tk.Button(frame1, width=100, height=100, image=photo6, command=rectification )
button6.pack(side=tk.LEFT, padx=2, pady=2)

photo1 = tk.PhotoImage(file="close.gif")
button1 = tk.Button(frame1, width=100, height=100, image=photo1, command=exit)
button1.pack(side=tk.LEFT, padx=2, pady=2)

root.mainloop()
