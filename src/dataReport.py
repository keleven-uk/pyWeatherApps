###############################################################################################################
#    pyDataBuild   Copyright (C) <2023>  <Kevin Scott>                                                        #
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

import src.weatherData as WD
import src.utils.dataUtils as utils

def report(mainWB, logger):
    """  Scans a given spreadsheet and produces a report in min and max values.
    """


    mainData = WD.WeatherData(mainWB, screen=True)    #  Load the main spreadsheet - this is the running aggregate of weather data.git status
    if mainData.countData() !=0:
        print(f" Starting size of mainData : {mainData.countData()}")
    else:
        utils.logPrint(logger, True, "No entires in main spreadsheet - mayber rin build first", Red)
        sys.exit(1)


    for _ in range(mainData.countData()-1):      #  Iterate each row of each new spreadsheet.
        key, row = next(mainData.nextRow())
        print(key, row)




