from PIL import Image
import scipy.misc
import tifwork
import numpy as np
from sklearn import svm
import sys
sys.path.append('../GUI/')
import imageGUI

def svmwork(fileName,data,target,typ):
	print 'SVM'
	dataset = tifwork.openTIF(fileName)

	(cols,rows,bands,bandArr) = tifwork.detailsTIF(dataset)

	bandArr = tifwork.getBand(dataset,bands,bandArr)


	imageArray = np.array(bandArr,dtype =float)

	print imageArray.shape

	array = imageArray.copy()

	array = array.reshape((cols*rows),bands)

	#print array.shape


	# training data extract
	
	# classifying training data
	


	#print target.shape
	#print data.shape
	#print array.shape

	# SVM
	if (typ == 'poly'):
		clf = svm.SVC(kernel=typ,degree=3)
	else:
		clf = svm.SVC(kernel=typ)	

	clf.fit(data, target) 

	isoarr = clf.predict(array)

	isoarr  = np.array(isoarr,dtype =int)
	#print isoarr

	#print isoarr.max()


	#print z.shape
	#print z


	colorArray=np.array([[0,0,100],[100,0,0],[0,100,0],[100,100,0],[75,75,75],[0,100,100],[100,0,100],[50,25,25],[25,50,25],[25,25,50]])
	clusteredArray = np.zeros((rows*cols,3))
	#print clusteredArray.shape
	clusters = isoarr.max()

	#print clusters
	for i in xrange(clusters+1):
		indices = np.where(isoarr == i)[0]
		print i ,indices.size
		if indices.size:
			clusteredArray[indices] = colorArray[i]


	print clusteredArray
	clusteredArray = clusteredArray.reshape(rows,cols,3)

	#print clusteredArray
	
	scipy.misc.imsave('svm'+typ+'.jpg',clusteredArray)
	imageGUI.imdisplay('svm'+typ+'.jpg','SVM-'+typ+'-Image')
	print 'SVM Done'

