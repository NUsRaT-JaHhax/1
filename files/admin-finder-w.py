#!/usr/bin/python2

#MODUELS

import os
import sys
import requests as nabil

# MAIN FUNTION

def main():
    os.system('clear')
    web = raw_input('>> ENTER WEBSITE NAME : ')
    wordlist = str(input('>> ENTER WARDLIST PATH : '))
    if web == '':
       print ('ENTER SOMETHING')
       exit() 
    else:
       try:
         chk_site = nabil.get(web)
         if chk_site.status_code != 200:
             print (' CHECK YOUR URL')
         else:
             try:
               f = open(wordlist , 'r')
               fr = f.read()
               print (fr)
             except Exception as e:
               print ('ERROR : '+str(e))
       except Exception as e:
          print ('ERROR : '+str(e))
main()

