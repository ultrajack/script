#!/usr/bin/python
# -*- coding: utf-8 -*-
"""IBM Watson Developer Cloud  Visual Recognition
"""
import os
import sys
import json
import requests

from auth import vrauth, vrurl, concat
url = vrurl%"classifiers"

def namefd(f): #from xx_xx__nnn.zip to name, filename, fd
  fname = f
  try: fname = f.split('__')[0]
  except: pass
  filepath = './img/%s'%f
  try: fd = open(filepath, 'rb')
  except:
    print "Can't open", f
    sys.exit(1)
  return fname, f, fd

def createClassifiers(positive, negative=None): # item is item.zip file
  pos = namefd(positive)
  neg = namefd(negative)
  payload = {"name":pos[0]}
  posneg = {'positive_examples': (pos[1:]), 'negative_examples': (neg[1:]),}
  print repr(payload), repr(posneg)

  res = requests.post(url, auth=vrauth,
    data = payload,
    files = posneg,
    )
  if res.status_code == requests.codes.ok:
    data = json.loads(res.text)
    print data
  else:  # error
    print 'stauts_code: %s(reason: %s)'%(res.status_code, res.reason)

if __name__ == "__main__":
  try:
    item = sys.argv[1]
    pos, neg = item.split(':')
  except:
    print "Usage: %s <positive:negative zipfilename under ./img> <neg>"%sys.argv[0]
    sys.exit(1)

  print pos, neg
  #createClassifiers(pos)
  createClassifiers(pos, neg)
  #createClassifiers(neg, pos)
