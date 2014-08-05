from PIL import Image
import numpy as np
import pylab
#from PIL import Image
import random
import tifwork as tw
import scipy.misc



def initCentroids(Dataset,K,z):
	init_centroid = np.zeros((K,z))
	for i in range(0,K):
		j = random.choice(Dataset)
		init_centroid[i,:] = j
	return init_centroid

def kmeans(Dataset,K,initial_centroid):
	(nos,z) = Dataset.shape

	idx = np.zeros((row*col),float)
	dis = np.zeros(z,float) 
	for i in range(0,nos):
		for j in range(0,K):		
			dis = (initial_centroid[j,:] - Dataset[i,:])**2
			dist = 0
			for k in range(0,z):
				dist += dis[k]
			if( j == 0):
				minimum = dist
				idx[i] = j			
			elif (dist < minimum):
				minimum = dist
				idx[i] = j

	centroid = newclus(K,nos,Dataset,idx)
	return (idx,centroid)

def newclus(K,nos,Dataset,idx):	
	centroid = np.zeros((K,z))
	for i in range(0,K):
		mean = [0,0,0]
		count = 0 
		for j in range(0,nos):
			if(idx[j] == i):
				mean = mean+Dataset[j]
				count+=1
		
		mean = mean/count				
		centroid[i,:] = mean		
	return centroid
			
Dataset = np.array(Image.open('good.jpg'),float)
(row,col,z) = Dataset.shape

arr2 = np.zeros(Dataset.shape,float)

Dataset = Dataset/255

# no of clusters
K = 4

#no of iters
iters = 3

Data_orig = Dataset
Dataset=Dataset.reshape(((row*col),z))
#print Dataset.shape


initial_centroid = initCentroids(Dataset,K,z)
#print initial_centroid

for q in range(0,iters):

	(idx,centroid)=kmeans(Dataset,K,initial_centroid)

print idx.max()

color = [(10,0,0),(0,25,0),(0,0,55),(10,10,10),(12,0,45),(34,65,0),(0,45,87),(100,100,100),(50,50,50),(12,54,77),(43,65,99)]
for i in range(0,(row*col)):
	
	Dataset[i] = color[int(idx[i])]

Dataset=Dataset.reshape(row,col,z)

print Dataset.shape
scipy.misc.imsave('kmeans.jpeg',Dataset)	

