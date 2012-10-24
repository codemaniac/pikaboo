# -*- coding: utf-8 -*-

def main():  
  s = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''  
  src_img_path = 'image.jpeg'
  dest_img_path = 'output.png'
  key, passcode = hide(s, src_img_path, dest_img_path)  
  print 'key = %s, passcode = %s' % (key,passcode)
  got = retrieve(dest_img_path, key, passcode)
  print s == got

if __name__ == '__main__':
  main()
