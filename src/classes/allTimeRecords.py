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

from rich.console import Console
from rich.table import Table

class allTimeRecords:
    """  A class to hold the all time weather records.

         All values should be numeric when passed in.
    """

    def __init__(self, recordFiles):
        self.Records     = {}
        self.recordFiles = pathlib.Path(recordFiles)
        self.load()


    def add(self, cat, value, dt_value):
        """  Adds a new entry if not already present and the value is greater then already present.
               If the new value is equal to the stored values, it is ignored.
               So, only the first instance is stored. [is this correct?]

             The key is the category and the data is a tuple of the date and value.

             The categories can be found on the calling script - dataSQLreport.py
        """
        mode = cat[-3:]                     #  either MAX or MIN
        if cat not in self.Records:
            self.Records[cat] = (dt_value, value)
        else:
            data = self.Records[cat]
            if mode == "MAX":
                if value > data[1]:
                    self.Records[cat] = (dt_value, value)
            elif mode == "MIN":
                if value < data[1]:
                    self.Records[cat] = (dt_value, value)
            else:
                print("Unknown mode.")



    def load(self):
        """  Load the records  in pickle format.
        """
        try:
            with open(self.recordFiles, "rb") as pickle_file:
                self.Records = pickle.load(pickle_file)
        except FileNotFoundError:
            print(f"ERROR :: Cannot find library file. {self.recordFiles}.  Will use an empty library")
            self.Records = {}


    def save(self):
        """  Save the monthly records in pickle format.
        """
        with open(self.recordFiles, "wb") as pickle_file:
            pickle.dump(self.Records, pickle_file)


    def show(self):
        print()
        table = Table(title=" All Time Weather Records")

        table.add_column("Category", justify="right", style="cyan", no_wrap=True)
        table.add_column("Date", style="magenta")
        table.add_column("Value", justify="right", style="green")

        for d, v in self.Records.items():
            table.add_row(f"{d}", f"{v[0]}", f"{v[1]}")

        console = Console()
        console.print(table)




