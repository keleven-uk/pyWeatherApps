###############################################################################################################
#    myLicense.py   Copyright (C) <2023>  <Kevin Scott>                                                       #
#                                                                                                             #
#    Two methods to print out License information, one short and one long.                                    #
#    One method to either print text to screen or a file.                                                     #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2023>  <Kevin Scott>                                                                      #
#                                                                                                             #
#    This program is free software: you can redistribute it and/or modify it under the terms of the           #
#    GNU General Public License as published by the Free Software Foundation, either Version 3 of the         #
#    License, or (at your option) any later Version.                                                          #
#                                                                                                             #
#    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without        #
#    even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#    GNU General Public License for more details.                                                             #
#                                                                                                             #
#    You should have received a copy of the GNU General Public License along with this program.               #
#    If not, see <http://www.gnu.org/licenses/>.                                                              #
#                                                                                                             #
###############################################################################################################

########################################################################################### printSortLicense ######
def printShortLicense(name, version, logger, screen=True):
    logger.info("")
    logger.info(f"{name} {version}   Copyright (C) 2023  Kevin Scott")
    logger.info(f"This program comes with ABSOLUTELY NO WARRANTY; for details type `{name} -l'.")
    logger.info("This is free software, and you are welcome to redistribute it under certain conditions.")
    logger.info("")
    if screen:
        print("")
        print(f"{name} {version}   Copyright (C) 2023  Kevin Scott")
        print(f"This program comes with ABSOLUTELY NO WARRANTY; for details type `{name} -l'.")
        print("This is free software, and you are welcome to redistribute it under certain conditions.")
        print("")
########################################################################################### printLongLicense ######
def printLongLicense(name, version):
    print(f"""
    {name} {version}  Copyright (C) 2023  Kevin Scott

    This program is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either myVERSION 3 of the License, or
    (at your option) any later myVERSION.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    """, end="")
