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
#{u'classifier_id': u'Black_and_white', u'name': u'Black_and_white'}

def listClassifiers(item=None, regonly=1):
  res = requests.get(url, auth=vrauth, headers={'content-type': 'application/json'})
  if res.status_code == requests.codes.ok:
    labels = json.loads(res.text)
    classifiers = labels["classifiers"]
    for clf in classifiers:
      if item:
        if not item in repr(clf): continue
      if regonly and clf['classifier_id'] == clf['name']: continue
      
      print clf['classifier_id'], clf['name']
    #print repr(classifiers)
    #print 'label groups(%s): %s'%(len(labels['label_groups']), labels['label_groups'])
    #print 'labels(%s): %s'%(len(labels['labels']), labels['labels'])
  else:  # error
    print 'stauts_code: %s(reason: %s)'%(res.status_code, res.reason)

if __name__ == "__main__":
  item, regonly = "", 1
  argv = []
  for arg in sys.argv:
    if '--watdefault' in repr(sys.argv): regonly = 0
    else: argv.append(arg)
  try:
    item = argv[1]
  except: pass

  listClassifiers(item, regonly)
