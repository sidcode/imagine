from osgeo import gdal
import PIL.Image as Image
import numpy as np
import imageGUI
import scipy.misc

gdal.AllRegister()

def openTIF(filename):
    dataset =gdal.Open(filename,gdal.GA_ReadOnly)
    if dataset is None:
        print 'Could Not Open' + filename
        #Alternatively Raise an Event here
        sys.exit(1)

    return dataset

def detailsTIF(dataset):
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    bands = dataset.RasterCount
    bandArray = np.zeros((rows,cols,bands),dtype = float)
    return (cols, rows,bands,bandArray)

def getBand(dataset,bands,bandArr):
    for x in range(1,bands+1):
        band=dataset.GetRasterBand(x)
        array=band.ReadAsArray()
        bandArr[:,:,x-1] = array
    return bandArr


def selectBand(bandArray,rows,cols,ch1,ch2,ch3):

	ch1 = int(ch1)
	ch2 = int(ch2)
	ch3 = int(ch3)
	combi= np.zeros((rows,cols,3),'uint8')
	combi[:,:,0]=bandArray[:,:,ch1-1]
	combi[:,:,1]=bandArray[:,:,ch2-1]
	combi[:,:,2]=bandArray[:,:,ch3-1]
	combImage= Image.fromarray(combi)
	scipy.misc.imsave('fcc.jpg',combImage)
	imageGUI.imdisplay('fcc.jpg','False Colour Composite',1)
                

