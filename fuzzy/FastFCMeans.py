# Segment N-dimensional grayscale image into c classes using a memory 
# efficient implementation of the fuzzy c-means (FCM) clustering algorithm. 
# The computational efficiency is achieved by using the histogram of the 
# image intensities during the clustering process instead of the raw image
# data.
#
# INPUT ARGUMENTS:
#   - im  : N-dimensional grayscale image in integer format. 
#   - c   : positive interger greater than 1 specifying the number of
#           clusters. c=2 is the default setting. Alternatively, c can be
#           specified as a k-by-1 array of initial cluster (aka prototype)
#           centroids.
#   - q   : fuzzy weighting exponent. q must be a real number greater than
#           1.1. q=2 is the default setting. Increasing q leads to an
#           increased amount of fuzzification, while reducing q leads to
#           crispier class memberships.
#
# OUTPUT  :
#   - L   : label image of the same size as the input image. For example,
#           L==i represents the region associated with prototype C(i),
#           where i=[1,k] (k = number of clusters).
#   - C   : 1-by-k array of cluster centroids.
#   - U   : L-by-k array of fuzzy class memberships, where k is the number
#           of classes and L is the intensity range of the input image, 
#           such that L=numel(min(im(:)):max(im(:))).
#   - LUT : L-by-1 array that specifies the defuzzified intensity-class 
#           relations, where L is the dynamic intensity range of the input 
#           image. Specifically, LUT(1) corresponds to class assigned to 
#           min(im(:)) and LUT(L) corresponds to the class assigned to
#           max(im(:)). See 'apply_LUT' function for more info.
#   - H   : image histogram. If I=min(im(:)):max(im(:)) are the intensities
#           present in the input image, then H(i) is the number of image 
#           pixels/voxels that have intensity I(i). 
#


import numpy as np
import matplotlib.pyplot as plt
import tifwork as tw
import scipy.misc
import LUT2label as label
import FastCMeans as fc

def FastFCMeans(im, c, q):
    
    #intensity range

    Imin = float(np.min(im[:]))
    Imax = float(np.max(im[:]))
    I = np.transpose(np.array(np.arange(Imin,Imax+1)))
    
    I = I[:, np.newaxis]
    
    #print 'I size ', I.shape

    #print Imin, Imax

    # Compute intensity histogram
	
    H = np.histogram(im.flatten(),I.flatten())
    
    (H1, H2) = H
    
    #H1 = H1.flatten()
    #H2 = H2.flatten()
    
    H1 = H1[:, np.newaxis]
    H2 = H2[:, np.newaxis]
    
    #print 'H1 and H2 Size: ', H1.shape, H2.shape
    
    
    
    H = np.copy(np.append(H1,[1]))
    H = H[:, np.newaxis]
    
    
    
    #print H.shape
    
    #plt.show()
    #print H

    #Initialize Cluster Centroids

    if np.size(c) > 1:
        C = c
        c = np.size(c)
    else:
        
        (l,C,lut) = fc.FastCMeans(im,c)

    #Update Fuzzy Memberships and cluster centroids

    #I = repmat(I,[1 c])
    I = np.tile(I,np.array([1,c]))
    
    #print ' I shape ', I.shape
    
    dC = np.inf
    
    eps = np.finfo(float).eps
    
    #print 'Epsilon is ', eps

    while (dC > 1E-6):
    	
    	C0 = np.copy(C)
        #Distance to the centroids
	D = np.abs(I-C)
        D = D**(2/(q-1)) + eps
        
        #compute fuzzy memberships
       
        recipSum = np.sum(1/D,1)
        recipSum = recipSum[:, np.newaxis]
        
        
        U = D * recipSum
        
        U = 1/(U+ eps)
        
        #update the centroids
        
        UH = (U**q) * H
        
        s1 = np.sum(UH * I,0)
        s1 = s1[:,np.newaxis]
        s2 = np.sum(UH,0).astype(float)
        s2 = s2[:, np.newaxis]
        
        s1 = np.transpose(s1)
        s2 = np.transpose(s2)
        C = s1 /s2
        
        
        C = np.sort(C)
        #Change in centroids
        dC = np.max(np.abs(C-C0))
        
    #Defuzzify and create a label image
    
    Umax = np.max(U,1)
    #Umax = Umax[:,np.newaxis]
    #print Umax
    LUT = np.argmax(U,1)
    #print LUT2label
    
    L = label.LUT2label(im,LUT) 

    return (L,C,U,LUT,H)


