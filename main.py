###############################################################################################################
#    main.py   Copyright (C) <2023>  <Kevin Scott>                                                            #
#                                                                                                             #
#    pyWeatherApp - Builds a main spreadsheet out of individual daily spreadsheets.                           #
#                                                                                                             #
#  Usage:                                                                                                     #
#     main.py.py [-h] [-l] [-v] [-e]                                                                          #
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

     dataBuild.build(mainWB, targetFiles) - builds the main spreadsheet.
"""

import sys

import src.Timer as Timer
import src.Logger as Logger
import src.License as License
import src.buildArgs as args
import src.buildConfig as Config
import src.dataBuild as dataBuild
import src.utils.dataUtils as utils

if __name__ == "__main__":

    Config = Config.Config()  # Need to do this first.
    LGpath = "logs\\" +Config.NAME +".log"
    logger = Logger.get_logger(LGpath)                        # Create the logger.

    mainWB      = Config.MAIN_WB
    targetFiles = Config.TARGET_FILES

    args.parseArgs(Config.NAME, Config.VERSION, logger)

    timer = Timer.Timer()
    timer.Start()

    utils.logPrint(logger, False, "-" * 100)
    utils.logPrint(logger, True, f"Start of {Config.NAME} {Config.VERSION}")
    utils.logPrint(logger, False, f"Running on {sys.version} Python")

    License.printShortLicense(Config.NAME, Config.VERSION, logger)

    dataBuild.build(mainWB, targetFiles, logger)


    timeStop = timer.Stop

    utils.logPrint(logger, True, f"{Config.NAME} Completed :: {timeStop}")
    utils.logPrint(logger, True, f"End of {Config.NAME} {Config.VERSION}")

    sys.exit(0)
