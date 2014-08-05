# Segment N-dimensional grayscale image into c classes using a memory 
# efficient implementation of the c-means (aka k-means) clustering 
# algorithm. The computational efficiency is achieved by using the 
# histogram of the image intensities during the clustering process instead 
# of the raw image data.
#
# INPUT ARGUMENTS:
#   - im  : N-dimensional grayscale image in integer format. 
#   - c   : positive interger greater than 1 specifying the number of
#           clusters. c=2 is the default setting. Alternatively, c can be
#           specified as a k-by-1 array of initial cluster (aka prototype)
#           centroids.
#
# OUTPUT  :
#   - L   : label image of the same size as the input image. For example,
#           L==i represents the region associated with prototype C(i),
#           where i=[1,k] (k = number of clusters).
#   - C   : 1-by-k array of cluster centroids.
#   - LUT : L-by-1 array that specifies the intensity-class relations,
#           where L is the dynamic intensity range of the input image. 
#           Specifically, LUT(1) corresponds to class assigned to 
#           min(im(:)) and LUT(L) corresponds to the class assigned to
#           max(im(:)). See 'apply_LUT' function for more info.
#

import numpy as np
import LUT2label as label



def FastCMeans(im, c):

	# Intensity range
	
	Imin = float(np.min(im[:]))
	Imax = float(np.max(im[:]))
	I = np.transpose(np.array(np.arange(Imin,Imax+1)))
	
	I = I[:, np.newaxis]
	
	# Compute intensity histogram
	
	H = np.histogram(im.flatten(),I.flatten())
	(H1, H2) = H
	#H1 = H1.flatten()
	#H2 = H2.flatten()
	H1 = H1[:, np.newaxis]
    #H2 = H2[:, np.newaxis]
	#print 'H1 and H2 Size: ', H1.shape, H2.shape
    #print H1.shape
	H = np.copy(np.append(H1,[1]))
	H = H[:, np.newaxis]
    
    
	# Initialize cluster centroids
	
	if np.size(c) > 1:
		C = c
		c = np.size(c)
	else:
		dl = (Imax - Imin)/c
		C = np.arange(Imin + dl/2, Imax+1, dl)
		
	# Update cluster centroids
	
	IH = I * H
	dC = float(np.inf)
	
	while (dC > 1.0E-6):
		
		C0 = np.copy(C)
		
		# Distance to the centroids
		D = np.abs(I - C)
		
		# Classify by proximity
		Dmin = np.min(D,1)
		LUT	=	np.argmin(D,1)
		
		for j in range(0,c):
			index = LUT==j
			C[j] = 	np.sum(IH[index]) / np.sum(H[index])
			
		# Change in centroids
		#print (C-C0)
		dC = np.max(np.abs(C-C0))
	
	L = label.LUT2label(im,LUT)
	return (L,C,LUT)
	
