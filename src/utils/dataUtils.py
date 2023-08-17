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
import sqlite3

from src.console import console


######################################################################################## sqlite3Version() ####
def sqlite3Version():
    """  Returns the current sqlite3 version as a string.
    """
    return sqlite3.sqlite_version

######################################################################################## loadExplorer() ######
def loadExplorer(logger):
    """  Load program working directory into file explorer.
    """
    try:
        os.startfile(os.getcwd(), "explore")
    except NotImplementedError as error:
        logger.error(error)

########################################################################################### logPrint() #######
def logPrint(logger, verbose, message, style):
    """  If a logger is supplied, log message.
         If screen is True, print message to screen.
    """
    if logger:
        logger.info(message)

    if verbose:
        if style == "warning":
            console.log(f"{message}", style="warning")
        else:
            console.log(f"{message}", style="info")

########################################################################################### listFiles() ######
def listFiles(targetFiles, verbose):
    """  Produce a list of weather data files in the data directory.
         If screen is True [default], the file name will be printed to screen.

         NB  assumes it's run in the parent directory and the data files are in sub directory called data.'
    """
    dataFiles = glob.glob(targetFiles)

    if verbose:
        for file in dataFiles:
            console.log(f"Found data file :: {file}", style="info")

    return(dataFiles)


############################################################################################### maxMin() ######
def maxMin(recordValue, newValue, recordDate, newDate, mode):
    """  Checks to see if a newValue is greater of less then the recordValue.
         Returns the new record values with the corresponding date.
    """
    if mode == "MAX":
        if newValue == 200.0:                 #  An inserted value, so ignore.
            return recordValue, recordDate
        elif newValue > recordValue:
            return newValue, newDate
        else:
            return recordValue, recordDate

    if mode == "MIN":
        if newValue < recordValue:
            return newValue, newDate
        else:
            return recordValue, recordDate






