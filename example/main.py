
from src import functions
from src import getsave as gs


## ur code here
## here is an example of code but it is bullshit

b = int(input('Entrez un nombre'))
print('son carre est',functions.square(b))

gs.save_files('.')


## try to launch me ! a repertory called 'autosav' should be appear with inside several files:
##          - one file 'version' that remember which version of ur code is running
##          - one or more files 'saved_*.savd' (* is the version of each .savd file)
##
## u can now try to extract source code from .savd using getback.py
