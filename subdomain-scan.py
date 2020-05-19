#!/usr/bin/env python


# By: pwnshell
import pyfiglet
import termcolor
import optparse
import os.path
import requests

try:

    parser = optparse.OptionParser()
    parser.add_option("-d", "--domain", dest="domain", help="Domain Name")
    parser.add_option("-w", "--wordlist", dest="wordlist", help="Worlist File i.e. full path")
    
    (options, args) = parser.parse_args()

    print termcolor.colored('                 Sub-Domain Scanner By:!!', 'red', attrs=['bold'])
    banner = pyfiglet.figlet_format("            pwnshell")
    print termcolor.colored(banner, 'red', attrs=['bold'])

    if os.path.exists(str(options.wordlist)) != True:
        print termcolor.colored('\nPlease enter a valid wordlist and re-run the program.', 'red', attrs=['bold'])
    else:    
        print termcolor.colored('\nGO...GRAB A COFFE FOR YOURSELF TILL THE TIME SCAN GETS COMPLETED..:)', 'blue', attrs=['blink'])

        try:
            with open(options.wordlist,"r") as wordlist:
                for line in wordlist:
                    try:
                        word = line.strip()
                        url = word + "." + options.domain
                        f = requests.get("http://" + url)
                        print termcolor.colored('\nSubdomain Found: {}'.format(url), 'green', attrs=['bold'])
            
                    except requests.exceptions.ConnectionError:
                        pass

        except KeyboardInterrupt:
            print('\n[+]Ctrl + c..Byeeee...')

except KeyboardInterrupt:
    print('\nByeeeee....')
