###############################################################################################################
#    Records.py    Copyright (C) <2023>  <Kevin Scott>                                                        #
#                                                                                                             #
#    A class to hold records, this then subclassed to monthly, yearly and all time.                           #
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

from src.console import console, Table

class Records:
    """  A class to hold weather records.

         All values should be numeric when passed in.

         usage:
                class r (Records):

                then
                    __init__(recordFiles)                #  Record files is a files for the records.
                        super().__init__(recordFiles)    #  This will call load().

                then call to

                r.add()   to add a record to the store.
                r.save()  to save records to a pickle file.
                r.show()  to display the records in a pretty table.
    """

    def __init__(self, recordFiles):
        """  Set up class.
        """
        self.Records = {}
        self.recordFiles = pathlib.Path(recordFiles)
        self.load()


    def add(self, category, value, dt_value):
        """  Adds a new entry if not already present.
             The key is the category and the data is a tuple of the date and value.

             The categories can be found on the calling script - dataSQLreport.py
        """
        mode = category[-3:]                     #  either MAX or MIN
        if category not in self.Records:
            self.Records[category] = (dt_value, value)
        else:
            data = self.Records[category]
            if mode == "MAX":
                if value > data[1]:
                    print(f"New monthly record {category:25} {dt_value:14} {value}")
                    self.Records[category] = (dt_value, value)
            elif mode == "MIN":
                if value < data[1]:
                    print(f"New monthly record {category:25} {dt_value:14} {value}")
                    self.Records[category] = (dt_value, value)
            elif mode == "AVG":
                if value > data[1]:
                    print(f"New monthly record {category:25} {dt_value:14} {value}")
            else:
                print("Unknown mode.")


    def load(self):
        """  Load the monthly records  in pickle format.
        """
        try:
            with open(self.recordFiles, "rb") as pickle_file:
                self.Records = pickle.load(pickle_file)
        except FileNotFoundError:
            print(f"ERROR :: Cannot find library file. {self.recordFiles}.  Will use an empty library")
            self.monthlyRecords = {}


    def save(self):
        """  Save the monthly records in pickle format.
        """
        with open(self.recordFiles, "wb") as pickle_file:
            pickle.dump(self.Records, pickle_file)


    def show(self, title, mothlyReport=False):
        """  Prints to screen the contains of the records in a pretty table.

             The title of the table needs to be passed in.
        """
        print()

        Table.title = title

        Table.add_column("Category", justify="right", style="cyan", no_wrap=True)
        Table.add_column("Date", style="magenta")
        Table.add_column("Value", justify="left", style="green")

        for d, v in self.Records.items():
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
                case d if d == "OutdoorTemperature_AVG":
                    if mothlyReport: continue                                    #  Ignore monthly average on yearly and all time displays.
                    value  = f"{amount:.2f}C"
                case d if "Temperature" in d:
                    value  = f"{amount:.2f}C"
                case d if "Temprature" in d:                    #  Correct spelling mistake in category title.
                    d = d.replace("Temprature", "Temperature")
                    value  = f"{amount:.2f}C"
                case d if "DewPoint" in d:
                    value  = f"{amount}C"
                case d if "FeelsLike" in d:
                    value  = f"{amount}C"
                case _:
                    value = v[1]

            Table.add_row(f"{d}", f"{v[0]}", f"{value}")

        console.print(Table)




