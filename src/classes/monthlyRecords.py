###############################################################################################################
#    monthlyRecords.py    Copyright (C) <2023>  <Kevin Scott>                                                 #
#                                                                                                             #
#    A class to hold the monthly records.                                                                     #
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

import pickle
import pathlib

from src.console import console, monthlyTable

class monthlyRecords:
    """  A class to hold the monthly weather records.

         All values should be numeric when passed in.
    """

    def __init__(self, recordFiles):
        self.monthlyRecords = {}
        self.recordFiles = pathlib.Path(recordFiles)
        self.load()


    def add(self, category, value, dt_value):
        """  Adds a new entry if not already present.
             The key is the category and the data is a tuple of the date and value.

             The categories can be found on the calling script - dataSQLreport.py
        """
        mode = category[-3:]                     #  either MAX or MIN
        if category not in self.monthlyRecords:
            self.monthlyRecords[category] = (dt_value, value)
        else:
            data = self.monthlyRecords[category]
            if mode == "MAX":
                if value > data[1]:
                    print(f"New monthly record {category:25} {dt_value:14} {value}")
                    self.monthlyRecords[category] = (dt_value, value)
            elif mode == "MIN":
                if value < data[1]:
                    print(f"New monthly record {category:25} {dt_value:14} {value}")
                    self.monthlyRecords[category] = (dt_value, value)
            else:
                print("Unknown mode.")


    def load(self):
        """  Load the monthly records  in pickle format.
        """
        try:
            with open(self.recordFiles, "rb") as pickle_file:
                self.monthlyRecords = pickle.load(pickle_file)
        except FileNotFoundError:
            print(f"ERROR :: Cannot find library file. {self.recordFiles}.  Will use an empty library")
            self.monthlyRecords = {}


    def save(self):
        """  Save the monthly records in pickle format.
        """
        with open(self.recordFiles, "wb") as pickle_file:
            pickle.dump(self.monthlyRecords, pickle_file)


    def show(self, month, year):
        print()

        monthlyTable.title=f" Weather Records for {month} {year}"

        monthlyTable.add_column("Category", justify="right", style="cyan", no_wrap=True)
        monthlyTable.add_column("Date", style="magenta")
        monthlyTable.add_column("Value", justify="left", style="green")

        for d, v in self.monthlyRecords.items():
            amount = float(v[1])

            match d:
                case d if d.startswith("Rain"):
                    value  = f"{amount}mm ({amount*0.0393701:.2f}in)"
                case d if d.startswith("Wind"):
                    value  = f"{amount}km/h ({amount*0.6213715277778:.2f}mph)"
                case d if d.startswith("Solar"):
                    value  = f"{amount}Klux"
                case d if d.startswith("Pressue"):
                    value  = f"{amount}hPa"
                case d if "Humidity" in d:
                    value  = f"{amount}%"
                case d if "Temperature" in d:
                    value  = f"{amount}C"
                case d if "Temprature" in d:                    #  Correct spelling mistake in category title.
                    d = d.replace("Temprature", "Temperature")
                    value  = f"{amount}C"
                case d if "DewPoint" in d:
                    value  = f"{amount}C"
                case d if "FeelsLike" in d:
                    value  = f"{amount}C"
                case other:
                    value = v[1]

            monthlyTable.add_row(f"{d}", f"{v[0]}", f"{value}")

        console.print(monthlyTable)




