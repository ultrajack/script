#!/usr/bin/python
# -*- coding: utf-8 -*-
"""IBM Watson Developer Cloud  Visual Recognition
"""
import os
import sys
import json
import requests

from auth import vrauth, vrurl, concat
url = vrurl%"classify"

def classifyImage(item):
  try: itemfd = open(item, 'rb')
  except IOError, xe:
    return {'Error': xe, 'filename': item}
  itemname = os.path.basename(item)
  #print url
  res = requests.post(url, auth=vrauth,
    files={
      'images_file': (itemname, itemfd)
    }
  )
  if res.status_code == requests.codes.ok:
    data = json.loads(res.text)
    return data
  else:  # error
    print 'stauts_code: %s(reason: %s)'%(res.status_code, res.reason)

import pickle
if __name__ == "__main__":
  try:
    item = sys.argv[1]
  except:
    print "Usage %s <file>"%sys.argv[0]
    sys.exit(1)

  result = classifyImage(item)
  pf = open(sys.argv[1]+".pickle", "wb")
  pickle.dump(result, pf)
  pf.close()
