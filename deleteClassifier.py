#!/usr/bin/python
# -*- coding: utf-8 -*-
"""IBM Watson Developer Cloud  Visual Recognition
"""
import os
import sys
import json
import requests

from auth import vrauth, vrurl, concat
#{u'classifier_id': u'Black_and_white', u'name': u'Black_and_white'}

def deleteClassifier(item):
  urlitem = 'classifiers/%s'%item
  url = vrurl%urlitem
  res = requests.delete(url, auth=vrauth, )
  if res.status_code == requests.codes.ok:
    data = json.loads(res.text)
    print item, "has deleted."
    #print 'label groups(%s): %s'%(len(labels['label_groups']), labels['label_groups'])
    #print 'labels(%s): %s'%(len(labels['labels']), labels['labels'])
  else:  # error
    print 'stauts_code: %s(reason: %s)'%(res.status_code, res.reason)

if __name__ == "__main__":
  try:
    item = sys.argv[1]
  except:
    print "Usage %s <classifier_id>"%sys.argv[0]
    sys.exit(1)

  for item in sys.argv[1:]:
    deleteClassifier(item)
