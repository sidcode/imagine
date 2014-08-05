'''
The software aims to be an open-source package with basic, and advanced Image Processing features.
Copyright (C) 2014	Indian Institute of Remote Sensing, Dehradun

The original authors of this program (in alphabetical order) are:

---------------------------------------------------------------------------------------------------------------------------------------
Sno.		NAME											Email( AT gmail DOT com)			Role(s)
---------------------------------------------------------------------------------------------------------------------------------------
1.				Abhishek Mohta							mohta.abhishek								GUI, Spectral
----------------------------------------------------------------------------------------------------------------------------------------

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
import numpy as np
from osgeo import gdal
import tifwork

dataset=tifwork.openTIF(filename)
cols, rows,bands,bandArray=tifwork.detailsTIF(dataset)
bandArray=tifwork.getBand(dataset,bands,bandArray)

mean=np.mean(bandArray, axis=0)
median=np.median(bandArray, axis=0)
stddev=np.std(bandArray,axis=0)
max=np.max(bandArray,axis=0)
min=np.min(bandArray,axis=0)

f=open("abc.txt",'w')
f.write("Mean = "+str(mean)+"\n")
f.write("Median = "+str(median)+"\n")
f.write("Standard Deviation = "+str(stddev)+"\n")
f.write("Max = "+str(max)+"\n")
f.write("Min = "+str(min)+"\n")
f.close()

#f=open("abc.txt",'r')
lines=[line.strip() for line in open('abc.txt')]
print lines

f.close()


