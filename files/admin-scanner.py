#!/usr/bin/python 
# AUTHOR : NABIL-RAHMAN
# FUCK YOU DEAR DECRYPTER 
# -*- coding: utf-8 -*-
import requests as nabil 
import time 
import os,sys

# file 
file = open('scan.txt','r')


logo = """ \033[1;94m
    _   __    _       ____________
   / | / /   | |     / / ____/ __ )
  /  |/ /____| | /| / / __/ / __  |
 / /|  /_____/ |/ |/ / /___/ /_/ /
/_/ |_/      |__/|__/_____/_____/

Created By : \033[1;96mNabil-Rahman |\033[1;0m [V 1.1.1]

\033[1;32m------------------------------------------
\33[93m AUTHOR  : Team DarkWeb T-D
\33[93m GITHUB  : github.com/Nabil-Official 
\33[93m FB      : nabil.404
\033[1;32m------------------------------------------
"""


def main():
    os.system('clear')
    print logo
    print 
    site = raw_input('\033[1;31m[+] \033[1;32mSITE URL\033[1;31m (http://site.com) \033[1;33m: \033[1;36m ')
    admin = raw_input('\033[1;31m[+] \033[1;32mADMIN DIRECTORY\033[1;31m (admin,administrator)\033[1;33m :\033[1;36m ')
    total = site+'/'+admin+'/'
    i = nabil.get(total)
    print 
    if i.status_code != 200:
       print ('   \033[1;31m>>\033[1;32m SITE    : \033[1;33m'+site)
       print ('   \033[1;31m>>\033[1;32m STATUS  :\033[1;31m NOT FOUND !')
       print ('   \033[1;31m>>\033[1;32m SCANING :\033[1;31m ERROR !')

    else:
       print ('   \033[1;31m>>\033[1;32m SITE    :\033[1;33m '+site)
       print ('   \033[1;31m>>\033[1;32m STATUS  :\033[1;32m OK')
       print ('   \033[1;31m>>\033[1;32m SCANING :\033[1;32m STARTING...')
       time.sleep(2)
       print 
       for words in file:
           words = words.strip()
           main = total+words
           req = nabil.get(main)
           if req.status_code == 200:
              print ('\033[1;31m[+] \033[32mFOUND : '+main)
           else:
              print ('\033[1;31m[+] NOT FOUND : '+main)
       
main()
