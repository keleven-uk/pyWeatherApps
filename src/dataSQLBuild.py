###############################################################################################################
#    pyDataSQLBuild   Copyright (C) <2023 - 2024>  <Kevin Scott>                                              #
#    Scans a given directory for excel spreadsheets the contains weather data and for each                    #
#    new data adds them to a main spreadsheet.                                                                #
#                                                                                                             #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2023>  <Kevin Scott - 2024>                                                               #
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
import src.classes.sql3Data as DB
import src.utils.dataUtils as utils

from src.console import console

def build(mainDB, targetFiles, logger, verbose, create=False):
    """  Scans a given directory for excel spreadsheets the contains weather data and for
         each new data adds them to a main spreadsheet.
         if create is not supplied, default to False.
    """

    utils.logPrint(logger, verbose, f"Building SQL in :: {mainDB}", "info")

    try:
        sql3DB = DB.sql3Data(mainDB)
    except Exception as e:
        print(e)
        sys.exit(1)

    if create:                               #  Create the table - should be on a new database.
        try:
            sql3DB.createTable()
            utils.logPrint(logger, "True", "SQLite3 tables created successfully.", "info")
            return
        except Exception as e:
            utils.logPrint(logger, verbose, f"{e}.", "info")
            return

    dataFiles = utils.listFiles(targetFiles, verbose)   #  Returns a list of excel spreadsheets

    if dataFiles == []:
        utils.logPrint(logger, True, "ERROR : no data files to build", "warning")
        sys.exit(1)

    #Fetching all row from the table
    count = sql3DB.count()

    if count !=0:
        utils.logPrint(logger, verbose, f"Size of mainData : {count}", "info")

    oldRows  = 0
    newRows  = 0
    noOfDays = 0
    rainDays = 0
    dryDays  = 0

    with console.status("Scanning..."):
        for file in dataFiles:   #  Loop through excel spreadsheets
            newData = WD.WeatherData(file, screen=verbose)
            noOfDays += 1

            for _ in range(newData.countData()-1):      #  Iterate each row of each new spreadsheet.
                key, row = next(newData.nextRow())

                year  = key[0:4]
                month = key[5:7]
                day   = key[8:10]

                if sql3DB.keyExists(key):
                    oldRows += 1
                else:
                    newRows += 1
                    sql3DB.insert([key,
                                   day,
                                   month,
                                   year,
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
                                   row.PressureAbsolute
                                   ])

            #  values should be the last for the day.
            if row.RainDaily:
                rainDays += 1
            else:
                dryDays += 1

        sql3DB.insertXtra(["RainDays", noOfDays, rainDays, month, year])
        sql3DB.insertXtra(["DryDays" , noOfDays, dryDays, month, year])

    #Fetching all row from the table
    count = sql3DB.count()

    utils.logPrint(logger, True, f" Number of data files : {noOfDays}", "info")
    utils.logPrint(logger, True, f" Number of rain days  : {rainDays}", "info")
    utils.logPrint(logger, True, f" rows existing {oldRows} :: rows to be added {newRows}", "info")
    utils.logPrint(logger, True, f" New size of mainData : {count}", "info")






