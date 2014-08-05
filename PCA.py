from PIL import Image
import numpy
import pylab
#from PIL import Image
from numpy import *
import tifwork as tw
import scipy.misc
import sys
sys.path.append('../GUI/')
import imageGUI
def pca(fileName):
	dataset = tw.openTIF(fileName)
	cols, rows,bands,bandArray = tw.detailsTIF(dataset)
	bandArray = tw.getBand(dataset,bands,bandArray)
	print bands
	for i in range(0,bands):

		array = bandArray[:,:,i]
		#print array
		scipy.misc.imsave('./temp/PCA/test'+str(i)+'.png',array)

	imlist = []
	for i in range(0,bands):
		imlist.append('./temp/PCA/test'+str(i)+'.png')
	print imlist

	def pca(X):
	  # Principal Component Analysis
	  # input: X, matrix with training data as flattened arrays in rows
	  # return: projection matrix (with important dimensions first),
	  # variance and mean

	  #get dimensions
	  num_data,dim = X.shape

	  #center data
	  mean_X = X.mean(axis=0)
	  for i in range(num_data):
	      X[i] -= mean_X

	  if dim>100:
	      print 'PCA - compact trick used'
	      M = dot(X,X.T) #covariance matrix
	      print M
	      e,EV = linalg.eigh(M) #eigenvalues and eigenvectors
	      print e 
	      print EV
	      tmp = dot(X.T,EV).T #this is the compact trick
	      V = tmp[::-1] #reverse since last eigenvectors are the ones we want
	      S = sqrt(e)[::-1] #reverse since eigenvalues are in increasing order
	  else:
	      print 'PCA - SVD used'
	      U,S,V = linalg.svd(X)
	      V = V[:num_data] #only makes sense to return the first num_data

	  #return the projection matrix, the variance and the mean
	  return V,S,mean_X



	im = numpy.array(Image.open(imlist[0])) #open one image to get the size
	m,n = im.shape[0:2] #get the size of the images
	imnbr = len(imlist) #get the number of images

	#create matrix to store all flattened images
	immatrix = numpy.array([numpy.array(Image.open(imlist[i])).flatten() for i in range(imnbr)],'f')

	#perform PCA
	V,S,immean = pca(immatrix)

	#mean image and first mode of variation
	immean = immean.reshape(m,n)

	for i in range (0,bands):
		mode = V[i].reshape(m,n)
		scipy.misc.imsave('./temp/PCA/pca'+str(i+1)+'.png',mode)
		x = imageGUI.imdisplay('./temp/PCA/pca'+str(i+1)+'.png','PCA '+str(i),1)

	#show the images

	scipy.misc.imsave('./temp/PCA/meanimage.png',immean)
	imageGUI.imdisplay('./temp/PCA/meanimage.png','Mean Image',1)

