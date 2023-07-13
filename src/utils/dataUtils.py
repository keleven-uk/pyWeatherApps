###############################################################################################################
#    dataUtils.py   Copyright (C) <2023>  <Kevin Scott>                                                       #                                                                                                             #                                                                                                             #
#    A number of helper and utility functions                                                                 #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2023>  <Kevin Scott>                                                                     #
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

import os
import glob

import colorama

######################################################################################## loadExplorer() ######
def loadExplorer(logger):
    """  Load program working directory into file explorer.
    """
    try:
        os.startfile(os.getcwd(), "explore")
    except NotImplementedError as error:
        logger.error(error)

########################################################################################### listFiles() ######
def listFiles(targetFiles, screen=True):
    """  Produce a list of weather data files in the data directory.
         If screen is True [default], the file name will be printed to screen.

         NB  assumes it's run in the parent directory and the data files are in sub directory called data.'
    """
    dataFiles = glob.glob(targetFiles)

    if screen:
        for file in dataFiles:
            print(f"{colorama.Fore.YELLOW} Found data file {file}{colorama.Fore.RESET}")

    return(dataFiles)



