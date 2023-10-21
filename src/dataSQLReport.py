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

            if highLow == "OutdoorTemperature":                 #  ** should this be here, maybe another function.  **
                #  Obtain average temperatures for the month.
                sql3DB.execute("SELECT DateTime, AVG(OutdoorTemperature) from DailyData")
                value    = sql3DB.fetchone()
                dt_value = f"{month} {year}"
                mx_value = value[1]
                utils.logPrint(logger, verbose, f"date = {dt_value}  max value = {mx_value}", "info")

                monthlyRecords.add("OutdoorTemperature_AVG", mx_value, dt_value)        #  Add average to monthly.
                yearlyRecords.add( "OutdoorTemperature_AVG_MAX", mx_value, dt_value)    #  add min and max average to yearly.
                yearlyRecords.add( "OutdoorTemperature_AVG_MIN", mx_value, dt_value)
                allTimeRecords.add("OutdoorTemperature_AVG_MAX", mx_value, dt_value)    #  add min and max average to all time.
                allTimeRecords.add("OutdoorTemperature_AVG_MIN", mx_value, dt_value)

                        #  Obtain highest night-time temperatures for the month.
                sql3DB.execute("SELECT DateTime, MAX(OutdoorTemperature) from DailyData where Solar == 0")
                value    = sql3DB.fetchone()
                dt_value = value[0]
                mx_value = value[1]
                utils.logPrint(logger, verbose, f"date = {dt_value}  max value = {mx_value}", "info")

                monthlyRecords.add("NightTimeTemprature_MAX", mx_value, dt_value)    #  Add lowest day time to monthly.
                yearlyRecords.add( "NightTimeTemprature_MAX", mx_value, dt_value)    #  add min and max lowest day time to yearly.
                allTimeRecords.add("NightTimeTemprature_MAX", mx_value, dt_value)    #  add min and max lowest day time to all time.

                #  Obtain lowest day time temperatures for the month.
                sql3DB.execute("SELECT DateTime, MAX(OutdoorTemperature) from DailyData where Solar != 0 group by day")
                value    = sql3DB.fetchall()
                dt_value = ""
                mx_value = 100                  # ** must be a better way of doing this.  **
                for v in value:
                    if v[1] < mx_value:
                        dt_value = v[0]
                        mx_value = v[1]

                utils.logPrint(logger, verbose, f"date = {dt_value}  max value = {mx_value}", "info")

                monthlyRecords.add("DayTimeTemprature_MIN", mx_value, dt_value)    #  Add lowest day time to records.
                yearlyRecords.add( "DayTimeTemprature_MIN", mx_value, dt_value)
                allTimeRecords.add("DayTimeTemprature_MIN", mx_value, dt_value)

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
        allTimeRecords.show(month, year)
    elif Yreport:
        yearlyRecords.show(month, year)
    else:
        monthlyRecords.show(month, year)






