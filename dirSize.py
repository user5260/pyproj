'''
dirSize.py
----------
Prints the total size of the
current working directory and
each of the files contained
within it (seems to have a
problem with hidden dirs,
e.g. '../.hiddenrc/'.

[Comments]
Would like to display sizes in
MB rather than bytes. An easy
fix.

brianc2788@gmail.com
github.com/user5260/pyscripts
'''
import os

sizeofcwd = 0

for file in os.listdir(os.getcwd()):
    print(file + ", " + str(os.path.getsize(os.path.join(os.getcwd(),file))) + ' bytes')
    sizeofcwd += os.path.getsize(os.path.join(os.getcwd(),file))

print('Total Dir Size: ' + str(sizeofcwd) + ' bytes')