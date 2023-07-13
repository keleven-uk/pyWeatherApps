###############################################################################################################
#    main.py   Copyright (C) <2023>  <Kevin Scott>                                                            #
#                                                                                                             #
#    new data adds them to a main spreadsheet.                                                                #
#                                                                                                             #
#  Usage:                                                                                                     #
#     main.py.py [-h] [-l] [-v] [-e]                                                                      #
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

import sys

import colorama

import src.Timer as Timer
import src.Logger as Logger
import src.License as License
import src.buildArgs as args
import src.buildConfig as Config
import src.dataBuild as dataBuild

if __name__ == "__main__":

    Config = Config.Config()  # Need to do this first.
    LGpath = "logs\\" +Config.NAME +".log"
    logger = Logger.get_logger(LGpath)                        # Create the logger.

    mainWB      = Config.MAIN_WB
    targetFiles = Config.TARGET_FILES

    args.parseArgs(Config.NAME, Config.VERSION, logger)

    timer = Timer.Timer()
    timer.Start()

    message = f"Start of {Config.NAME} {Config.VERSION}"

    print(message)
    logger.info("-" * 100)
    logger.info(message)
    logger.info(f"Running on {sys.version} Python")

    License.printShortLicense(Config.NAME, Config.VERSION, logger)

    dataBuild.build(mainWB, targetFiles)


    timeStop = timer.Stop

    message = f" {Config.NAME} Completed :: {timeStop}"
    print(message)
    logger.info(message)
    logger.info(f"End of {Config.NAME} {Config.VERSION}")

    sys.exit(0)
