###############################################################################################################
#    allTimeRecords.py    Copyright (C) <2023>  <Kevin Scott>                                                 #
#                                                                                                             #
#    A class to hold the all time weather records.                                                            #
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

from src.console import console, YearlyTable

class yearlyRecords:
    """  A class to hold the yearly weather records.

         All values should be numeric when passed in.
    """

    def __init__(self, yearlyRecordFiles):
        self.yearlyRecords     = {}
        self.yearlyRecordFiles = pathlib.Path(yearlyRecordFiles)
        self.load()


    def add(self, category, value, dt_value):
        """  Adds a new entry if not already present and the value is greater then already present.
               If the new value is equal to the stored values, it is ignored.
               So, only the first instance is stored. [is this correct?]

             The key is the category and the data is a tuple of the date and value.

             The categories can be found on the calling script - dataSQLreport.py
        """

        if category not in self.yearlyRecords:
            self.yearlyRecords[category] = (dt_value, value)
        else:
            data = self.yearlyRecords[category]
            mode = category[-3:]                     #  either MAX or MIN

            match mode:
                case "MAX" if value > data[1]:
                    print(f"New yearly record {category:26} {dt_value:14} {value}")
                    self.yearlyRecords[category] = (dt_value, value)
                case "MIN" if value < data[1]:
                    print(f"New yearly record {category:26} {dt_value:14} {value}")
                    self.yearlyRecords[category] = (dt_value, value)

            # if mode == "MAX":
            #     if value > data[1]:
            #         print(f"New yearly record {category:26} {dt_value:14} {value}")
            #         self.yearlyRecords[category] = (dt_value, value)
            # elif mode == "MIN":
            #     if value < data[1]:
            #         print(f"New yearly record {category:26} {dt_value:14} {value}")
            #         self.yearlyRecords[category] = (dt_value, value)
            # else:
            #     print("Unknown mode.")



    def load(self):
        """  Load the monthly records  in pickle format.
        """
        try:
            with open(self.yearlyRecordFiles, "rb") as pickle_file:
                self.yearlyRecords = pickle.load(pickle_file)
        except FileNotFoundError:
            print(f"ERROR :: Cannot find library file. {self.yearlyRecords}.  Will use an empty library")
            self.yearlyRecords = {}


    def save(self):
        """  Save the monthly records in pickle format.
        """
        with open(self.yearlyRecordFiles, "wb") as pickle_file:
            pickle.dump(self.yearlyRecords, pickle_file)


    def show(self, year):
        print()

        YearlyTable.title = f" Weather Records for {year}"
        YearlyTable.add_column("Category", justify="right", style="cyan", no_wrap=True)
        YearlyTable.add_column("Date", style="magenta")
        YearlyTable.add_column("Value", justify="right", style="green")

        for d, v in self.yearlyRecords.items():
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

            YearlyTable.add_row(f"{d}", f"{v[0]}", f"{value}")

        console.print(YearlyTable)

