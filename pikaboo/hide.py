#!/usr/bin/env python

import Image
import random
from util import LoopInterrupt

__all__ = ['hide']

def hide(string, src_img_path, dest_img_path):
  l_bin = bin(len(string))[2:]
  key_size = 5
  passcode_size = 10
  im = Image.open(src_img_path)
  pels = im.load()
  width, height = im.size
  done = False
  trys = 0
  while not done:
    key_int = random.randint(2**(key_size*3-1), 2**(key_size*3) - 1)
    passcode_int = random.randint(2**(passcode_size*3-1), 2**(passcode_size*3) - 1)
    key = bin(key_int)[2:]
    passcode = bin(passcode_int)[2:]
    bin_str = []
    for c in string:
      bin_str.append(bin(ord(c))[2:])
      bin_str.append(key)
    bin_str = ''.join(bin_str)  
    data = '%s%s%s%s' % (l_bin, key, bin_str, passcode)        
    i = 0; j = 0  
    for x in xrange(0, len(data), 3):
      r,g,b = pels[i,j]
      try:
        temp = int(data[x])
        if (r ^ temp): r = r | 0xFF if temp else r & 0xFE    
      except IndexError:        
        pass
      try:
        temp = int(data[x+1])
        if (g ^ temp): g = g | 0xFF if temp else g & 0xFE    
      except IndexError:        
        pass
      try:
        temp = int(data[x+2])
        if (b ^ temp): b = b | 0xFF if temp else b & 0xFE    
      except IndexError:        
        pass
      pels[i,j] = (r,g,b)
      i += 1
      if i == width and j < height:
        i = 0
        j += 1
      elif j == height:
        raise Exception('Image not big enough !')
    test_data = ''    
    try:
      for i in xrange(height):
        for j in xrange(width):
          if test_data.find(passcode) != -1:
            raise LoopInterrupt
          r,g,b = pels[j,i]                       
          test_data += str(r & 0x01)
          test_data += str(g & 0x01)
          test_data += str(b & 0x01)                
    except LoopInterrupt:
      pass
    test_data = test_data.split(passcode)[0]+passcode   
    done = (data == test_data) and (test_data.split(key)[0] == l_bin)
    trys += 1
    if trys % 3 == 0:
      key_size += 1
      passcode_size += 1
    if trys == 50:
      raise Exception('Something went wrong !')
  im.save(dest_img_path)  
  return key_int, passcode_int
