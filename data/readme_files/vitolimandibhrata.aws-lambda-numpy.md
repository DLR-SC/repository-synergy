NumPy Python Library for AWS Lambda
===========================================

This is a custom compiled NumPy library for Python. 

Alternative project:
https://github.com/Miserlou/lambda-packages

The AMI image of AWS Lambda does not have the required dependencies as listed below:

1. Blas
2. Lapack
3. Atlas

Thus, we needed to compile NumPy with statically linked blas, lapack and atlas libraries instead of the default dynamic link.

Common error messages that this project will resolve

	liblapack.so.3: cannot open shared object file: No such file or directory
	libptf77blas.so.3: cannot open shared object file: No such file or directory
	libf77blas.so.3: cannot open shared object file: No such file or directory
	libptcblas.so.3: cannot open shared object file: No such file or directory
	libcblas.so.3: cannot open shared object file: No such file or directory
	libatlas.so.3: cannot open shared object file: No such file or directory
	libptf77blas.so.3: cannot open shared object file: No such file or directory
	libgfortran.so.3: cannot open shared object file: No such file or directory
	libquadmath.so.0: cannot open shared object file: No such file or directory

### How to use

Just copy the directories of the libraries and the 'lib' folder into your AWS Lambda zip package.

### Instructions on compiling this package from scratch

Prepare a fresh AWS EC instance with AWS Linux.

Install compiler dependencies

	sudo yum -y install python-devel
	sudo yum -y install gcc-c++
	sudo yum -y install gcc-gfortran
	sudo yum -y install libgfortran

Install NumPy dependencies 

	sudo yum -y install blas
	sudo yum -y install lapack
	sudo yum -y install atlas-sse3-devel

Create /var/task/lib to contain the runtime libraries

	mkdir -p /var/task/lib

/var/task is the root directory where your code will reside in AWS Lambda thus we need to statically link the required library files in a well known folder which in this case /var/task/lib

Copy the following library files to the /var/task/lib

	cp /usr/lib64/atlas-sse3/liblapack.so.3 /var/task/lib/.
	cp /usr/lib64/atlas-sse3/libptf77blas.so.3 /var/task/lib/.
	cp /usr/lib64/atlas-sse3/libf77blas.so.3 /var/task/lib/.
	cp /usr/lib64/atlas-sse3/libptcblas.so.3 /var/task/lib/.
	cp /usr/lib64/atlas-sse3/libcblas.so.3 /var/task/lib/.
	cp /usr/lib64/atlas-sse3/libatlas.so.3 /var/task/lib/.
	cp /usr/lib64/atlas-sse3/libptf77blas.so.3 /var/task/lib/.
	cp /usr/lib64/libgfortran.so.3 /var/task/lib/.
	cp /usr/lib64/libquadmath.so.0 /var/task/lib/.

Get the latest numpy source code from http://sourceforge.net/projects/numpy/files/NumPy/

Go to the numpy source code folder e.g numpy-1.10.4
Create a site.cfg file with the following entries

	[atlas]
	libraries=lapack,f77blas,cblas,atlas
	search_static_first=true
	runtime_library_dirs = /var/task/lib
	extra_link_args = -lgfortran -lquadmath

-lgfortran -lquadmath flags are required to statically link gfortran and quadmath libraries with files defined in runtime_library_dirs

Build NumPy

	python setup.py build

Install NumPy

	python setup.py install

Check whether the libraries are linked to the files in /var/task/lib

	ldd $PYTHON_HOME/lib64/python2.7/site-packages/numpy/linalg/lapack_lite.so

You should see

	linux-vdso.so.1 =>  (0x00007ffe0dd2d000)
	liblapack.so.3 => /var/task/lib/liblapack.so.3 (0x00007ffad6be5000)
	libptf77blas.so.3 => /var/task/lib/libptf77blas.so.3 (0x00007ffad69c7000)
	libptcblas.so.3 => /var/task/lib/libptcblas.so.3 (0x00007ffad67a7000)
	libatlas.so.3 => /var/task/lib/libatlas.so.3 (0x00007ffad6174000)
	libf77blas.so.3 => /var/task/lib/libf77blas.so.3 (0x00007ffad5f56000)
	libcblas.so.3 => /var/task/lib/libcblas.so.3 (0x00007ffad5d36000)
	libpython2.7.so.1.0 => /usr/lib64/libpython2.7.so.1.0 (0x00007ffad596d000)
	libgfortran.so.3 => /var/task/lib/libgfortran.so.3 (0x00007ffad5654000)
	libm.so.6 => /lib64/libm.so.6 (0x00007ffad5352000)
	libquadmath.so.0 => /var/task/lib/libquadmath.so.0 (0x00007ffad5117000)
	libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007ffad4f00000)
	libc.so.6 => /lib64/libc.so.6 (0x00007ffad4b3e000)
	libpthread.so.0 => /lib64/libpthread.so.0 (0x00007ffad4922000)
	libdl.so.2 => /lib64/libdl.so.2 (0x00007ffad471d000)
	libutil.so.1 => /lib64/libutil.so.1 (0x00007ffad451a000)
	/lib64/ld-linux-x86-64.so.2 (0x000055cfc3ab8000)

