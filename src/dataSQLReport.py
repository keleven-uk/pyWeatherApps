###############################################################################################################
#    sql3Report   Copyright (C) <2023>  <Kevin Scott>                                                         #
#    stores the highs and low weather values.                                                                 #
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

import src.classes.sql3Data as DB
import src.classes.monthlyRecords as monthly
import src.classes.allTimeRecords as allTime

import src.utils.dataUtils as utils

from src.console import console

def report(mainDB, logger, verbose):
    """  Scans a given sqlite2 database and produces a report on high and low values.
    """

    monthlyRecords = monthly.monthlyRecords(mainDB)
    allTimeRecords = allTime.allTimeRecords()

    utils.logPrint(logger, verbose, f"Reporting on :: {mainDB}", "info")

    try:
        sql3DB = DB.sql3Data(mainDB)
    except Exception as e:
        print(e)
        sys.exit(1)


    # highLowValues = ("OutdoorTemperature", "OutdoorFeelsLike", "OutdoorDewPoint", "OutdoorHumidity",  "IndoorTemprature", "IndoorHumidity", "PressueRelative", "PressueAbsolute")
    # highValues = ("Solar", "UVI", "RainRate", "RainDaily", "RainEvent", "RainHourly", "RainWeekly", "WindSpeed", "WindGust")

    highLowValues = ("OutdoorTemperature",)

    with console.status("Reporting..."):
        for highLow in highLowValues:

            print(f"Processing {highLow}")

            sql3DB.execute(f"SELECT DateTime, MAX({highLow}) from DailyData")

            value    = sql3DB.fetchone()
            dt_value = value[0]
            mx_value = value[1]
            print(f"date = {dt_value}  max value = {mx_value}")

            sql3DB.execute(f"SELECT DateTime, MIN({highLow}) from DailyData")

            value    = sql3DB.fetchone()
            dt_value = value[0]
            mn_value = value[1]
            print(f"date = {dt_value}  max value = {mn_value}")

            #
            # for high in highValues:
            #     print(f"Processing {high}")
            #
            #     sql3DB.execute(f"SELECT DateTime, MAX({high}) from DailyData")
            #
            #     print(sql3DB.fetchone())


    monthlyRecords.save()





