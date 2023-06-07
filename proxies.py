import os
import sys
import random
import time
import requests

def Print():
    Cls = '\x1b[0m'
    Colors = [37, 31, 32, 36, 30, 35, 34, 33]
    Logo = '''
     _____________
< Proxies Grabber >
 -------------
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
             """"          """""""
             |_)  _|                     |
 __ \   _ \  | | |    _ \  __|  _ \   _` |  _ \  __|
 |   | (   | | | __|  __/ (    (   | (   |  __/ |
_|  _|\___/ _|_|_|  \___|\___|\___/ \__,_|\___|_|

    '''
    for N, Line in enumerate(Logo.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(Colors), Line, Cls))
        time.sleep(0.05)

def Clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])

def Http_grab():
    color_array = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[39m']
    print(random.choice(color_array) + 'Grabbing Http Proxies')
    time.sleep(1)
    print(random.choice(color_array) + '.')
    time.sleep(1)
    print(random.choice(color_array) + '..')
    time.sleep(1)
    print(random.choice(color_array) + '....')
    r = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all').text.encode('utf-8')
    with open('HTTP_Grabbed.txt', 'w') as op:
        op.write(r.replace(b'\r\n', b'\n').decode('utf-8'))
    Clear()
    print(random.choice(color_array) + 'Grab Completed!' + '\n' + random.choice(color_array) + 'Restarting...!')
    time.sleep(5)

def Socks5_grab():
    color_array = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[39m']
    print(random.choice(color_array) + 'Grabbing Socks5 Proxies')
    time.sleep(1)
    print(random.choice(color_array) + '.')
    time.sleep(1)
    print(random.choice(color_array) + '..')
    time.sleep(1)
    print(random.choice(color_array) + '....')
    r = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text.encode('utf-8')
    with open('SOCKS5_Grabbed.txt', 'w') as op:
        op.write(r.replace(b'\r\n', b'\n').decode('utf-8'))
    Clear()
    print(random.choice(color_array) + 'Grab Completed!' + '\n' + random.choice(color_array) + 'Restarting...!')
    time.sleep(5)

def Socks4_grab():
    color_array = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[39m']
    print(random.choice(color_array) + 'Grabbing Socks4 Proxies')
    time.sleep(1)
    print(random.choice(color_array) + '.')
    time.sleep(1)
    print(random.choice(color_array) + '..')
    time.sleep(1)
    print(random.choice(color_array) + '....')
    r = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text.encode('utf-8')
    with open('SOCKS4_Grabbed.txt', 'w') as op:
        op.write(r.replace(b'\r\n', b'\n').decode('utf-8'))
    Clear()
    print(random.choice(color_array) + 'Grab Completed!' + '\n' + random.choice(color_array) + 'Restarting...!')
    time.sleep(5)

while True:
    Clear()
    Print()

    color_array = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[39m']
    print(random.choice(color_array) + '[?]Enter The Proxy Type Number:' + '\n' + random.choice(color_array) + '[1]HTTP/S' + '\n' + random.choice(color_array) + '[2]SOCKS5' + '\n' + random.choice(color_array) + '[3]SOCKS4')
    tYpe = input('> ')
    if tYpe == '1':
        Clear()
        Http_grab()
    elif tYpe == '2':
        Clear()
        Socks5_grab()
    elif tYpe == '3':
        Clear()
        Socks4_grab()
