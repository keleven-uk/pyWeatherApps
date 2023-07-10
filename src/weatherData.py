###############################################################################################################
#    weatherData.py    Copyright (C) <2023>  <Kevin Scott>                                                    #
#                                                                                                             #
#    A class that loads in a spread sheet containing weather data.                                            #
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

import json

import colorama

from openpyxl import load_workbook

import src.classes.dataMapping as DM

from src.classes.dataClasses import weatherValues


class WeatherData():
    """  A class that loads in a spread sheet containing weather data.

         mainData = WD.WeatherData("data\\main.xlsx")  -  pass in the file containing the data in excell spreadsheet format.

         The file is loaded and the data inserted into a dictionary, then the object is created.

         mainData.countData()  -  return the number of entries.
         mainData.nextRow()    -  returns the data, one line at a time.

    """

    def __init__(self, file, screen=True):
        if screen:
            print(f"{colorama.Fore.GREEN} Processing data file {file}{colorama.Fore.RESET}")

        self.screen = screen
        self.fileName = file
        self.values   = {}         #  Dictionary to hold weather values.
        self.val_keys = list()     #  List to hold the dictionary keys
        self.position = 0
        self.loadFile()
        self.loadData()


    def loadFile(self):
        """  Load the spreadsheet in read only [don't want to accidentally amend] and only load data and not formulas.
        """
        self.workBook = load_workbook(filename=self.fileName, read_only=True, data_only=True)

        #  Grab the active worksheet
        self.workSheet = self.workBook.active
        if self.screen:
            print(f"{colorama.Fore.GREEN}     Scanning {self.workSheet.title} in {self.fileName}{colorama.Fore.RESET}")

    def loadData(self):
        """  Loads the entries into the directory.
        """
        for row in self.workSheet.iter_rows(min_row=3, values_only=True):
            self.wv = weatherValues()  #  A class to hold each row of weather data.  **REMEMBER**

            self.wv.OutdoorTemperature = row[DM.OUTDOOR_TEMPERATURE]
            self.wv.OutdoorFeelsLike   = row[DM.OUTDOOR_FEELS_LIKE]
            self.wv.OutdoorDewPoint    = row[DM.OUTDOOR_DEW_POINT]
            self.wv.OutdoorHumidity    = row[DM.OUTDOOR_HUMIDITY]
            self.wv.IndoorTemperature  = row[DM.INDOOR_TEMPERATURE]
            self.wv.IndoorHumidity     = row[DM.INDOOR_HUMIDITY]
            self.wv.Solar              = row[DM.SOLAR]
            self.wv.UVI                = row[DM.UVI]
            self.RainRate              = row[DM.RAIN_RATE]
            self.RainDaily             = row[DM.RAIN_DAILY]
            self.RainEvent             = row[DM.RAIN_EVENT]
            self.RainHourly            = row[DM.RAIN_HOURLY]
            self.RainWeekly            = row[DM.RAIN_WEEKLY ]
            self.RainMonthly           = row[DM.RAIN_MONTHLY]
            self.RainYearly            = row[DM.RAIN_YEARLY ]
            self.WindSpeed             = row[DM.WIND_SPEED]
            self.WindGust              = row[DM.WIND_GUST]
            self.WindDirection         = row[DM.WIND_DIRECTION]
            self.PressureRelative      = row[DM.PRESSURE_RELATIVE]
            self.PressureAbsolute      = row[DM.PRESSURE_ABSOLUTE]

            self.key                   = row[DM.TIME]

            self.values[self.key]      = self.wv

            self.wv = None      #  Is this needed? - memory??

        self.val_keys = list(self.values.keys())

        if self.screen:
            print(f"{colorama.Fore.GREEN}     with {self.countData()} rows{colorama.Fore.RESET}")


    def countData(self):
        """  Return the number of entries.
        """
        return len(self.values)


    def saveData(self):
        json_fileName = "dump.json"
        with open(json_fileName, "w") as json_file:
            json.dump(self.values, json_file, indent=4)


    def nextRow(self):
        """  Returns the data, one line at a time.
        """
        if self.position <= self.countData():
            self.position += 1
            yield (self.val_keys[self.position], self.values[self.val_keys[self.position]])     #  Return a tuple (key, data)



