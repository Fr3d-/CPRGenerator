#!/usr/bin/env python

import sys, argparse

def generate( dateOfBirth, gender ):
	controlNumber = "432765432"
	check = 0
	count = 0
	results = [];

	# Generate all possible numbers from 0-1000 except for 500-899 as they're reserved for people either born in 18th or 20th century
	for i in range( 0, 1000 ):
		if( i < 500 or i > 899 ):
			cpr = dateOfBirth + str( i ).zfill( 3 )

			for i in range( 9 ):
				check = check + int( cpr[i] ) * int( controlNumber[i] )
			lastdigit = 11 - ( check % 11 )

			if( lastdigit < 10 ):
				if( ( lastdigit % 2 == 0 and gender == 0 ) or ( lastdigit % 2 != 0 and gender == 1 ) ): # Gender test

					year = int( cpr[4:6] )
					#seventh = int( cpr[6] )

					#if( year > 0 and year < 37 and ( seventh == 4 or seventh == 9 ) ): # If the 7th digit is either 4 or 9 and they're born between 00-37 then they're born in 2000 and are therefore irrelevant
					#	pass
					#else:
					count = count + 1
					results.append( cpr + str( lastdigit ) )
		i = i + 1
		check = 0
	return results, count

if __name__ == "__main__":
	parser = argparse.ArgumentParser( formatter_class=argparse.RawDescriptionHelpFormatter, description=
"""CPR (Personal identification number) generator.
Example: %(prog)s 101299 male

This will generate almost all possible CPR numbers for a male born
on the 10th December 1999"""
	)
	parser.add_argument("-c", "--count", help="print the number of generated CPR numbers", action="store_true")
	parser.add_argument("dob", help="the date of birth in the format DDMMYY for the generated CPR numbers")
	parser.add_argument("gender", help="the gender for the generated CPR numbers")
	args = parser.parse_args()

	if( args.gender == "male"):
		gender = 1
	elif( args.gender == "female"):
		gender = 0
	else:
		sys.exit("Invalid argument: gender can be either female or male.")

	if( int( args.dob ) < 010100 or int( args.dob ) > 311299):
		sys.exit("Invalid argument: The date of birth has to be the following format DDMMYY")	
	results, count = generate( args.dob, gender )

	for CPR in results:
		print( CPR )
		
	if( args.count ):
		print( count )
		
