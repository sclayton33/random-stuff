#! /usr/bin/python3.7
# mcb.pyw - Saves clipboard contents to specified keyword and allows recall later.
# Usage: ./mcb.pyw help - Displays usage guide.
#        ./mcb.pyw save <keyword> - Save clipboard contents to keyword.
#        ./mcb.pyw del <keyword> - Delete clipboard contents for specified keyword.
#        ./mcb.pyw delall - Deletes all clipboard contents.
#        ./mcb.pyw <keyword> - loads keyword to clipboard.
#        ./mcb.pyw list - loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delall':
    mcbShelf.clear()
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'help':
    print('''
Python multi-clipboard help:
./mcb.pyw help - Displays usage guide.
./mcb.pyw save <keyword> - Save clipboard contents to keyword.
./mcb.pyw del <keyword> - Delete clipboard contents for specified keyword.
./mcb.pyw delall - Deletes all clipboard contents.
./mcb.pyw <keyword> - loads keyword to clipboard.
./mcb.pyw list - loads all keywords to clipboard.''')
elif len(sys.argv) == 2:
    # List keywords and load conent.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

