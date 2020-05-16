#!/usr/bin/python

import requests
import termcolor
import os.path

try:
    print termcolor.colored('====================================================', 'red', attrs=['bold'])
    print termcolor.colored('   SUB DOMAIN SCANNER BY: pwnshell', 'green', attrs=['bold'])
    print termcolor.colored('====================================================', 'red', attrs=['bold'])
    target_url = raw_input(termcolor.colored('\nPlease enter Domain Name to scan: ', 'red', attrs=['bold']))
    target_list = raw_input(termcolor.colored('\nPlease enter complete wordlist path e.g./usr/share/wordlist/file.txt: ', 'red', attrs=['bold']))
    if os.path.exists(target_list) != True:
        print termcolor.colored('\nPlease enter a valid wordlist and re-run the program.', 'red', attrs=['bold'])
    else:    
        print termcolor.colored('\nGO...GRAB A COFFE FOR YOURSELF TILL THE TIME SCAN GETS COMPLETED...:)', 'blue', attrs=['blink'])

        try:
            with open(target_list,"r") as wordlist:
                for line in wordlist:
                    try:
                        word = line.strip()
                        url = word + "." + target_url
                        f = requests.get("http://" + url)
                        print termcolor.colored("\nSubdomain Found: " + url, 'green', attrs=['bold'])
            
                    except requests.exceptions.ConnectionError:
                        pass

        except KeyboardInterrupt:
            print termcolor.colored('\n[+]Ctrl + c..Byeeee...', 'red')

except KeyboardInterrupt:
    print termcolor.colored('\nByeeeee....', 'red')
