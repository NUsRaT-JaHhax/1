# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: sumarr
import os, sys

def bannar():
    os.system('clear')
    print "\x1b[94m\n  ____   ___  _     _                                        \n / ___| / _ \\| |   (_)                                       \n \\___ \\| | | | |   | |                                       \n  ___) | |_| | |___| |                                       \n |____/ \\__\\_\\_____|_|                \n \n  __     __     _                      _     _ _ _ _         \n  \\ \\   / /   _| |_ __   ___ _ __ __ _| |__ (_) (_) |_ _   _ \n   \\ \\ / / | | | | '_ \\ / _ \\ '__/ _` | '_ \\| | | | __| | | |\n    \\ V /| |_| | | | | |  __/ | | (_| | |_) | | | | |_| |_| |\n     \\_/  \\__,_|_|_| |_|\\___|_|  \\__,_|_.__/|_|_|_|\\__|\\__, |\n                                                       |___/ \n              \n                                          \x1b[0m   \x1b[93mVersion : 1.0\n\n                \x1b[0;37;41m SQLi Vulnerability Scanner\x1b[0m\n                \n             \x1b[0;37;41m Coded By DarkXploit , Dark Wolf \x1b[0m\n              \n               \x1b[95m       Team Dark Hunter 141\x1b[0m\n    \n               \n"
    site = raw_input('\x1b[92m[!] Paste Site Url With Perameter : \x1b[93m')
    os.system('curl -s ' + site + ' | wc -l > file1')
    abir = '%27'
    sitea = site + abir
    os.system('curl -s ' + sitea + ' | wc -l > file2')
    abir = open('file1')
    na = abir.read()
    biva = open('file2')
    ho = biva.read()
    if na > ho:
        print ''
        print ''
        print '\x1b[96m[\xc3\x97]\x1b[92m Vulnerability Found !!! '
    elif na < ho:
        print ''
        print ''
        print '\x1b[96m[\xc3\x97]\x1b[92m Vulnerability Found !!! '
    elif na == ho:
        print ''
        print ''
        print '\x1b[96m[\xc3\x97]\x1b[91m Vulnerability Not Found !!! '
    else:
        print ''
        print ''
        print '\x1b[91m [\xc3\x97]Something is Wrong'
    os.system('rm -rf file1 && rm -rf file2')
    print ''
    print ''
    print ''
    raw_input('\x1b[92m[\xe2\x9c\x93]\x1b[91m Press Enter To Continue...')
    bannar()


bannar()