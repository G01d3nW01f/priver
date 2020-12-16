import os
import subprocess as sp
import re
import sys
from colorama import Fore as fore
import time

def init():
    logo = """

    ######   ######    ######  ##   ##   ######  ######
    ##   ##  ##   ##   # ## #  ##   ##      ##   ##   ##
    ##   ##  ##   ##     ##    ##   ##     ##    ##   ##
    ##   ##  ##  ###     ##    ### ###    ####   ##  ###
    ######   #####       ##     #####        ##  #####
    ##       ## ###    # ## #    ###    ##   ##  ## ###
    ##       ##  ###   ######     #      #####   ##  ###

    Recon for privilege escalation 
    """

    print(f"{fore.RED}{logo}{fore.RESET}")

def main():

    pythonVersion = sp.getoutput("python3 -V")
    platform = sys.platform

    def output_parse(output):

        reg = re.search(r"\n",output)

        if reg == None:

            return output

        else:

            output = output.split('\n')

            return output


    def output_forms(output):

        if str(type(output)) == "<class 'list'>":

            for i in output:
                print(i)
                time.sleep(0.5)     
        else:

            print(output)
            print("")
     
    def cycle(output):
        output = output_parse(output)
        output = output_forms(output)
        print("")

    output = sp.getoutput('uname -a')
    cycle(output)

    output = sp.getoutput('sudo -V')

    output = sp.getoutput('sudo -l')
    cycle(output)

    output = sp.getoutput('ls -l /etc | grep sudoers')
    cycle(output)

    output = sp.getoutput('ls -l /etc | grep passwd')
    cycle(output)

    output = sp.getoutput('ps aux | grep root')
    cycle(output)
    
    output = sp.getoutput('find / -perm -u=s -type f 2>/dev/null')
    cycle(output)

    output = sp.getoutput('ps -ef | grep cron')
    cycle(output)

if __name__ == "__main__":

    init()
    main()


