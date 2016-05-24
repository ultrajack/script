#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pickle
def readPickle(filepath):
  pf = file(filepath, 'rb')
  data = pickle.load(pf)
  pf.close()
  return data

def addDict(item, val, dictname, replacemax=0):
  if item in dictname:
    if replacemax:
      if val > dictname[item]: dictname[item] = val
    else:
      dictname[item] += val
  else:
    dictname[item] = val

def makeScoreList(data, method, minscore=0.7, maxlen=10, nobuiltin=1):
  scoreList = []
  scoreTotal = {}
  scoreMax = {}
  for img in data['images']:
    filename = img['image'] 
    filescore = []
    filedict = {}
    for scr in img['scores']:
      score, cid, name = scr['score'], scr['classifier_id'], scr['name']
      if nobuiltin and cid == name: continue
      if not method in name: continue
      if score < minscore or len(filescore) >= maxlen: break
      filescore.append((name, score, cid,))
      addDict(name, score, filedict)
      addDict(name, score, scoreTotal)
      addDict(name, score, scoreMax, 1)
    scoreList.append((filename, filescore, filedict))
  return scoreList, scoreTotal, scoreMax

def printdict(dictname):
  for k, v in dictname.iteritems():
    print k, v

if __name__ == "__main__":
  try:
    item = sys.argv[1]
  except:
    print "Usage %s <file>"%sys.argv[0]
    sys.exit(1)

  methodlist = ['2CH', '4CH', 'SAG', '4CHSAG', 'CINE']
  detail = 0
  for f in sys.argv[1:]:
    if f == '-d':
      detail = 1
      continue
    result = readPickle(f)
    for m in methodlist:
      if m in f:
        method = m
	break
    else:
      print "No METHOD!!!!"
      sys.exit(2)
    slist, stotal, smax = makeScoreList(result, method)
    #printdict(stotal)
    #print sorted(smax.items(), key=lambda x:x[1], reverse=1)
    maxscore, maxtotal = 0, 0
    print "Filename:", f
    for k, v in  sorted(stotal.items(), key=lambda x:x[1], reverse=1):
      if not maxscore: maxscore, maxtotal = smax[k], v
      print "%6.4f"%( maxscore * v / maxtotal), k
    else: print

  if not detail: sys.exit(0)
  for fn, img, imgdict in slist:
    print fn
    for score, cid, name in img:
      print "  ", name, score, cid
    else:
      printdict(imgdict)
      print
