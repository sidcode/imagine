'''
The software aims to be an open-source package with basic, and advanced Image Processing features.
Copyright (C) 2014	Indian Institute of Remote Sensing, Dehradun

The original authors of this program (in alphabetical order) are:

---------------------------------------------------------------------------------------------------------------------------------------
Sno.		NAME											Email( AT gmail DOT com)			Role(s)
---------------------------------------------------------------------------------------------------------------------------------------

1.				Shalaka Somani							shalaka195										GUI
----------------------------------------------------------------------------------------------------------------------------------------

Compatible with Python 2.7 ( NOT COMPATIBLE with Python(>3))

Dependencies: GDAL, NumPy, SciPy, OpenCV, Spectral Python, Tkinter, scikit-learn, scikit-fuzz

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

import Tkinter as tk
import ttk
import matrix
import tkFileDialog
from PIL import Image
import tkMessageBox
import menu_unsuper
import sys
sys.path.append('./SVM')
import menu_super as men

def classgui():
	frame=tk.Tk()
	frame.title("Image Classification")

	frame1=tk.Frame(frame)
	frame2=tk.Frame(frame)

	x1=tk.Label(frame, text="Image Classification")
	x1.pack(side=tk.TOP, pady = 5 , padx = 5 )


	x2=tk.Label(frame1, text="Supervised")
	x2.pack(side=tk.TOP, pady = 5 , padx = 5 )

	button1=tk.Button(frame1, text="SVM Linear",command = lambda:men.supervi('linear'))
	button1.pack(side=tk.TOP, padx=2, pady=2)

	button1=tk.Button(frame1, text="SVM Poly" , command = lambda:men.supervi('poly'))
	button1.pack(side=tk.TOP, padx=2, pady=2)

	button1=tk.Button(frame1, text="SVM RBF" , command = lambda:men.supervi('rbf'))
	button1.pack(side=tk.TOP, padx=2, pady=2)


	x3=tk.Label(frame2, text="Unsupervised")
	x3.pack(side=tk.TOP, pady = 5 , padx = 5 )

	button2=tk.Button(frame2, text="IsoData", command=lambda:menu_unsuper.unsuper(2))
	button2.pack(side=tk.TOP, padx=2, pady=2)
	button3=tk.Button(frame2, text="K-Means", command=lambda:menu_unsuper.unsuper(1))
	button3.pack(side=tk.TOP, padx=2, pady=2)
	button3=tk.Button(frame2, text="Fuzzy", command=lambda:menu_unsuper.unsuper(3))
	button3.pack(side=tk.TOP, padx=2, pady=2)


	frame1.pack(side=tk.LEFT, padx=20, pady=20)
	frame2.pack(side=tk.LEFT, padx=20, pady=20)
	frame.mainloop()
