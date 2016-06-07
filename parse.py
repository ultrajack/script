#!/usr/env/bin python

#print "Hello, world!!"
import sys
import dicom
import pylab

import os
for root, dirs, files in os.walk('./'):
  #if '.DCM' in files: print "here:",files
  #	if dirs: print dirs
  dicoms = [x for x in files if '.dcm' in x.lower()]
  r = str(root).replace('\\', '__')
  for x in dicoms:
    fname = '__'.join([r, x])
    fpath = fname.replace('__', '/')
    fname = fname.replace('.DCM', '.png')
    ds=dicom.read_file(fpath)
    #print "FNAME", fname
    try:
      pylab.imsave('./img/'+fname, ds.pixel_array, cmap=pylab.cm.bone)
    except Exception, xe:
      print xe
sys.exit(0)
