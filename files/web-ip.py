#!/usr/bin/python
import os
import sys
import time
import socket 

def main():
    os.system('clear')
    print #logo
    user = raw_input('ENTER DOMAIN NAME : ')
    if user == "":
       user = raw_input('ENTER DOMAIN NAME : ')
    get_ip = socket.gethostbyname(user)
    print (get_ip)


def main1():
    print (get_ip_address('google.com'))
main1()
