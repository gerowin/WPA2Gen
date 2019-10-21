#!/usr/bin/env python3
#This is a a program that will generate a randomized password
#of a specified length to use as a WPA/WPA2 password.
#These passwords can be used for other things as well if you wish.
#Marcus Dean Adams (marcusdean.adams@protonmail.com)
#Last updated: 2 October 2017

#Import needed libraries
import random, sys, time, os

#Welcome Message
print ( "\n\nWelcome to Marcus's WPA2Gen wifi password generator v17.10.2!\n" )
time.sleep(1)

#Attempt to import colorama for printing colored text
try:
	from colorama import Back
except ImportError:
	print ( "\nYou do not appear to have the colorama library installed, colored text will be disabled." )
	print ( "You can get the colorama library at https://pypi.python.org/pypi/colorama, or in your Linux package manger.\n" )
	input ( "Press Enter to continue: ")
	nocolor = "true"#The value of this variable is checked later to decide whether colored text can be displayed.
else:
	nocolor = "false"

#The dialogs that ask for a password length.
print ( "\n\nHow long would you like your password to be?\n" )
print ( "Please keep in mind, shorter passwords mean weaker encryption.\n" )
print ( "1) Light Security - 8 characters" )
print ( "2) Medium Security - 20 characters" )
print ( "3) Maximum Security - 63 characters (Recommended)\n" )
length = input ( "Choice [Default 63 chars]: " )

#Translate the value of length to the appropriate length of password.
if length == "1":
	length = 8
elif length == "2":
	length = 20
else:
	length = 63


#Generate random ascii values, then translate them to their corresponding
#character, and append them to the string that will be reported as the
#password.
pw = ""
for i in range ( length ):
	ascii = chr ( random.randint ( 33, 126 ) )
	pw += str ( ascii )
	
#Convert the value of length to a string for later usage.
length = str ( length )

#Report the password.
print ( "\nYour " + length + " character password is:\n" )
if nocolor == "false":	
	print ( Back.GREEN + pw + Back.RESET + "\n" )
else:
	print ( pw + "\n" )

#Offer to save the password since Windows doesn't let you copy text
#in the command line window, and so you can put it on a thumb stick
#to make it easier to update your various portable devices.

print ( "Would you like to save this password to a file on your \
desktop for later use?" )
print ( "\nSecurity tip: You should delete the file once you have \
connected all of your devices and no longer need it.\n" )
save = input ( "Yes(y) or No(n) [Default is no]: " )
save = save.lower()

if save == "yes" or save == "y":
	#Set variables to make later commands shorter and writes the password
	#to the appropriate location depending on operating system.
	timenow = time.strftime("%B-%d-%Y-%H-%M-%S")
	if os.name == "nt":
		path = os.environ [ 'USERPROFILE' ] + "\\Desktop\\" + "wifi-password-" + timenow + ".txt"
	else:
		path = os.environ [ 'HOME' ] + "/Desktop/" + "wifi-password-" + timenow + ".txt"
	
	#Write the password to a file
	dest = open ( path, "w" )
	dest.write ( "This " + length + " character password was generated at " + timenow + "\n\n" )
	dest.write ( pw )
	dest.close()
	
	#Display exit message
	print ( "\nThe file has been saved as " + path + "\n")
	input ( "Press Enter to exit" )
	print ( "Exiting..." )
	sys.exit(0)
	
else:
	print ( "Exiting..." )
	sys.exit(0)
