#!/usr/bin/env python

import Image
from util import LoopInterrupt

__all__ = ['retrieve']

def retrieve(src_img_path, key, passcode):
  key = bin(key)[2:]
  passcode = bin(passcode)[2:]
  im = Image.open(src_img_path)
  pels = im.load()
  width, height = im.size
  data = ''
  try:
    for i in xrange(height):
      for j in xrange(width):
        if data.find(passcode) != -1:
          raise LoopInterrupt
        r,g,b = pels[j,i]                       
        data += str(r & 0x01)
        data += str(g & 0x01)
        data += str(b & 0x01)                
  except LoopInterrupt:
    pass
  data = data.split(passcode)[0] + passcode
  frags = data.split(key)
  l = int(frags[0], 2)
  frags = frags[1:-1]
  data = []  
  for frag in frags:
    data.append(chr(int(frag, 2)))
  return ''.join(data)
