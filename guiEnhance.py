'''
The software aims to be an open-source package with basic, and advanced Image Processing features.
Copyright (C) 2014	Indian Institute of Remote Sensing, Dehradun

The original authors of this program (in alphabetical order) are:

---------------------------------------------------------------------------------------------------------------------------------------
Sno.		NAME											Email( AT gmail DOT com)			Role(s)
---------------------------------------------------------------------------------------------------------------------------------------
1.				Shalaka Somani							shalaka195										GUI, Spectral
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
import ttk
import matrix
import tkFileDialog
from PIL import Image
import tkMessageBox
#import spatial as sp
import sys
sys.path.append('./PCA')
import PCA
import contrast
import Spectral as spec
import tifwork
import spatial as spat
global box
global guiSpat4
global guiSpat3

#defines the main GUI for image enhancement

def guiEn():
	global fileName
	fileName = ''

	frame=tk.Tk()

	frame1=tk.Frame(frame)
	frame.title("Image Enhancement")

	def open():

	    global fileName
	    fileName=tkFileDialog.askopenfilename(filetypes=[('tiff file','*.tif')])

	    if(fileName == ''):
		tkMessageBox.showerror("Error", "Please select an image.")
		return
	    else:
		print(fileName)


#GUI for Spectral Analysis 		

	def guiSpectral():
	    frame.destroy()
	    guiSpec=tk.Tk()
	    guiSpec.title("Spectral Analysis")

	    menuBar = tk.Menu(guiSpec)
	    guiSpec['menu'] = menuBar
	    subMenu1 = tk.Menu(menuBar)

	    menuBar.add_command(label='Open',  command=open)
	    menuBar.add_command(label='Close', command=guiSpec.destroy)

	    frameSpec=tk.Frame(guiSpec, width=200, height=200)
	    
	    x1=tk.Label(frameSpec, text="Spectral Analysis")
	    x1.pack(side=tk.TOP, pady = 5 , padx = 5 )

	    def goSpectral(x):
		
		global fileName
		if(fileName == ''):
		    tkMessageBox.showerror("Error", "Please select an image.")
		    open()
		    return
		else:
			dic = {	1: PCA.pca , 2: spec.spec , 3: spec.spec , 4: spec.spec}
			if (x == 1):
				dic[x](fileName)	    
			else:
				
				
			
				def indices():
					i = opt1.get()
					j = int(i)
					i = opt2.get()
					k = int(i)
					frameSpec1.destroy()
					frameSpec2.destroy()
					frameSpec3.destroy()
				 	dic[x](fileName,x-1,j,k)
						
				frameSpec1=tk.Frame(frameSpec)
				frameSpec2=tk.Frame(frameSpec)
				frameSpec1.pack()
				frameSpec2.pack()
				frameSpec3= tk.Frame(guiSpec)
				frameSpec3.pack()
				dataset = tifwork.openTIF(fileName)
				(cols,rows,bands,bandArray) = tifwork.detailsTIF(dataset)

				optionList=[]
				for k in range(1, bands+1):
					optionList.append(k)

				lab1=tk.Label(frameSpec1, text="Band Number 1: ")
				lab1.pack(side=tk.LEFT, padx=2, pady=2)
				opt1= ttk.Combobox(frameSpec1,values=optionList, width=5)
				opt1.pack(side = tk.LEFT , pady = 5,padx = 5 )


				lab2=tk.Label(frameSpec2, text="Band Number 2: ")
				lab2.pack(side=tk.LEFT, padx=2, pady=2)

				opt2= ttk.Combobox(frameSpec2,values=optionList, width=5)
				opt2.pack(side = tk.LEFT , pady = 5,padx = 5 )

				button=tk.Button(frameSpec3, text="Go", command=indices)
				button.pack(side=tk.BOTTOM, padx=2, pady=2)
		
	    
	    button1=tk.Button(frameSpec, text="PCA", command=lambda : goSpectral(1))
	    button1.pack(side=tk.TOP, padx=2, pady=2)
	    button2=tk.Button(frameSpec, text="NDVI", command=lambda:goSpectral(2))
	    button2.pack(side=tk.TOP, padx=2, pady=2)
	    button3=tk.Button(frameSpec, text="TVI", command=lambda:goSpectral(3))
	    button3.pack(side=tk.TOP, padx=2, pady=2 )
	    button4=tk.Button(frameSpec, text="RI", command=lambda:goSpectral(4))
	    button4.pack(side=tk.TOP, padx=2, pady=2 )
	    frameSpec.pack()

#GUI for Spatial Analysis 

	def guiSpatial():
	    frame.destroy()
	    guiSpat=tk.Tk()
	    guiSpat.title("Spatial Analysis")

	    menuBar = tk.Menu(guiSpat)
	    guiSpat['menu'] = menuBar
	    subMenu1 = tk.Menu(menuBar)

	    menuBar.add_command(label='Open',  command=open)
	    menuBar.add_command(label='Close', command=guiSpat.destroy)
	    
	    x1=tk.Label(guiSpat, text="Spatial Analysis")
	    x1.pack(side=tk.TOP, pady = 5 , padx = 5 )

	    guiSpat1=tk.Frame(guiSpat)
	    guiSpat2=tk.Frame(guiSpat)
	    frameSpat1=tk.Frame(guiSpat1, width=200, height=200)
	    frameSpat2=tk.Frame(guiSpat1, width=200, height=200)
	    frameSpat3=tk.Frame(guiSpat, width=200, height=200)

	    def dest():
		global guiSpat3
		global guiSpat4
		guiSpat3.destroy()
		guiSpat4.destroy()
	    def destr():
		global guiSpat3
		guiSpat3.destroy()
		
#get the bands for enhancement		
	    def bandChoose():
        
		    global guiSpat3		    
		    guiSpat3=tk.Frame(guiSpat)
		    if(fileName == ''):
		    	tkMessageBox.showerror("Error", "Please select an image.")
		    	open()
		    	return
		    else:
			    if(opt1.get()=='' and opt2.get()==''):
			    	tkMessageBox.showerror("Error", "Please select an option.")
			    	return
			    elif(opt1.get()!='' and opt2.get()!=''):
			    	tkMessageBox.showerror("Error", "Please select only one option.")
			    	return
			    else:        

				global box    
				dataset = tifwork.openTIF(fileName)
				(cols,rows,bands,bandArray) = tifwork.detailsTIF(dataset)

				optionList=[]
				for k in range(1, bands+1):
					optionList.append(k)

				lab=tk.Label(guiSpat3, text="Band Number : ")
				lab.pack(side=tk.LEFT, padx=2, pady=2)
				box= ttk.Combobox(guiSpat3,values=optionList, width=5)
				box.pack(side = tk.LEFT , pady = 5,padx = 5 )
				button=tk.Button(guiSpat3, text="Go", command=goSpatial)
            			button.pack(side=tk.RIGHT, padx=2, pady=2)
				guiSpat3.pack(side=tk.TOP)
		    
	    def enterVariable(x,option,bandNum):
		global guiSpat4
		global fileName
		def spati(option):
			
			size = boxVar.get()
			size = int(size)
			#print option 
			#print size
			dic = {'Mean Filter':spat.meanFilter, 'Median Filter':spat.medianFilter, 'Fourier Filter':spat.fourierFilter, 'Gaussian Filter':spat.gaussFilter}
			#print dic[option]
			dic[option](fileName,size,bandNum)
			dest()

		guiSpat4=tk.Frame(guiSpat)

		var=tk.Label(guiSpat4, text="Enter "+str(x))
		var.pack(side=tk.LEFT, padx=2, pady=2)
		boxVar=tk.Entry(guiSpat4)
		boxVar.pack(side=tk.LEFT, padx=2, pady=2)
		button=tk.Button(guiSpat4, text="Goooo",command= lambda : spati(option))
		button.pack(side=tk.LEFT, padx=2, pady=2)

		
		guiSpat4.pack(side=tk.TOP)

 	    def goSpatial():
		global fileName
	
	    
	    	print(fileName)
    		

		bandNum = box.get()
		bandNum = int(bandNum)
		dic1 = { 'User Defined Kernel':matrix.test,   'Laplace Filter':spat.laplaceFilter}
		dic2 = {'Emboss East':spat.hpfEmbossE,'Sobel Filter':spat.sobelFilter, 'Emboss West':spat.hpfEmbossW, 'Edge Detect':spat.hpfEdgeDetect, 'Prewitt':spat.hpfPrewitt, 'High Pass North':spat.hpfN, 'High Pass Northeast':spat.hpfNE, 'High Pass East':spat.hpfE, 'High Pass Southeast':spat.hpfSE, 'High Pass South':spat.hpfS, 'High Pass Southwest':spat.hpfSW, 'High Pass West':spat.hpfW, 'High Pass Northwest':spat.hpfNW}
		
		option1 = opt1.get()
		option2 = opt2.get()
	            		
		if (option1 == ''):
			if (option2 != ''):				
								
				print option2
				dic2[option2](fileName,bandNum)
				destr()
		else:
			if(option1== 'Mean Filter' or option1== 'Median Filter'):
	            		enterVariable('Filter Size',option1,bandNum)


	        	elif(option1== 'Fourier Filter' or option1== 'Gaussian Filter'):
				enterVariable('Sigma',option1,bandNum)
				
			else:
				if (option1 == 'User Defined Kernel'):
					dic1[option1]()
				else:
					dic1[option1](fileName,bandNum)
				destr()
			

	    optionList1=['','User Defined Kernel', 'Mean Filter', 'Median Filter', 'Gaussian Filter',  'Laplace Filter', 'Fourier Filter']
	    
	    x1=tk.Label(frameSpat1, text="Low Pass Filter")
	    x1.pack(side=tk.TOP, pady = 5 , padx = 5 )
	    opt1= ttk.Combobox(frameSpat1,values=optionList1, width=20)
	    opt1.pack(side = tk.TOP , pady = 5,padx = 5 )
	    
	    optionList2=['','Emboss East', 'Emboss West', 'Edge Detect', 'Prewitt', 'High Pass North','Sobel Filter', 'High Pass Northeast', 'High Pass East', 'High Pass Southeast', 'High Pass South', 'High Pass Southwest', 'High Pass West', 'High Pass Northwest']

	    x2=tk.Label(frameSpat2, text="High Pass Filter")
	    x2.pack(side=tk.TOP, pady = 5 , padx = 5 )
	    opt2= ttk.Combobox(frameSpat2,values=optionList2, width=20)
	    opt2.pack(side = tk.TOP , pady = 5,padx = 5 )

	    
	    button1=tk.Button(guiSpat1, text="Choose Band", command=bandChoose)
    	    button1.pack(side=tk.BOTTOM, padx=2, pady=2)
	       
	    frameSpat1.pack(side=tk.LEFT, padx=2, pady=2)
	    frameSpat2.pack(side=tk.LEFT, padx=2, pady=2)
	    guiSpat1.pack(side=tk.TOP)
	    frameSpat3.pack(side=tk.TOP, padx=2, pady=2)
	    guiSpat2.pack(side = tk.BOTTOM)

	    
	def guiContrast():
		frame.destroy()
		guiCont=tk.Tk()
		guiCont.title("Contrast Analysis")

		menuBar = tk.Menu(guiCont)
		guiCont['menu'] = menuBar
		subMenu1 = tk.Menu(menuBar)

		menuBar.add_command(label='Open',  command=open)
		menuBar.add_command(label='Close', command=guiCont.destroy)

	       
		frameCont=tk.Frame(guiCont, width=200, height=200)
		
		x1=tk.Label(frameCont, text="Contrast Analysis")
		x1.pack(side=tk.TOP, pady = 5 , padx = 5 )
		def pwrun():
		    import piecewise_guiFinal
		
		def herun():
			import histequalfinal

		def goContrast(x):
		
		    global fileName
		    if(fileName == ''):
		        tkMessageBox.showerror("Error", "Please select an image.")
			open()
		        return
		    else:
		        print(fileName)
			contrast.cont(fileName,x)	
	
		button3=tk.Button(frameCont, text="Linear", command=lambda:goContrast(1))
		button3.pack(side=tk.TOP, padx=2, pady=2 )		       
		button1=tk.Button(frameCont, text="Logarithmic", command=lambda:goContrast(2))
		button1.pack(side=tk.TOP, padx=2, pady=2)
		button2=tk.Button(frameCont, text="Exponential", command=lambda:goContrast(3))
		button2.pack(side=tk.TOP, padx=2, pady=2)
		button4=tk.Button(frameCont, text="Piece Wise", command=pwrun)
		button4.pack(side=tk.TOP, padx=2, pady=2 )
		button5=tk.Button(frameCont, text="Histogram Equilization", command=herun)
		button5.pack(side=tk.TOP, padx=2, pady=2 )
		
		frameCont.pack()    





	x1=tk.Label(frame1, text="Image Enhancement")
	x1.pack(side=tk.TOP, pady = 5 , padx = 5 )

	button1=tk.Button(frame1, text="Spatial", command=guiSpatial)
	button1.pack(side=tk.TOP, padx=2, pady=2)
	button2=tk.Button(frame1, text="Spectral", command=guiSpectral)
	button2.pack(side=tk.TOP, padx=2, pady=2)
	button3=tk.Button(frame1, text="Contrast", command=guiContrast)
	button3.pack(side=tk.TOP, padx=2, pady=2 )

	frame1.pack(padx=20, pady=20)

	frame.mainloop()
