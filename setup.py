from distutils.core import setup
import py2exe
import numpy
import scipy
import matplotlib
import sklearn

setup(windows=['start.py'],
		options={
		'py2exe':{
			r'includes':[r'scipy.sparse.csgraph._validation',
						r'scipy.special._ufuncs_cxx',
						r'sklearn.utils.sparsetools._graph_validation',
						r'sklearn.utils.lgamma',
						r'sklearn.utils.weight_vector']
		}
	}
)