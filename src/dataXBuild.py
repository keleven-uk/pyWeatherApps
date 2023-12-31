###############################################################################################################
#    pyDataXBuild   Copyright (C) <2023>  <Kevin Scott>                                                       #
#    Scans a given directory for excel spreadsheets the contains weather data and for each                    #
#    new data adds them to a main spreadsheet.                                                                #
#                                                                                                             #
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

import src.classes.weatherData as WD
import src.utils.dataUtils as utils

from src.console import console

def build(mainWB, targetFiles, logger, verbose):
    """  Scans a given directory for excel spreadsheets the contains weather data and for
         each new data adds them to a main spreadsheet.
    """

    dataFiles = utils.listFiles(targetFiles, verbose)   #  Returns a list of excel spreadsheets

    if dataFiles == []:
        utils.logPrint(logger, True, "ERROR : no data files to build", "warning")
        sys.exit(1)

    mainData = WD.WeatherData(mainWB, screen=verbose)    #  Load the main spreadsheet - this is the running aggregate of weather data.git status
    if mainData.countData() !=0:
        utils.logPrint(logger, verbose, "Size of mainData : {mainData.countData()}", "info")

    old_rows = 0
    new_rows = 0

    with console.status("Building main..."):
        for file in dataFiles:   #  Loop through excel spreadsheets
            #console.log(file)
            newData = WD.WeatherData(file, screen=False)

            for _ in range(newData.countData()-1):      #  Iterate each row of each new spreadsheet.
                key, row = next(newData.nextRow())

                if (key in mainData):
                    old_rows += 1
                else:
                    new_rows += 1
                    mainData.add(key, row)

            newData = None


    utils.logPrint(logger, True, f" rows existing {old_rows} :: rows to be added {new_rows}", "info")
    utils.logPrint(logger, True, f" New size of mainData : {mainData.countData()}", "info")
    utils.logPrint(logger, True, f" Saving back to {mainWB}", "info")

    mainData.saveData()


