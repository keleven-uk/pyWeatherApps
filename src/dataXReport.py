###############################################################################################################
#    dataReport   Copyright (C) <2023>  <Kevin Scott>                                                         #
#    Scans the previously built main data for min and max values.                                             #
#    new data adds them to a main spreadsheet.                                                                #
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

def report(mainWB, logger, verbose):
    """  Scans a given spreadsheet and produces a report in min and max values.
    """
    maxOutdoorTemperature     = 0
    maxOutdoorTemperatureDate = ""
    minOutdoorTemperature     = 100
    minOutdoorTemperatureDate = ""

    maxIndoorTemperature     = 0
    maxIndoorTemperatureDate = ""
    minIndoorTemperature     = 100
    minIndoorTemperatureDate = ""

    maxRainRate     = 0
    maxRainRateDate = ""

    maxRainDaily     = 0
    maxRainDailyDate = ""

    mainData = WD.WeatherData(mainWB, screen=verbose)    #  Load the main spreadsheet - this is the running aggregate of weather data.

    if mainData.countData() !=0:
        utils.logPrint(logger, verbose, "Size of mainData : {mainData.countData()}", "info")
    else:
        utils.logPrint(logger, True, "No entries in main spreadsheet - maybe run build first", "warning")
        sys.exit(1)


    with console.status("Scanning..."):
        for _ in range(mainData.countData()-1):      #  Iterate each row of each new spreadsheet.
            date, row = next(mainData.nextRow())

            maxOutdoorTemperature, maxOutdoorTemperatureDate = utils.maxMin(maxOutdoorTemperature, row.OutdoorTemperature, maxOutdoorTemperatureDate, date, "MAX")
            minOutdoorTemperature, minOutdoorTemperatureDate = utils.maxMin(minOutdoorTemperature, row.OutdoorTemperature, minOutdoorTemperatureDate, date, "MIN")

            maxIndoorTemperature, maxIndoorTemperatureDate = utils.maxMin(maxIndoorTemperature, row.IndoorTemperature, maxIndoorTemperatureDate, date, "MAX")
            minIndoorTemperature, minIndoorTemperatureDate = utils.maxMin(minIndoorTemperature, row.IndoorTemperature, minIndoorTemperatureDate, date, "MIN")

            maxRainRate, maxRainRateDate = utils.maxMin(maxRainRate, row.RainRate, maxRainRateDate, date, "MAX")

            maxRainDaily, maxRainDailyDate = utils.maxMin(maxRainDaily, row.RainDaily, maxRainDailyDate, date, "MAX")


    console.rule("Results")
    print(f" The max outdoor temp {maxOutdoorTemperature} occurred on {maxOutdoorTemperatureDate}")
    print(f" The min outdoor temp {minOutdoorTemperature} occurred on {minOutdoorTemperatureDate}")

    print(f" The max indoor temp {maxIndoorTemperature} occurred on {maxIndoorTemperatureDate}")
    print(f" The min indoor temp {minIndoorTemperature} occurred on {minIndoorTemperatureDate}")

    print(f" The max Rain Rate {maxRainRate} occurred on {maxRainRateDate}")

    print(f" The max Rain Daily {maxRainDaily} occurred on {maxRainDailyDate}")
    console.rule("")





