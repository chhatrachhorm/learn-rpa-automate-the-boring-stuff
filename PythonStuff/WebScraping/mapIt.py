#! python3
# use shebang line to run python with its name from cmd
# shebang line is #! python3


# program to open google map with cmd
# to run: mapIt your_address
import webbrowser
import sys
import pyperclip

# command line arg
if len(sys.argv) > 1:
    # get address from command line
    address = ''.join(sys.argv[1:])
    # the sys.argv will return each arg as array
    print(sys.argv)
else:
    # get address from clipboard
    address = pyperclip.paste()
# webbrowser.open('https://i-out.io')
webbrowser.open('https://www.google.com/maps/place/' + address)
