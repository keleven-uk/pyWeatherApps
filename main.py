###############################################################################################################
#    main.py   Copyright (C) <2023>  <Kevin Scott>                                                            #
#                                                                                                             #
#    pyWeatherApp - Builds a main database out of individual daily spreadsheets.                              #
#                   The main database can be either a Excel spreadsheet or a SQLite3 database.                #
#                                                                                                             #
#  Usage:                                                                                                     #
#     main.py [-h] for help.                                                                                  #
#                                                                                                             #
#     For changes see history.txt                                                                             #
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

"""  pyWeatherApp - Builds a main spreadsheet out of individual daily spreadsheets.

     dataBuild.build(mainWB, targetFiles, logger, verbose) - builds the main spreadsheet.
     dataReportreport(mainWB, logger, verbose) - scans the main file and finds the highs and lows.
"""

import sys

import src.args as args
import src.timer as Timer
import src.config as Config
import src.logger as Logger
import src.license as License
import src.dataXBuild as dataXBuild
import src.dataXReport as dataXReport
import src.dataSQLBuild as dataSQLBuild
import src.dataSQLReport as dataSQLReport

import src.utils.dataUtils as utils


if __name__ == "__main__":

    Config = Config.Config()  # Need to do this first.
    LGpath = "logs\\" +Config.NAME +".log"
    logger = Logger.get_logger(LGpath)                        # Create the logger.

    mainWB             = Config.MAIN_WB
    mainDB             = Config.MAIN_DB
    DB_TYPE            = Config.DB_TYPE
    recordFiles        = Config.RECORD_FILES
    targetFiles        = Config.TARGET_FILES
    yearRecordFiles    = Config.YEAR_RECORD_FILES
    allTimeRecordsFile = Config.ALLTIME_RECORD_FILES

    build, report, ATreport, infile, verbose, create, config, month, year = args.parseArgs(Config, logger)

    timer = Timer.Timer()
    timer.Start()

    License.printShortLicense(Config.NAME, Config.VERSION, logger)

    utils.logPrint(logger, False, "-" * 100, "info")
    utils.logPrint(logger, True, f"Start of {Config.NAME} {Config.VERSION}", "info")

    if not create and not config and not build and not report and not ATreport:
        utils.logPrint(logger, True, "No mode given, please state either config, build or report - main.py -h for help", "warning")

    #  If month and year are supplied from the command line use them, if not use from config file.
    if month and year:
        mainWB, mainDB, recordFiles, targetFiles = utils.buildFileNames(Config.DATA_DIR, Config.REC_DIR, Config.DB_DIR, month, year, Config.TARGET)
    else:
        month = Config.MONTH
        year  = Config.YEAR

    if config:
        utils.printConfig(logger, Config.NAME, Config.VERSION, mainWB, mainDB, recordFiles, targetFiles, DB_TYPE, month, year)
        sys.exit(0)

    if DB_TYPE == "sqlite":
        utils.logPrint(logger, verbose, f"Running on {sys.version} Python", "info")
        utils.logPrint(logger, verbose, f"Running on {utils.sqlite3Version()} SQLite3", "info")
    else:
        utils.logPrint(logger, verbose, f"Running on {sys.version} Python", "info")

    if create:                                  #  only create if we are in SQLite3 mode.
        if DB_TYPE == "sqlite":
            utils.logPrint(logger, True, "Creating SQLite3 database and tables", "info")
            dataSQLBuild.build(mainDB, targetFiles, logger, verbose, create)
        else:
            utils.logPrint(logger, True, f"Cannot create SQLite3 database on DB TYPE {DB_TYPE}", "warning")

    if build:
        if DB_TYPE == "excel":
            utils.logPrint(logger, True, "Running build to EXCEL", "info")
            dataXBuild.build(mainWB, targetFiles, logger, verbose)
        elif DB_TYPE == "sqlite":
            try:
                print(f"DB file name = {mainDB}")
                utils.logPrint(logger, True, "Running build to SQLite", "info")
                dataSQLBuild.build(mainDB, targetFiles, logger, verbose)
            except Exception as e:
                utils.logPrint(logger, verbose, f"{e}.  Maybe run main.py -c", "warning")
        else:
            utils.logPrint(logger, verbose, "ERROR: Unkown DB type", "danger")

    if report or ATreport:
        if DB_TYPE == "sqlite":
            utils.logPrint(logger, True, f"Running report on SQLite3 database - {mainDB}", "info")
            dataSQLReport.report(mainDB, recordFiles, yearRecordFiles, allTimeRecordsFile, month, year, logger, verbose, ATreport)
        else:
            dataXReport.report(mainWB, logger, verbose)



    timeStop = timer.Stop

    print("")
    utils.logPrint(logger, True, f"{Config.NAME} Completed :: {timeStop}", "info")
    utils.logPrint(logger, True, f"End of {Config.NAME} {Config.VERSION}", "info")
    utils.logPrint(logger, False, "-" * 100, "info")

    sys.exit(0)
