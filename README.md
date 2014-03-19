CPRGenerator
============

Python script that will generate all the possible CPR (Personal identification number) for a given date of birth and gender.

```
usage: CPRGenerator.py [-h] [-c] dob gender

CPR (Personal identification number) generator.
Example: CPRGenerator.py 101299 male

This will generate almost all possible CPR numbers for a male born
on the 10th December 1999

positional arguments:
  dob          the date of birth in the format DDMMYY for the generated CPR
               numbers
  gender       the gender for the generated CPR numbers

optional arguments:
  -h, --help   show this help message and exit
  -c, --count  print the number of generated CPR numbers

```
