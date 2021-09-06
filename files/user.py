#!usr/bin/python2 
# -*- coding: utf-8 -*-
# Author : Nabil-Rahmam ;)

import os,sys,json
import urllib2,time 


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
    print (logo)
    print 
    url = raw_input('\033[1;31m>> \033[1;32mEnter Site Url \033[1;31m(with http) \033[1;32m: \033[1;35m')
    print 
    print ('   \033[1;31m[+] \033[1;32mTarget   \033[1;31m>> \033[1;33m'+url)
    print ('   \033[1;31m[+] \033[1;32mScanning \033[1;31m>> \033[1;33mStarting...')
    time.sleep(2.5)
    print 
    total_url = url+'/wp-json/wp/v2/users'
    try:
      req = urllib2.urlopen(total_url)
      re = req.read()
      data = json.loads(re)
      #data = json.dumps(js, indent=2)
      for x in range(len(data)):
          print ('\033[1;36mId \033[1;31m>> \033[1;36m'+str(data[x]['id'])+' | \033[1;32mName \033[1;31m>> \033[1;32m'+data[x]['name']+' | \033[1;33mUserName \033[1;31m>> \033[1;33m'+data[x]['slug'])
      print 
      print ("\033[1;31m<<< \033[1;33mThanks For Using \033[1;31m>>>")
          
    except:
      print 
      print ('\033[1;31m[+] An Error !\033[1;0m')
main()
