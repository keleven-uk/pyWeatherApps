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
import src.classes.yearlyRecords as yearly
import src.classes.allTimeRecords as allTime

import src.utils.dataUtils as utils

from src.console import console

def report(mainDB, monthlyrecordFiles, yearlyRecordsFile, allTimeRecordsFile, month, year, logger, verbose, Areport, Yreport):
    """  Scans a given sqlite3 database and produces a report on high and low values.
    """

    monthlyRecords = monthly.monthlyRecords(monthlyrecordFiles)
    allTimeRecords = allTime.allTimeRecords(allTimeRecordsFile)
    yearlyRecords  = yearly.yearlyRecords(yearlyRecordsFile)

    utils.logPrint(logger, verbose, f"Reporting on :: {mainDB}", "info")

    try:
        sql3DB = DB.sql3Data(mainDB)
    except Exception as e:
        print(e)
        sys.exit(1)


    #  WindDirection not added yet.
    highLowValues = ("OutdoorTemperature", "OutdoorFeelsLike", "OutdoorDewPoint", "OutdoorHumidity",  "IndoorTemprature", "IndoorHumidity", "PressueRelative", "PressueAbsolute")
    highValues = ("Solar", "UVI", "RainRate", "RainEvent", "RainHourly", "RainDaily", "RainWeekly", "RainMonthly", "RainYearly", "WindSpeed", "WindGust")

    with console.status("Reporting..."):
        for highLow in highLowValues:

            utils.logPrint(logger, verbose, f"Processing {highLow}", "info")

            sql3DB.execute(f"SELECT DateTime, MAX({highLow}) from DailyData")
            value    = sql3DB.fetchone()
            dt_value = value[0]
            mx_value = value[1]
            utils.logPrint(logger, verbose, f"date = {dt_value}  max value = {mx_value}", "info")

            monthlyRecords.add(f"{highLow}_MAX", mx_value, dt_value)
            yearlyRecords.add(f"{highLow}_MAX",  mx_value, dt_value)
            allTimeRecords.add(f"{highLow}_MAX", mx_value, dt_value)

            sql3DB.execute(f"SELECT DateTime, MIN({highLow}) from DailyData")
            value    = sql3DB.fetchone()
            dt_value = value[0]
            mn_value = value[1]
            utils.logPrint(logger, verbose, f"date = {dt_value}  max value = {mn_value}", "info")

            monthlyRecords.add(f"{highLow}_MIN", mn_value, dt_value)
            yearlyRecords.add(f"{highLow}_MIN",  mn_value, dt_value)
            allTimeRecords.add(f"{highLow}_MIN", mn_value, dt_value)

        for high in highValues:
            utils.logPrint(logger, verbose, f"Processing {high}", "info")

            sql3DB.execute(f"SELECT DateTime, MAX({high}) from DailyData")
            value    = sql3DB.fetchone()
            dt_value = value[0]
            mx_value = value[1]
            utils.logPrint(logger, verbose, f"date = {dt_value}  max value = {mx_value}", "info")

            monthlyRecords.add(f"{high}_MAX", mx_value, dt_value)
            yearlyRecords.add(f"{high}_MAX",  mx_value, dt_value)
            allTimeRecords.add(f"{high}_MAX", mx_value, dt_value)


    monthlyRecords.save()
    yearlyRecords.save()
    allTimeRecords.save()

    if Areport:
        allTimeRecords.show()
    elif Yreport:
        yearlyRecords.show(year)
    else:
        monthlyRecords.show(month, year)






