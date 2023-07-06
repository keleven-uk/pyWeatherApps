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

import colorama

from src.classes.dataMapping import *
from src.classes.dataClasses import weatherValues

from openpyxl import load_workbook

class WeatherData():

    def __init__(self, file, screen=True):
        if screen:
            print(f"{colorama.Fore.GREEN} Processing data file {file}{colorama.Fore.RESET}")

        self.wv = weatherValues()  #  A class to hold each row of weather data.
        self.fileName = file
        self.values   = {}         #  Dictionary to hold weather values.
        self.loadFile()
        self.loadData()


    def loadFile(self):
        #  Load the spreadsheet in read only [don't want to accidentally amend]
        #  and only load data and not formulas.
        self.workBook = load_workbook(filename=self.fileName, read_only=True, data_only=True)

        #  Grab the active worksheet
        self.workSheet = self.workBook.active
        if self.fileName:
            print(f"{colorama.Fore.GREEN}     Scanning {self.workSheet.title} in {self.fileName}{colorama.Fore.RESET}")

    def loadData(self):
        for row in self.workSheet.iter_rows(min_row=3, max_row = 6, values_only=True):
            print(row)
            print(row[OUTDOOR_TEMPERATURE], row[UTDOOR_FEELS_LIKE])
            self.wv.OutdoorTemperature  = row[OUTDOOR_TEMPERATURE]
            self.wv.OutdoorFeelsLike    = row[UTDOOR_FEELS_LIKE]
            self.values[row[TIME]]      = self.wv
            print(f" :: {self.wv.OutdoorTemperature}, {self.wv.OutdoorFeelsLike}")

        for k, v in self.values.items():
            self.wv = v
            print(f"{k} :: {self.wv.OutdoorTemperature}, {self.wv.OutdoorFeelsLike}")

        print(f"\nLength of dict :: {len(self.values)}")





