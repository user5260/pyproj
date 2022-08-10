#!/usr/bin/env python3
'''
lookup - python3 script
------------------------
Modified version of 'lookup' to work better
with the Qt Python3 Interpreter from 3-Labs
for Android.
Basically, just adding a prompt for user input
instead of getting args from the CLI.
# TODO:
    - Add GUI front-end. Tcl Tk (import ttk)?

Authored by: brianc2788@gmail.com
'''
from bs4 import BeautifulSoup
import requests,sys

""" Request URL and soupify. Print Definition(s). """
def main():
    """ Prompt user for a word to look up. """
    lookupWord = input('Enter:')
    webAddr = 'https://www.merriam-webster.com/dictionary/'+lookupWord+'/'
    '''
        Handle exception in case of no internet connection.
        socket.gaierror (get address info error); name resolution failure.
        Presumably, the first thing these modules try to do is resolve
        the domain name through the dns. Raises an exception & breaks the loop.
    '''
    try:
        req = requests.get(webAddr)
    except Exception:
        print('An error has occurred while trying to establish a connection with the internet.')
        sys.exit(1)
    # Soupify; create soup object & designate the python built-in html parser.
    soup = BeautifulSoup(req.text,'html.parser')
    # Create list of CSS class attributes
    # Tag is <span class="dtText"><\span>
    resultList = soup.select('.dtText')
    # Print the word & its definition(s).
    entryNum = 1
    print('*',lookupWord.upper(),sep='')
    if len(resultList) == 0:
        print('No dictionary entries found.')
    else:
        for r in resultList:
            print(entryNum,r.getText())
            entryNum += 1
    
print('\nPowered by Merriam-Webster.com\nAuthored by brianc2788@gmail.com')

if __name__ == '__main__':
    main()