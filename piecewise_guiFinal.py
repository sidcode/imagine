from osgeo import gdal
from Tkinter import *
import Tkinter as tk
import tkMessageBox
import tkFileDialog
from PIL import Image
import pylab
import hist

root=tk.Tk()
root.geometry('500x200')

root.title('Piecewise Contrast Enhancement')

filename=''
bandnum=''
band_chosen=''
def openimage():
  global filename
  global box1
  filename=tkFileDialog.askopenfilename(title='Choose Image File',filetypes=[('TIF Image','*.tif')])
  box1.destroy()
  labelfile=tk.Entry(frametop,width=35)
  labelfile.insert(0,filename)
  labelfile.pack(side=LEFT)

def bandsel():
  global band_chosen
  global entry_bb,bandbox
  band_chosen=int(entry_bb.get())
  
  print band_chosen
  bandbox.destroy()
  
def chooseband():
  global filename
  print filename
  if(filename == ''):
	tkMessageBox.showerror('Error','Image not selected.')
  else:
	global bandnum,bandbox  
	bandnum=hist.numbands(filename)
	print bandnum
	bandbox=tk.Tk()
	bandbox.title('Select Band')
	frame_bb=tk.Frame(bandbox)
	text_bb='Select Band : 1 -' +str(bandnum)
	l_bb=tk.Label(frame_bb,text=text_bb)
	l_bb.pack(side=tk.LEFT)
	global entry_bb
	entry_bb=tk.Entry(frame_bb)
	entry_bb.pack(side=tk.LEFT)
	
	selectbandbutton=tk.Button(frame_bb,text='Proceed',command=bandsel)
	selectbandbutton.pack(side=tk.BOTTOM)
	frame_bb.pack(side=tk.TOP)
	bandbox.mainloop() 

def displayinstruction():
  tkMessageBox.showinfo('Help','Click on "Select" button.Then click on a point in the histogram you want to enhance following the second point to specify the piece')   
    
def displayhist():
  global root	
  global filename	
  global band_chosen,bandnum
  if(filename != '' and band_chosen != ''):
      
	hist.showhist2(filename,root,band_chosen)	
	root.geometry('500x1000')
  
  else:
    tkMessageBox.showerror('Error','Image not selected')	  
# create a new figure
#figure()
# don't use colors
#gray()
# show contours with origin upper left corner
#contour(im, origin='image')
#axis('equal')
#axis('off')

frametop=tk.Frame(root,pady=10)
b1=tk.Button(frametop,text='Choose Image',command=openimage)
b1.pack(side=LEFT)

box1=tk.Entry(frametop,width=35)
box1.pack(side=LEFT)
box1.insert(0,'None')
frametop.pack(side=TOP)

frame1=tk.Frame(root,pady=10)

bband=tk.Button(frame1,text='Choose Band',padx=5,command=chooseband)
bband.pack(side=LEFT)
b2=tk.Button(frame1,text='Display Histogram',padx=5,command=displayhist)
b2.pack(side=LEFT)
b3=tk.Button(frame1,text='Instructions',padx=5,command=displayinstruction)
b3.pack(side=LEFT)
frame1.pack(side=TOP)

root.mainloop()
