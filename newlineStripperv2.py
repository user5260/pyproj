'''
pyscripts/newlineStripper.py
----------------------------
strip whitespace & newlines out of
text files and copies the single-
line string to a new, plaintext
file.

- asks the user for a path to a plain-text file.
  absolute or relative paths will work.
- after the inputted string checks out,
  the program moves on to open and read the file.
  if there is a problem with the path inputted,
  the program will loop until satisfied or
  the process is killed (e.g. SIGINT).
- next, the program prints the string of
  text gotten from the file (after closing it,
  of course)

brianc2788@gmail.com
github.com/user5260
'''
import os
import re

globPath = ' '
bGoodPath = False
bGoodFile = False

while not bGoodPath & bGoodFile:
    usrInput = input('enter the full/relative path of your plaintext file: ')
    if not os.path.isdir(os.path.dirname(usrInput)):
        print('invalid directory/directories.')
        bGoodPath = False
    else:
        bGoodPath = True
        if not os.path.isfile(usrInput):
            print('invalid file/file not found.')
            bGoodFile = False
        else:
            bGoodFile = True
            globPath = usrInput

stripper = re.compile(r'[\S]+')
rFile = open(globPath, mode='r')

# if rFile.closed():
#     print('unable to open file.')

fullString = rFile.read()
rFile.close()

validChars = stripper.findall(fullString)
cutString = ''
for n in validChars:
    cutString += n

# this works for now, because I'm using a very small
# plantext file for testing.
print('ORIGINAL:\n'+fullString+'\n--- END ORIGINAL ------------')
print('RECOVERED:\n'+cutString+'\n--- END RECOVERED -----------')

newFilePath = os.path.dirname(globPath)
newFilePath += '/stripped-'
# could just inform the user that the file has
# already been created in [an identical] prev
# operation. however, this is a good technique
# to flesh out, because some apps will need it.

# while 1:
#     if os.path.isfile(os.path.join(newFilePath, os.path.basename(globPath))) is True:
#         newFilePath += 'stripped-'
#     else:

bFileExists = True
counter = '1'
while bFileExists:
    if os.path.isfile(os.path.join(newFilePath, os.path.basename(globPath))):
        newFilePath += counter
        counter = str(int(counter)+1)
    else:
        newFilePath += os.path.basename(globPath)
        bFileExists = False

wFile = open(newFilePath,mode='x') # can omit 'mode=' for just 'x'/'r'/'w'
if not wFile.writable():
    print('file not writable. aborting.')
    wFile.close()
else:
    wFile.write(cutString)
    wFile.close()
    if os.path.isfile(newFilePath):
        print('created file: '+newFilePath+'\n# EXITING APPLICATION -------------------')

''' # UNUSED GARBAGE
# extRegex = re.compile(r'([\S])+\.([\S]+)')
cutString = ''
for n in fullString:
    if fullString[n] == '\\n':
        continue
    else:
        cutString += fullString[n]
print(cutString)
'''