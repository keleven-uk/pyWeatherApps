###############################################################################################################
#    pyDataBuild   Copyright (C) <2023>  <Kevin Scott>                                                        #
#    Scans a given directory for excel spreadsheets the contains weather data and for each                    #
#    new data adds them to a main spreadsheet.                                                                #
#                                                                                                             #
#  Usage:                                                                                                     #
#     pyDataBuild.py [-h] [-l] [-v] [-e]                                                                      #
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

import src.args as args
import src.Timer as Timer
import src.Config as Config
import src.Logger as Logger
import src.License as License
import src.weatherData as WD
import src.utils.dataUtils as utils


############################################################################################### __main__ ######

if __name__ == "__main__":


    Config = Config.Config()  # Need to do this first.
    LGpath = "logs\\" +Config.NAME +".log"
    logger = Logger.get_logger(LGpath)                        # Create the logger.

    args.parseArgs(Config.NAME, Config.VERSION, logger)

    timer = Timer.Timer()
    timer.Start()

    message = f"Start of {Config.NAME} {Config.VERSION}"

    print(message)
    logger.info("-" * 100)
    logger.info(message)
    logger.info(f"Running on {sys.version} Python")

    License.printShortLicense(Config.NAME, Config.VERSION, logger)

    dataFiles = utils.listFiles(screen=False)   #  Returns a list of excel spreadsheets

    if dataFiles == []:
        message = "ERROR : no data files to build"
        logger.error(message)
        print(f"{colorama.Fore.RED}{message}{colorama.Fore.RESET}")
        sys.exit(1)

    mainData = WD.WeatherData("data\\main.xlsx", screen=False)    #  Load the main spreadsheet - this is the running aggregate of weather data.
    print(f" Starting size of mainData : {mainData.countData()}")
    mainData.saveDataJson("mainStart.json")

    old_rows = 0
    new_rows = 0

    for file in dataFiles:                          #  Loop through excel spreadsheets
        newData = WD.WeatherData(file, screen=False)

        for _ in range(newData.countData()-1):      #  Iterate each row of each new spreadsheet.
            key, row = next(newData.nextRow())

            if (key in mainData):
                old_rows += 1
            else:
                new_rows += 1
                mainData.add(key, row)

        newData = None


    print(f" rows existing {old_rows} :: rows to be added {new_rows}")
    print(f" New size of mainData : {mainData.countData()}")
    mainData.saveDataJson("mainEnd.json")

    print(" Saving back to main.xlsx")
    mainData.saveData()

    timeStop = timer.Stop

    message = f" {Config.NAME} Completed :: {timeStop}"
    print(message)
    logger.info(message)
    logger.info(f"End of {Config.NAME} {Config.VERSION}")

    sys.exit(0)
