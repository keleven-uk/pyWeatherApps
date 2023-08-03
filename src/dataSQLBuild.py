###############################################################################################################
#    pyDataSQLBuild   Copyright (C) <2023>  <Kevin Scott>                                                     #
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
import src.classes.sql3Data as DB
import src.utils.dataUtils as utils

from src.console import console

def build(mainDB, targetFiles, logger, verbose, create=False):
    """  Scans a given directory for excel spreadsheets the contains weather data and for
         each new data adds them to a main spreadsheet.
         if create os not supplied, default to False.
    """

    print(f"Building SQL in :: {mainDB}")

    try:
        sql3DB = DB.sql3Data(mainDB)
    except Exception as e:
        print(e)
        sys.exit(1)

    if create:                               #  Create the table - should be on a new database.
        try:
            sql3DB.createTable()
            sys.exit(0)
        except Exception as e:
            print(e)
            sys.exit(1)

    dataFiles = utils.listFiles(targetFiles, verbose)   #  Returns a list of excel spreadsheets

    if dataFiles == []:
        utils.logPrint(logger, True, "ERROR : no data files to build", "warning")
        sys.exit(1)

    #Fetching all row from the table
    results = sql3DB.fetchall()

    if len(results) !=0:
        utils.logPrint(logger, verbose, f"Size of mainData : {len(results)}", "info")

    old_rows = 0
    new_rows = 0

    with console.status("Scanning..."):
        for file in dataFiles:   #  Loop through excel spreadsheets
            console.log(file)
            newData = WD.WeatherData(file, screen=verbose)

            for _ in range(newData.countData()-1):      #  Iterate each row of each new spreadsheet.
                key, row = next(newData.nextRow())

                if sql3DB.keyExists(key):
                    old_rows += 1
                else:
                    new_rows += 1
                    sql3DB.insert([key,
                                   row.OutdoorTemperature,
                                   row.OutdoorFeelsLike,
                                   row.OutdoorDewPoint,
                                   row.OutdoorHumidity,
                                   row.IndoorTemperature,
                                   row.IndoorHumidity,
                                   row.Solar,
                                   row.UVI,
                                   row.RainRate,
                                   row.RainDaily,
                                   row.RainEvent,
                                   row.RainHourly,
                                   row.RainWeekly,
                                   row.RainMonthly,
                                   row.RainYearly,
                                   row.WindSpeed,
                                   row.WindGust,
                                   row.WindDirection,
                                   row.PressureRelative,
                                   row.PressureAbsolute])

            newData = None

    #Fetching all row from the table
    results = sql3DB.fetchall()

    utils.logPrint(logger, True, f" rows existing {old_rows} :: rows to be added {new_rows}", "info")
    utils.logPrint(logger, True, f" New size of mainData : {len(results)}", "info")





