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

class monthlyRecords:
    """  A class to hold the monthly weather records.

         All values should be numeric when passed in.
    """

    def __init__(self, DBfilename):
        self.monthlyRecords = {}
        self.DBfilename = f"{DBfilename[0:-4]}.pickle"
        print(self.DBfilename)
        self.load()


    def load(self):
        """  Load the monthly records  in pickle format.
        """
        try:
            with open(self.DBfilename, "rb") as pickle_file:
                self.monthlyRecords = pickle.load(pickle_file)
        except FileNotFoundError:
            print(f"ERROR :: Cannot find library file. {self.DBfilename}.  Will use an empty library")
            self.monthlyRecords = {}


    def save(self):
        """  Save the monthly records in pickle format.
        """
        with open(self.DBfilename, "wb") as pickle_file:
            pickle.dump(self.monthlyRecords, pickle_file)



