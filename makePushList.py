#!/usr/bin/python
from itertools import permutations
for x, y in permutations(range(7),2):
  #if x == y: continue
  for ls, m in (("LVH","4CH"),("Stenosis","SAG")):
    print "%s_%s__00%d.zip:Normal_%s__00%d.zip"%(ls, m, x, m, y)
