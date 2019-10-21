README

WPA2Gen 17.10.2
Marcus Dean Adams (marcusdean.adams@protonmail.com)
2 October 2017

PURPOSE
----------------------------------------------------------------
The purpose of this program is to make it quick and easy to generate
secure passwords/encryption keys for WPA/WPA2 wireless networks.

HOW TO USE
----------------------------------------------------------------
1) If installing, just double click the icon and follow the directions.
2) If using the "source" version, you must have Python 3 installed;
   then just double click the "wpa2gen.py" file and follow directions.

WHAT DOES IT DO TO MY COMPUTER?
----------------------------------------------------------------
1) If running the installer, it installs the program files to the
   directory specified.
2) If you choose to save the password to a text file, it saves the
   text file to the "Desktop" folder in the current user's profile.

THINGS TO REMEMBER
----------------------------------------------------------------
- The source code version depends on Python 3, but will run on any machine
  regardless of whether its' 32 or 64 bit
- The Windows installer is 64 bit only
- The password generator only has 63 characters as an option and not 64
  because I have personally had issues with certain devices supporting WPA2,
  but not 64 character passwords for WPA2, but they worked fine with 63.
- Even if you use the compiled Windows installer, there is a "source"
  subfolder in the installation directory that contains the plain text
  Python executable that can be ran if you have Python installed, or
  examined if you wish to read the source code.
- The PNG version of the icon file is included for your convenience in case
  you are using a *nix based system and wish to create your own desktop shortcut.

LICENSING
----------------------------------------------------------------
If you make any changes to this software, be sure to annotate those
changes in the changelog.txt file.  Be sure to append the date, your
name and a way to contact you (website, e-mail, etc.).  You can use
my entries as a template.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses
