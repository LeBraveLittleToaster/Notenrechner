# Notenrechner
Enter your marks in the noten.txt file in the following format:

<Subject name>|<Amount of Points>|<Grade>

Run "python Notenrechner.py <options>"

Possible options:

-t <some Integer>   => Integer, only takes the best "t" points in the average calculation
-a                  => use all points, if -t is present, then -a is ignored
-f <filename.txt>   => filename, put a file in the same directory as Notenrechner.py and put the filename with .txt extentions behind -f

Built with python 3.7