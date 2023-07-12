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
from json import JSONEncoder

import colorama

from openpyxl import load_workbook

import src.classes.dataMapping as DM

from src.classes.dataClasses import weatherValues


class WeatherData():
    """  A class that loads in a spread sheet containing weather data.

         mainData = WD.WeatherData("data\\main.xlsx")  -  pass in the file containing the data in excell spreadsheet format.

         The file is loaded and the data inserted into a dictionary, then the object is created.

         mainData.loadFile()   -  loads the spreadsheet.
         mainData.loadData()   -  loads the spreadsheet into a directory.
         mainData.saveData()   -  save the directory back to the spreadsheet.
         mainData.countData()  -  return the number of entries.
         mainData.nextRow()    -  returns the data, one line at a time.
         mainData.add()        -  adds a row into the directory.

         to see in an entry is in the directory use key in mainData (uses __contains__)

    """

    def __init__(self, file, screen=True):
        if screen:
            print(f"{colorama.Fore.GREEN} Processing data file {file}{colorama.Fore.RESET}")

        self.screen = screen
        self.fileName = file
        self.values   = {}         #  Dictionary to hold weather values.
        self.val_keys = ()         #  List to hold the dictionary keys
        self.position = 0
        self.loadFile()
        self.loadData()


    def __contains__(self, key):
        """  checks to see if key already exists in the data directory.
             The directory keys are help in a separate list and MUST be kept updated.
        """
        return key in self.val_keys


    def loadFile(self):
        """  Load the spreadsheet in read only [don't want to accidentally amend] and only load data and not formulas.
        """
        self.workBook = load_workbook(filename=self.fileName, read_only=False, data_only=True)

        #  Grab the active worksheet
        self.workSheet = self.workBook.active
        if self.screen:
            print(f"{colorama.Fore.GREEN}     Scanning {self.workSheet.title} in {self.fileName}{colorama.Fore.RESET}")

    def loadData(self):
        """  Loads the entries into the directory.
        """
        for row in self.workSheet.iter_rows(min_row=DM.START_ROW, values_only=True):
            self.wv = weatherValues()  #  A class to hold each row of weather data.  **REMEMBER**

            self.wv.OutdoorTemperature = row[DM.OUTDOOR_TEMPERATURE]
            self.wv.OutdoorFeelsLike   = row[DM.OUTDOOR_FEELS_LIKE]
            self.wv.OutdoorDewPoint    = row[DM.OUTDOOR_DEW_POINT]
            self.wv.OutdoorHumidity    = row[DM.OUTDOOR_HUMIDITY]
            self.wv.IndoorTemperature  = row[DM.INDOOR_TEMPERATURE]
            self.wv.IndoorHumidity     = row[DM.INDOOR_HUMIDITY]
            self.wv.Solar              = row[DM.SOLAR]
            self.wv.UVI                = row[DM.UVI]
            self.wv.RainRate           = row[DM.RAIN_RATE]
            self.wv.RainDaily          = row[DM.RAIN_DAILY]
            self.wv.RainEvent          = row[DM.RAIN_EVENT]
            self.wv.RainHourly         = row[DM.RAIN_HOURLY]
            self.wv.RainWeekly         = row[DM.RAIN_WEEKLY ]
            self.wv.RainMonthly        = row[DM.RAIN_MONTHLY]
            self.wv.RainYearly         = row[DM.RAIN_YEARLY ]
            self.wv.WindSpeed          = row[DM.WIND_SPEED]
            self.wv.WindGust           = row[DM.WIND_GUST]
            self.wv.WindDirection      = row[DM.WIND_DIRECTION]
            self.wv.PressureRelative   = row[DM.PRESSURE_RELATIVE]
            self.wv.PressureAbsolute   = row[DM.PRESSURE_ABSOLUTE]

            self.key                   = row[DM.TIME]

            self.values[self.key]      = self.wv

            self.wv = None      #  Is this needed? - memory??

        self.val_keys = list(self.values.keys())    #  A list of keys for later.

        if self.screen:
            print(f"{colorama.Fore.GREEN}     with {self.countData()} rows{colorama.Fore.RESET}")


    def countData(self):
        """  Return the number of entries.
        """
        return len(self.values)


    def saveDataJson(self, jsonFileName="dump.json"):
        """  Converts the data directory to a json object, then writs to a file.
             Needs a custom encoder (dataEncoder), weatherValues is not natively serializable.
        """
        json_object = json.dumps(self.values, indent=4, cls=dataEncoder)
        with open(jsonFileName, "w") as json_file:
             json_file.write(json_object)


    def nextRow(self):
        """  Returns the data, one line at a time.
        """
        if self.position <= self.countData():
            self.position += 1
            yield (self.val_keys[self.position], self.values[self.val_keys[self.position]])     #  Return a tuple (key, data)


    def add(self, key, row):
        """  Adds a new entry to the data dictionary.
             The key is added to the list of keys.
        """
        self.values[key] = row
        self.val_keys.append(key)


    def saveData(self):
        """  Save the data directory to a excel spreadsheet.

             NB  Spreadsheets start at column 1.
        """
        rowNumber = DM.START_ROW
        for key, row in self.values.items():

            # the .cell is a function, we ignore the return value - looks like the cell reference.
            self.workSheet.cell(row=rowNumber, column=DM.TIME + 1               , value = key)
            self.workSheet.cell(row=rowNumber, column=DM.OUTDOOR_TEMPERATURE + 1, value = row.OutdoorTemperature )
            self.workSheet.cell(row=rowNumber, column=DM.OUTDOOR_FEELS_LIKE + 1 , value = row.OutdoorFeelsLike)
            self.workSheet.cell(row=rowNumber, column=DM.OUTDOOR_DEW_POINT + 1  , value = row.OutdoorDewPoint)
            self.workSheet.cell(row=rowNumber, column=DM.OUTDOOR_HUMIDITY + 1   , value = row.OutdoorHumidity)
            self.workSheet.cell(row=rowNumber, column=DM.INDOOR_TEMPERATURE + 1 , value = row.IndoorTemperature)
            self.workSheet.cell(row=rowNumber, column=DM.INDOOR_HUMIDITY + 1    , value = row.IndoorHumidity)
            self.workSheet.cell(row=rowNumber, column=DM.SOLAR + 1              , value = row.Solar)
            self.workSheet.cell(row=rowNumber, column=DM.UVI + 1                , value = row.UVI)
            self.workSheet.cell(row=rowNumber, column=DM.RAIN_RATE + 1          , value = row.RainRate)
            self.workSheet.cell(row=rowNumber, column=DM.RAIN_DAILY + 1         , value = row.RainDaily)
            self.workSheet.cell(row=rowNumber, column=DM.RAIN_EVENT + 1         , value = row.RainEvent)
            self.workSheet.cell(row=rowNumber, column=DM.RAIN_HOURLY + 1        , value = row.RainHourly)
            self.workSheet.cell(row=rowNumber, column=DM.RAIN_WEEKLY + 1        , value = row.RainWeekly)
            self.workSheet.cell(row=rowNumber, column=DM.RAIN_MONTHLY + 1       , value = row.RainMonthly)
            self.workSheet.cell(row=rowNumber, column=DM.RAIN_YEARLY + 1        , value = row.RainYearly)
            self.workSheet.cell(row=rowNumber, column=DM.WIND_SPEED + 1         , value = row.WindSpeed)
            self.workSheet.cell(row=rowNumber, column=DM.WIND_GUST + 1          , value = row.WindGust)
            self.workSheet.cell(row=rowNumber, column=DM.WIND_DIRECTION + 1     , value = row.WindDirection)
            self.workSheet.cell(row=rowNumber, column=DM.PRESSURE_RELATIVE + 1  , value = row.PressureRelative)
            self.workSheet.cell(row=rowNumber, column=DM.PRESSURE_ABSOLUTE + 1  , value = row.PressureAbsolute)

            rowNumber += 1

        self.workBook.save(filename=self.fileName)



class dataEncoder(JSONEncoder):
    """  A custom json encoder to bake directories serializable.
    """
    def default(self, o):
        return o.__dict__





