import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
import PIL.Image as Image
import tifwork
import sys
sys.path.append('./GUI/')
import imageGUI
#import scipy.signal as sig

'''
def plot(data,title):
    
    plot.i = plot.i + 1
    plt.subplot(3,2,plot.i)
    plt.imshow(data)
    plt.gray() 
    plt.title(title)
    

plot.i = 0
'''

def getData(fileName, num):
    #get dataset
    dataset = tifwork.openTIF(fileName)

    #get details of dataset
    (cols,rows,bands,bandArray) = tifwork.detailsTIF(dataset)

    #get all bands
    bandArray = tifwork.getBand(dataset,bands,bandArray)

    #input a band

    workData = bandArray[:,:,num-1]

    #show original image and plot it
    imdata = Image.fromarray(workData)
    imdata = imdata.convert('L')
    imdata.save('original.jpg')
    imageGUI.imdisplay('original.jpg','Original',1)  
    #plot(workData,'Original')
    
    return workData
    #print workData
    #print bandArray

#get kernel
def getKernel():
    print 'Input Size of Kernel'
    inp = raw_input()
    kernel_size = int(inp)
    kernel = np.zeros((kernel_size,kernel_size),dtype = float)

    print 'Enter kernel elements in matrix form'

    for i in range(0,kernel_size):
        for j in range(0,kernel_size):

            kernel[i,j] = float(raw_input())
   
    print 'Input Kernel is'
    print kernel
    
    return kernel

#getKernel()

def meanFilter(fileName,size,num): 
    workData = getData(fileName,num)
    kernel_size = size
    kernel = np.ones((kernel_size,kernel_size),dtype = float)
    
    print kernel
    kernel = kernel / (kernel_size**2)
   
    meanFilter = ndimage.convolve(workData, kernel,cval =1.0)
    print 'Mean Filter'
    
    meanFilter1 = 2 * workData - meanFilter
    
    mfSave = Image.fromarray(meanFilter)
    mfSave1 = Image.fromarray(meanFilter1)
    
    mfSave = mfSave.convert('1')
    mfSave1 = mfSave1.convert('1')

    mfSave.save('Mean Filter.jpg')
    mfSave1.save('Mean Filter1.jpg')
    imageGUI.imdisplay('Mean Filter.jpg','Mean Filter',1)
    imageGUI.imdisplay('Mean Filter1.jpg','Mean Filter1',1)

