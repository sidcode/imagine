import math
from osgeo import gdal
import PIL.Image as Image
import numpy as np
import math
import sys
import scipy.misc
sys.path.append('./GUI/')
import imageGUI

#linearly enhances an array from its minimum to maximum value.
def linearx(array):
    array1=np.array(array,'uint16')
    min=np.amin(array1)
    max=np.amax(array1)
    array1=((array1-min)*255)/((max-min))
    return array1

#creates and displays the NDVI image for the two bands entered
def goNDVI(array1,array2):   
    print 'NDVI'
    array1=np.array(array1,'float32') 
    array2=np.array(array2,'float32')
    num=array1-array2
    den=array1+array2    
    index  = (den>0)
    index1 = (den==0)
    num1=num[index]
    den1=den[index]
    output=num1/den1
    final=array1
    final[index]=output
    final[index1]=0
    #print index
    final=linearx(final)    
    #print final.shape
    
    scipy.misc.imsave('temp/Spectral/ndvi.png',final)
    imageGUI.imdisplay('temp/Spectral/ndvi.png','NDVI-Image',1)
    '''
    im=Image.fromarray(final)
    im = im.convert('L')
    im.save('ndvi'+str(count1)+'.png')
    #count1=count1+1
    #return final
    '''

#creates and displays the TVI image for the two bands entered
def goTVI(array,arrayz):   
    print 'TVI'
    array1=np.array(array,'float32') 
    array2=np.array(arrayz,'float32')
    num=array1-array2
    den=array1+array2    
    index=(den >0)
    index1=(den ==0)
    num1=num[index]
    den1=den[index]
    output=(((num1/den1) + 0.5)**0.5)*100
    final=array1
    final[index]=output
    final[index1]=0
    final=linearx(final)
    scipy.misc.imsave('temp/Spectral/tvi.png',final) 
    imageGUI.imdisplay('temp/Spectral/tvi.png','TVI-Image',1)    
    '''
    im=Image.fromarray(final)
    im = im.convert('L')
    im.save('tvi'+str(count1)+'.png')
    #count1=count1+1
    #return final
    '''

def goRVI(array,arrayz):   
    print 'RVI'
    array1=np.array(array,'float32') 
    array2=np.array(arrayz,'float32')
    num=array1
    den=array2    
    index=den >0
    index1=den ==0
    num1=num[index]
    den1=den[index]
    output=num1/den1
    final=array1
    final[index]=output
    final[index1]=0
    scipy.misc.imsave('temp/Spectral/ri.png',final) 
    imageGUI.imdisplay('temp/Spectral/ri.png','RI-Image',1)
    '''
    final=linearx(final) 
    im=Image.fromarray(final)
    im = im.convert('L')
    im.save('rvi'+str(count1)+'.png')
    #count1=count1+1
    #return final
    '''
    
#gets details about the number of rows ,columns ,bands and the array of bands for the file opened
#calls the function accordingly
def spec(fileName,num,no1,no2): 

	gdal.AllRegister()
	dataset =gdal.Open(fileName,gdal.GA_ReadOnly)
	if dataset is None:
	    print 'Could Not Open' + fileName
	    #Alternatively Raise an Event here
	    sys.exit(1)
	cols = dataset.RasterXSize
	rows = dataset.RasterYSize
	bands = dataset.RasterCount	
	dic = {1:goNDVI , 2 : goTVI , 3:goRVI}	
	band1=dataset.GetRasterBand(no1)
	band2=dataset.GetRasterBand(no2)
	array1=band1.ReadAsArray()	
	array2=band2.ReadAsArray()	
	dic[num](array1,array2)	

		        
