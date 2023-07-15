import sys,os,re,socket,binascii,time,json,random,threading,Queue,pprint,urlparse,smtplib,telnetlib,os.path,hashlib,string,urllib2,glob,sqlite3,urllib,argparse,marshal,base64,colorama,requests
import sys
import os
import re
import socket
import binascii
import time
import random
import threading
from multiprocessing.pool import ThreadPool
from colorama import *
from random import choice
from colorama import Fore,Back,init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from Queue import Queue
from time import strftime
from urlparse import urlparse
from urllib2 import urlopen
colorama.init()

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 
  ____                        _       ___                       _     _               
 |  _ \  ___  _ __ ___   __ _(_)_ __ |_ _|_ __   __ _ _ __ __ _| |__ | |__   ___ _ __ 
 | | | |/ _ \| '_ ` _ \ / _` | | '_ \ | || '_ \ / _` | '__/ _` | '_ \| '_ \ / _ \ '__|
 | |_| | (_) | | | | | | (_| | | | | || || |_) | (_| | | | (_| | |_) | |_) |  __/ |   
 |____/ \___/|_| |_| |_|\__,_|_|_| |_|___| .__/ \__, |_|  \__,_|_.__/|_.__/ \___|_|   
                                         |_|    |___/                                 
				  
                  telegram group : https://t.me/linuxploit_com
			                  """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)

def getIP(site):
    try:
        site = site.strip()
        if 'http://' not in site:
            IP1 = socket.gethostbyname(site)
            print("IP: " + IP1)
            with open('ips.txt', 'a') as f:
                f.write(IP1 + '\n')
        elif 'http://' in site:
            url = site.replace('http://', '').replace('https://', '').replace('/', '')
            IP2 = socket.gethostbyname(url)
            print("IP: " + IP2)
            with open('ips.txt', 'a') as f:
                f.write(IP2 + '\n')
    except:
        pass

if __name__ == '__main__':
    logo()
    nam = raw_input('Domain List name: ') 
    with open(nam) as f:
        domain_list = f.read().splitlines()

    pool = ThreadPool(1100) 
    pool.map(getIP, domain_list)
    pool.close()
    pool.join()