# watson@mediamart.jp VR auth
concat = lambda i,j: i+j
vrauth = ("6dedec07-99e2-44e9-b3a5-999d848c3ae5","XmKSzSnkgN0M")
vrurl = reduce(concat,
  ('https://gateway.watsonplatform.net/visual-recognition-beta/api', 
   '/v2/%s',
   '?version=2015-12-02'))
   #'?version=2016-05-19'))
if __name__ == "__main__":
  print vrauth
  print vrurl
