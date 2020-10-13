# getback
tool in python to extract several code files from a .savd file (principally used with delta2d for now)



The use of getback.py works in pair with the use of the tool getsave.py :

running getsave.py creates a .savd file that will save all your python files in the directory u chosed.
running getback.py extracts all the py files from the .savd file so u can run ur program

benefit :
The advantage of using that tool is that u can easily save a version of ur code (a program, a game or whatever) into a .savd file
in order to get it back if the further modifications broke it up.
(minor but more convenient version of git if u want)

You can easily call the getsave.py file within your code in order to create a .savd each time u run ur code
(see examples in a near future chalah)
So ur code is saved each time u play it.
Ok the way code is saved in the .savd file is gross and so a .savd can be heavy but it is a very safe way not to lose code.