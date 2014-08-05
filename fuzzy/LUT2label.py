import numpy as np

def LUT2label(im,LUT):
    #Create a label image using LUT obtained from a clustering operation of grayscale data
    
    # Intensity range
	
	Imin = float(np.min(im[:]))
	Imax = float(np.max(im[:]))
	I = np.transpose(np.array(np.arange(Imin,Imax+1)))
	I = I[:, np.newaxis]
	
	#print I.shape
	#Create a Label Image
	
	L = np.zeros(im.shape,int)
	
	#print L.shape
	
	for k in range(0, np.max(LUT)+1):
		
		
		#intensity range for k-th class
		i = np.nonzero(LUT==k)
		
		(arr ,)= i		
		arr = np.copy(arr[:,np.newaxis])
		#print 'arr shape is ', arr.shape
		#print arr[1]
		
		i1 = arr[1]
		
		sz = np.size(arr)
		#print arr[sz-1]
		if sz > 1:
			i2 = arr[sz-1]
		else:
			i2 = i1

		#map the intensities in the range [I(i1),I(i2)] to class k] 
		bw = np.logical_and(im >= I[i1], im <= I[i2])
		
		L[bw] = k
		
		
	return L	
