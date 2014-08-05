from Tkinter import *
import tkMessageBox
import tkFileDialog
import math
import numpy
import tkColorChooser
import sys
sys.path.append('./K-means')
import kmeanswork as km
import numpy as np
sys.path.append('./ISODATA')
import isodata as iso
sys.path.append('./fuzzy')
import fuzzy as fz
filename=''
iteration=0

def unsuper(no):
  global filename	
  global iteration  
  global box1
  global root
  root=Tk()
  root.geometry('350x350')
  root.title('Unsupervised Classification')
  count=0
  global i
  i=0
  global text
  text=0
  global clustervalue,add2
  clustervalue=numpy.array([])
  global l1,l2,l3,hexc,rgb

  global clusterarray
  clusterarray=[]

  global colorArr
  colorArr = []

  global className
  className = []
  
 

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
    global hexcsp
    global i
    global rgb
    hexc='hexc'+str(i+1)
    
    (rgb,hexc)=tkColorChooser.askcolor()
    #print hexc
    #print rgb
    l3.configure(bg=hexc)
    
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
    global clustervalue
    global l2
    global clusterarray
    global box1
    global rgb
    global colorArr
    global className
    global iteration
    cname=l2.get()
    #print cname
	
    className.append(cname)
    clustervalue=[i,cname,rgb]
    colorArr.append(rgb)
    #print clustervalue
    #print colorArr
    clusterarray.append(clustervalue)
    i=i+1
    iterationnum=box1.get()
    clusternum=i

    #print "No. of Iterations: ",iterationnum
    #print "No. of Clusters: ",clusternum
    
    #print clusterarray

    
    def changecolor2():
      global rgb
      global hexc
      global i
      rgb='rgb'+str(i+1)
      hexc='hexc'+str(i+1)
      (rgb,hexc)=tkColorChooser.askcolor()
      #print rgb
      l3.configure(bg=hexc)


    
    outerframe='outerframe'+str(i+1)
    #print outerframe
    l1='l1'+str(i+1)
    l2='box'+str(i+1)
    l3='colorchooser'+str(i+1)
    outerframe=Frame(frame2)
    l1=Label(outerframe,text=str(i+1),width=10)
    l1.pack(side=LEFT)

    l2=Entry(outerframe,width=5)
    l2.pack(side=LEFT)
    l3=Button(outerframe,text='Color',command=changecolor2,width=10)
    l3.pack(side=LEFT)
    outerframe.pack(side=TOP)
   

  #print i  
  def setiter():
    global iteration
    text=box1.get()
    a=len(text)
    if a == 0 :
      tkMessageBox.showerror('Error','Enter  value !')
      pass
    else:
      print text
      iteration=int(text)
      
      outerframe=numpy.array([])
      innerframe1=numpy.array([])
      colorbox=numpy.array([])



  def unsupervised():
	global filename
	global iteration
	print colorArr
	print className
	print filename
	if (filename == ''):
		browse()
		
	if (no == 1):
		km.kmea(colorArr,iteration,filename)
	if (no == 2):
		x = {'K':len(colorArr) , 'I':iteration}
		iso.isoclass(filename, colorArr,x)
	if (no == 3):
		fz.fuzz(colorArr,filename)
	
         
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
  showimg=Button(root,text='Display Image',command= unsupervised)
  showimg.pack()


#number of iterations
  framec=Frame(root)
  lnumiter=Label(framec,text='Enter Number of Iterations :',padx=10,pady=10)
  lnumiter.pack(side=LEFT)

  box1=Entry(framec,width=5)
  box1.pack(side=LEFT)

  submitnum=Button(framec,text='Go',command=setiter)
  submitnum.pack(side=LEFT)
  framec.pack(side=TOP)

  #creating labels
  frame1=Frame(root)
  lu=Label(frame1,text='Cluster No.',width=10)
  lu.pack(side=LEFT)
  lu1=Label(frame1,text='Name',width=10)
  lu1.pack(side=LEFT)

  lu2=Label(frame1,text='Color Code',width=10)
  lu2.pack(side=LEFT)

  frame1.pack(side=TOP)

  global frame2
  frame2=Frame(root)
  #print text

  global arrayvalue

  arrayvalue=numpy.array([])


  outerframe='outerframe'+str(i+1)
  #print outerframe
  l1='l1'+str(i+1)
  l2='box'+str(i+1)
  l3='colorchooser'+str(i+1)
  outerframe=Frame(frame2)
  l1=Label(outerframe,text=str(i+1),width=10)
  l1.pack(side=LEFT)

  l2=Entry(outerframe,width=5)
  l2.pack(side=LEFT)
  l3=Button(outerframe,text='Color',command=changecolor,width=10)
  l3.pack(side=LEFT)
  outerframe.pack(side=TOP)

    
  frame2.pack(side=TOP)


  #submit value
  framebutton=Frame(root,pady=30)
  global add
  add=Button(framebutton,text='Add',command=addfield)
  add.pack(side=LEFT)
  #stopaddition=Button(framebutton,text='End Addition',command=endfield)
  #stopaddition.pack(side=LEFT)
  framebutton.pack(side=TOP)
  iterationnum=l2.get()
  clusternum=i

  #print "No. of Iterations: ",iterationnum
  #print "No. of Iterations: ",clusternum
  root.mainloop()
  

