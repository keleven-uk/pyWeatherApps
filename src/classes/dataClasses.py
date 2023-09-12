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

from dataclasses import dataclass


@dataclass
class weatherValues:
    """  A data class to hold weather data.
    """

    OutdoorTemperature : float
    OutdoorFeelsLike   : float
    OutdoorDewPoint    : float
    OutdoorHumidity    : float
    IndoorTemperature  : float
    IndoorHumidity     : float
    Solar              : float
    UVI                : float
    RainRate           : float
    RainDaily          : float
    RainEvent          : float
    RainHourly         : float
    RainWeekly         : float
    RainMonthly        : float
    RainYearly         : float
    WindSpeed          : float
    WindGust           : float
    WindDirection      : float
    PressureRelative   : float
    PressureAbsolute   : float

    def __post_init__(self):
        """  Checks if the data value is of type numeric, if not make see it to None.
             In SQL the min and max functions ignore None..
        """
        if not isinstance(self.OutdoorTemperature, (int, float)):
            self.OutdoorTemperature = None
        if not isinstance(self.OutdoorFeelsLike, (int, float)):
            self.OutdoorFeelsLike = None
        if not isinstance(self.OutdoorDewPoint, (int, float)):
            self.OutdoorDewPoint = None
        if not isinstance(self.OutdoorHumidity, (int, float)):
            self.OutdoorHumidity = None
        if not isinstance(self.IndoorTemperature, (int, float)):
            self.IndoorTemperature = None
        if not isinstance(self.IndoorHumidity, (int, float)):
            self.IndoorHumidity = None
        if not isinstance(self.Solar, (int, float)):
            self.Solar = None
        if not isinstance(self.UVI, (int, float)):
            self.UVI = None
        if not isinstance(self.RainRate, (int, float)):
            self.RainRate = None
        if not isinstance(self.RainDaily, (int, float)):
            self.RainDaily = None
        if not isinstance(self.RainEvent, (int, float)):
            self.RainEvent = None
        if not isinstance(self.RainHourly, (int, float)):
            self.RainHourly = None
        if not isinstance(self.RainWeekly, (int, float)):
            self.RainWeekly = None
        if not isinstance(self.RainMonthly, (int, float)):
            self.RainWeekly = None
        if not isinstance(self.RainYearly, (int, float)):
            self.RainYearly = None
        if not isinstance(self.WindSpeed, (int, float)):
            self.WindSpeed = None
        if not isinstance(self.WindGust, (int, float)):
            self.WindGust = None
        if not isinstance(self.WindDirection, (int, float)):
            self.WindDirection = None
        if not isinstance(self.PressureRelative, (int, float)):
            self.PressureRelative = None
        if not isinstance(self.PressureAbsolute, (int, float)):
            self.PressureAbsolute = None


