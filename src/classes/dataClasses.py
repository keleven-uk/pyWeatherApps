###############################################################################################################
#    dataClasses.py    Copyright (C) <2023>  <Kevin Scott>                                                    #
#                                                                                                             #
#    A class to hold weather data.                                                                            #
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


class weatherValues:
    """  A class to hold weather data.

         wv = weatherValues()

         then

         wv.data = datavalue

         TODO
            currently stored as strings, need to convert to numerical values.
    """
    def __init__(self):
        """  Basic init, just initialise to empty strings.
        """
        self.OutdoorTemperature = ""
        self.OutdoorFeelsLike   = ""
        self.OutdoorDewPoint    = ""
        self.OutdoorHumidity    = ""
        self.IndoorTemperature  = ""
        self.IndoorHumidity     = ""
        self.Solar              = ""
        self.UVI                = ""
        self.RainRate           = ""
        self.RainDaily          = ""
        self.RainEvent          = ""
        self.RainHourly         = ""
        self.RainWeekly         = ""
        self.RainMonthly        = ""
        self.RainYearly         = ""
        self.WindSpeed          = ""
        self.WindGust           = ""
        self.WindDirection      = ""
        self.PressureRelative   = ""
        self.PressureAbsolute   = ""


    def __repr__(self):
        first  = f"{self.OutdoorTemperature} : {self.OutdoorFeelsLike} : {self.OutdoorDewPoint} : {self.OutdoorHumidity} : "
        second = f"{self.IndoorTemperature} : {self.IndoorTemperature} : {self.Solar} : {self.UVI}"
        third  = f"{self.RainRate} : {self.RainDaily} : {self.RainEvent} : {self.RainHourly} : {self.RainWeekly} : {self.RainMonthly } :{self.RainYearly }"
        fourth = f"{self.WindSpeed} : {self.WindGust} : {self.WindDirection} :{self.PressureRelative} : {self.PressureAbsolute }"
        return f"{first}{second}{third}{fourth}"

    def __str__(self):
        first  = f"{self.OutdoorTemperature} : {self.OutdoorFeelsLike} : {self.OutdoorDewPoint} : {self.OutdoorHumidity} : "
        second = f"{self.IndoorTemperature} : {self.IndoorTemperature} : {self.Solar} : {self.UVI}"
        third  = f"{self.RainRate} : {self.RainDaily} : {self.RainEvent} : {self.RainHourly} : {self.RainWeekly} : {self.RainMonthly } :{self.RainYearly }"
        fourth = f"{self.WindSpeed} : {self.WindGust} : {self.WindDirection} :{self.PressureRelative} : {self.PressureAbsolute }"
        return f"{first}{second}{third}{fourth}"
