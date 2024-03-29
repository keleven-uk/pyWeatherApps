###############################################################################################################
#    Records.py    Copyright (C) <2023 - 2024>  <Kevin Scott>                                                 #
#                                                                                                             #
#    A class to hold records, this then subclassed to monthly, yearly and all time.                           #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2023 - 2024>  <Kevin Scott>                                                               #
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
import calendar

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


    def add(self, category, period, value, dt_value):
        """  Adds a new entry if not already present.
             The key is the category and the data is a tuple of the date and value.

             The categories can be found on the calling script - dataSQLreport.py
        """
        mode = category[-3:]                     #  either MAX or MIN

        if category not in self.Records:
            self.Records[category] = (dt_value, value)
        elif category != "RainDays" or category != "DryDays":
            data = self.Records[category]
            if mode == "MAX":
                if value > data[1]:
                    print(f"New {period:9} record {category:25} {dt_value:14} {value} :: {data}")
                    self.Records[category] = (dt_value, value)
            elif mode == "MIN":
                if value < data[1]:
                    print(f"New {period:9} record {category:25} {dt_value:14} {value} :: {data}")
                    self.Records[category] = (dt_value, value)
            elif mode == "AVG":
                if value > data[1]:
                    print(f"New {period:9} record {category:25} {dt_value:14} {value} :: {data}")


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


    def show(self, title, month, year, monthlyReport=False):
        """  Prints to screen the contains of the records in a pretty table.

             The title of the table needs to be passed in.
        """
        print()

        Table.title = title

        Table.add_column("Category", justify="right", style="cyan", no_wrap=True)
        Table.add_column("Date", style="magenta")
        Table.add_column("Value", justify="left", style="green")

        for category, v in self.Records.items():
            date   = v[0]

            if category == "RainDays" or category == "DryDays":
                amount = v[1]
            else:
                amount = float(v[1])


            #  Format values correctly and add imperial equivalents, if appropriate.
            #  Also correct spelling mistakes.
            match category:
                case category if category.startswith("Rain"):
                    if category == "RainDays" or category == "DryDays":
                        value = amount
                    else:
                        value  = f"{amount}mm ({amount*0.0393701:.2f}in)"
                    match category:
                        case category if category.startswith("RainDays"):
                            date  = f"{calendar.month_name[month]} {year}"
                        case category if category.startswith("DryDays"):
                            date  = f"{calendar.month_name[month]} {year}"
                        case category if category.startswith("RainMonthly"):
                            if monthlyReport:           #  Used for monthly reports only
                                date  = f"{month} {year}"
                            else:                       #  Use the correct year and month for the record.
                                month = int(date[5:7])
                                date = f"{calendar.month_name[month]} {date[0:4]}"
                        case "RainYearly_MAX":
                            if monthlyReport:           #  Used for monthly reports only
                                date  = f"{year}"
                            else:                       #  Use the correct year for the record.
                                date = f"{date[0:4]}"
                case category if category.startswith("Wind"):
                    value  = f"{amount}km/h ({amount*0.6213715277778:.2f}mph)"
                case category if category.startswith("Solar"):
                    value  = f"{amount}Klux"
                case category if category.startswith("Pressue"):
                    value  = f"{amount}hPa"
                case category if "Humidity" in category:
                    value  = f"{amount}%"
                case category if category == "OutdoorTemperature_AVG":
                    if monthlyReport: continue                                    #  Ignore monthly average on yearly and all time displays.
                    value = f"{amount:.2f}C"
                    date  = f"{month} {year}"
                case category if "Temperature" in category:
                    value  = f"{amount:.2f}C"
                case category if "Temprature" in category:                       #  Correct spelling mistake in category title.
                    category = category.replace("Temprature", "Temperature")
                    value  = f"{amount:.2f}C"
                case category if "DewPoint" in category:
                    value  = f"{amount}C"
                case category if "FeelsLike" in category:
                    value  = f"{amount}C"
                case _:
                    value = v[1]

            #  Add horizontal lines to the table to split the categories
            match category:
                case "IndoorTemperature_MIN" | "DayTimeTemperature_MIN" | "OutdoorHumidity_MIN" | "IndoorHumidity_MIN"| \
                     "PressueAbsolute_MIN" | "UVI_MAX" | "Dry Days":
                    Table.add_row(f"{category}", f"{date}", f"{value}", end_section=True)
                case _:
                    Table.add_row(f"{category}", f"{date}", f"{value}")

        console.print(Table)