def medianFilter(fileName,size,num):
    workData = getData(fileName,num)    
    print 'Input filter size'
    #size = int(raw_input())
    medFilter = ndimage.median_filter(workData,size)
    mfSave = Image.fromarray(medFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('Median Filter.jpg')
    imageGUI.imdisplay('Median Filter.jpg','Median Filter',1)
   # print 'med filter' , medFilter[100,:]

def gaussFilter(fileName,sigma,num):
    workData = getData(fileName,num)    
    print 'INput sigma'
    #sigma = float(raw_input())
    gauFilter = ndimage.gaussian_filter(workData,sigma)
    mfSave = Image.fromarray(gauFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('Gauss Filter.jpg')
    imageGUI.imdisplay('Gauss Filter.jpg','Guass Filter',1)

def sobelFilter(fileName,num):
    workData = getData(fileName,num)
    sobFilter = ndimage.sobel(workData)
    mfSave = Image.fromarray(sobFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('Sobel Filter.jpg')
    imageGUI.imdisplay('Sobel Filter.jpg','Sobel Filter',1)
def laplaceFilter(fileName,num):

    workData = getData(fileName,num)
    lapFilter = ndimage.laplace(workData)
    lapFilter = workData + lapFilter
    mfSave = Image.fromarray(lapFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('Laplace Filter.jpg')
    imageGUI.imdisplay('Laplace Filter.jpg','Laplace Filter',1)
#High Pass Filters

def fourierFilter(fileName,sigma,num):
    workData = getData(fileName,num)
    print 'INput sigma'
    #sigma = float(raw_input())
    fourFilter1 = ndimage.fourier_uniform(workData,sigma)
    fourFilter = ndimage.fourier_uniform(fourFilter1,sigma)
    mfSave = Image.fromarray(fourFilter)
    mfSave = mfSave.convert('L')
    mfSave.save('Fourier Filter.jpg')
    imageGUI.imdisplay('Fourier Filter.jpg','Fourier Filter',1)
# user defined
def filterUser(fileName,kernel,num):
    workData = getData(fileName,num)
    
    userFil = ndimage.convolve(workData,kernel)
    imsave = Image.fromarray(userFil)
    imsave = imsave.convert('1')
    imsave.save('User defined kernel.jpg')
    imageGUI.imdisplay('User defined kernel.jpg','User defined kernel',1)

# HIGH PASS PREDEFINED

def hpfEmbossE(fileName,num):
    workData = getData(fileName,num)
    kernel = np.array([[0,0,0],
                      [1,0,-1],
                      [0,0,0]],dtype = float)
    eeFilter = ndimage.convolve(workData, kernel)
    mfSave = Image.fromarray(eeFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('Emboss East Filter.jpg')
    imageGUI.imdisplay('Emboss East Filter.jpg','Emboss East Filter',1)

def hpfEmbossW(fileName,num):
    workData = getData(fileName,num)
    kernel = np.array([[0,0,0],
                      [-1,0,1],
                      [0,0,0]],dtype = float)
    eeFilter = ndimage.convolve(workData, kernel)
    mfSave = Image.fromarray(eeFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('Emboss West Filter.jpg')
    imageGUI.imdisplay('Emboss West Filter.jpg','Emboss West Filter',1)

def hpfEdgeDetect(fileName,num):
    workData = getData(fileName,num)
    kernel = np.array([[-1,-1,-1],
                      [-1,9,-1],
                      [-1,-1,-1]],dtype = float)
    eeFilter = ndimage.convolve(workData, kernel)
    mfSave = Image.fromarray(eeFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('Edge Detect Filter.jpg')
    imageGUI.imdisplay('Edge Detect Filter.jpg','Edge Detect Filter',1)

def hpfN(fileName,num):
    workData = getData(fileName,num)
    kernel = np.array([[1,1,1],
                      [1,-2,1],
                      [-1,-1,-1]],dtype = float)
    eeFilter = ndimage.convolve(workData, kernel)
    mfSave = Image.fromarray(eeFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('North.jpg')
    imageGUI.imdisplay('North.jpg','North',1)

def hpfNE(fileName,num):
    workData = getData(fileName,num)
    kernel = np.array([[1,1,1],
                      [-1,-2,1],
                      [-1,-1,1]],dtype = float)
    eeFilter = ndimage.convolve(workData, kernel)
    mfSave = Image.fromarray(eeFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('NorthE.jpg')
    imageGUI.imdisplay('NorthE.jpg','NorthE',1)
def hpfE(fileName,num):
    workData = getData(fileName,num)
    kernel = np.array([[-1,1,1],
                      [-1,-2,1],
                      [-1,1,1]],dtype = float)
    eeFilter = ndimage.convolve(workData, kernel)
    mfSave = Image.fromarray(eeFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('East.jpg')
    imageGUI.imdisplay('East.jpg','East',1)
def hpfSE(fileName,num):
    workData = getData(fileName,num)
    kernel = np.array([[-1,-1,1],
                      [-1,-2,1],
                      [-1,1,1]],dtype = float)
    eeFilter = ndimage.convolve(workData, kernel)
    mfSave = Image.fromarray(eeFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('SouthE.jpg')
    imageGUI.imdisplay('SouthE.jpg','SouthE',1)
def hpfS(fileName,num):
    workData = getData(fileName,num)
    kernel = np.array([[-1,-1,-1],
                      [1,-2,1],
                      [1,1,1]],dtype = float)
    eeFilter = ndimage.convolve(workData, kernel)
    mfSave = Image.fromarray(eeFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('South.jpg')
    imageGUI.imdisplay('South.jpg','South',1)
def hpfSW(fileName,num):
    workData = getData(fileName,num)
    kernel = np.array([[1,-1,-1],
                      [1,-2,-1],
                      [1,1,1]],dtype = float)
    eeFilter = ndimage.convolve(workData, kernel)
    mfSave = Image.fromarray(eeFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('SouthW.jpg')
    imageGUI.imdisplay('SouthW.jpg','SouthW',1)
def hpfW(fileName,num):
    workData = getData(fileName,num)
    kernel = np.array([[1,1,-1],
                      [1,-2,-1],
                      [1,1,-1]],dtype = float)
    eeFilter = ndimage.convolve(workData, kernel)
    mfSave = Image.fromarray(eeFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('West.jpg')
    imageGUI.imdisplay('West.jpg','West',1)
def hpfNW(fileName,num):
    workData = getData(fileName,num)
    kernel = np.array([[1,1,1],
                      [1,-2,-1],
                      [1,-1,-1]],dtype = float)
    eeFilter = ndimage.convolve(workData, kernel)
    mfSave = Image.fromarray(eeFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('NorthW.jpg')
    imageGUI.imdisplay('NorthW.jpg','NorthW',1)


def hpfPrewitt(fileName,num):

    workData = getData(fileName,num)
    preFilter = ndimage.prewitt(workData)
    mfSave = Image.fromarray(preFilter)
    mfSave = mfSave.convert('1')
    mfSave.save('Prewitt Filter.png')
    imageGUI.imdisplay('Prewitt Filter.png','Prewitt',1)

