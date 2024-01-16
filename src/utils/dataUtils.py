###############################################################################################################
#    dataUtils.py   Copyright (C) <2023 - 2024>  <Kevin Scott>                                                #                                                                                                             #
#    A number of helper and utility functions                                                                 #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2023 - 2024>  <Kevin Scott>                                                               #
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
import shutil
import pathlib

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
        if newValue is None:                 #  An inserted value, so ignore.
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

############################################################################################ printConfig() ######
def printConfig(logger, name, version, mainWB, mainDB, recordFiles, yearRecordFiles, allTimeRecordsFile, targetFiles, DB_TYPE, month, year):
    """  Prints out a list of the current config values.
    """
    logPrint(logger, True, "List of Config Values", "info")
    logPrint(logger, True, f"App Name                     :: {name}",    "info")
    logPrint(logger, True, f"Current Version              :: {version}", "info")
    logPrint(logger, True, f"Location of main WB          :: {mainWB}", "info")
    logPrint(logger, True, f"Location of main DB          :: {mainDB}", "info")
    logPrint(logger, True, f"Location of records          :: {recordFiles}", "info")
    logPrint(logger, True, f"Location of yearly records   :: {yearRecordFiles}", "info")
    logPrint(logger, True, f"Location of all time records :: {allTimeRecordsFile}", "info")
    logPrint(logger, True, f"Location of target           :: {targetFiles}", "info")
    logPrint(logger, True, f"Current data type            :: {DB_TYPE}", "info")
    logPrint(logger, True, f"Current year                 :: {month}", "info")
    logPrint(logger, True, f"Current month                :: {year}", "info")

########################################################################################### buildFileName() ######
def buildFileNames(config):
    """  Builds a new set on config values from arguments supplied at the command line.
    """
    data_dir = config.DATA_DIR
    rec_dir  = config.REC_DIR
    db_dir   = config.MAIN_DB
    xl_dir   = config.XL_DIR
    month    = config.MONTH
    year     = config.YEAR
    target   = config.TARGET_FILES

    mainWB = f"{data_dir}\\{year}\\{db_dir}\\{month}{year}.xlsx"
    mainDB = f"{data_dir}\\{year}\\{db_dir}\\{month}{year}.sql"
    recordFiles = f"{data_dir}\\{year}\\{rec_dir}\\{month}{year}.pickle"
    targetFiles = f"{data_dir}\\{year}\\{xl_dir}\\{month}\\{target}"

    return mainWB, mainDB, recordFiles, targetFiles

########################################################################################### checkPaths() #########
def checkPaths(config, logger, verbose):
    """  Checks the data directories exist, if not create them.
    """

    logPrint(logger, verbose, "Checking Paths", "info")

    mainDB             = config.MAIN_DB
    targetFiles        = config.TARGET_FILES
    monthlyRecordFile  = config.RECORD_FILES

    mainDB_path            = pathlib.Path(mainDB).parent
    targetFiles_path       = pathlib.Path(targetFiles).parent
    monthlyRecordFile_path = pathlib.Path(monthlyRecordFile).parent

    if mainDB_path.exists():
        logPrint(logger, verbose, f"{mainDB_path} exists", "info")
    else:
        logPrint(logger, verbose, f"{mainDB_path} doesn't exists, will create", "warning")
        mainDB_path.mkdir(parents=True)

    if targetFiles_path.exists():
        logPrint(logger, verbose, f"{targetFiles_path} exists", "info")
    else:
        logPrint(logger, verbose, f"{targetFiles_path} doesn't exists, will create", "warning")
        targetFiles_path.mkdir(parents=True)

    if monthlyRecordFile_path.exists():
        logPrint(logger, verbose, f"{monthlyRecordFile_path} exists", "info")
    else:
        logPrint(logger, verbose, f"{monthlyRecordFile_path} doesn't exists, will create", "warning")
        monthlyRecordFile_path.mkdir(parents=True)

############################################################################################# makeArchive() ######
def makeArchive(tofile, config, logger):
    """  Create an archive at tofile containing the data directory.

         NB : No extension should be supplies with the filename.
              The correct extension according to the type of archive will be added.
    """
    type     = config.ARCHIVE_TYPE
    data_dir = config.DATA_DIR

    try:
        shutil.make_archive(base_name=f"{tofile}", format=f"{type}", root_dir=".", base_dir=f"{data_dir}")
    except Exception as e:
        logPrint(logger, True, f"{e}.  ERROR : Archive save", "warning")

############################################################################################# loadArchive() ######
def loadArchive(fromfile, config, logger):
    """  Create an archive at tofile containing the data directory.

         NB : the file extension should be supplied with the filename.
              The unpack method uses the extension to determine the type of the archive.
    """
    if not fromfile.exists():
        logPrint(logger, True, f"{fromfile} does not exists", "info")
        return

    try:
        shutil.unpack_archive(filename=f"{fromfile}", extract_dir=".")
    except Exception as e:
        logPrint(logger, True, f"{e}.  ERROR : Archive load", "warning")







