from spectral import kmeans
from PIL import Image
import scipy.misc
import tifwork
import numpy as np
import sys
sys.path.append('../GUI/')
import imageGUI

def kmea(colorArray,iterations,fileName):
	print 'Kmeans'
	
	print colorArray
	print iterations
	print fileName
	dataset = tifwork.openTIF(fileName)

	(cols,rows,bands,bandArr) = tifwork.detailsTIF(dataset)

	bandArr = tifwork.getBand(dataset,bands,bandArr)


	imageArray = np.array(bandArr,dtype =float)

	clusters = len(colorArray)
	print 'clusters = ' , clusters
	#iterations = 3

	(clusterNumber, colorArr) = kmeans(imageArray,clusters,iterations)

	#print colorArray.shape
	#print clusterNumber
	
	clusteredArray = np.zeros((rows,cols,3))

	for i in range(clusters):
	    index = clusterNumber == i
	    clusteredArray[index] = colorArray[i]

	
	scipy.misc.imsave('kMeans.jpg',clusteredArray)

	imageGUI.imdisplay('kMeans.jpg','Kmeans-Image')
	print 'kmeans done'
