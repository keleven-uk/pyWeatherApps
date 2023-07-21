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
        """  Checks if the data value is of type float, if not make it so (set to 200.0)
             A large value is used [hopefully never reached], will check later if this is an inserted value.
        """
        if not isinstance(self.OutdoorTemperature, float):
            self.OutdoorTemperature = 200.0
        if not isinstance(self.OutdoorFeelsLike, float):
            self.OutdoorFeelsLike = 200.0
        if not isinstance(self.OutdoorDewPoint, float):
            self.OutdoorDewPoint = 200.0
        if not isinstance(self.OutdoorHumidity, float):
            self.OutdoorHumidity = 200.0
        if not isinstance(self.IndoorTemperature, float):
            self.IndoorTemperature = 200.0
        if not isinstance(self.IndoorHumidity, float):
            self.IndoorHumidity = 200.0
        if not isinstance(self.Solar, float):
            self.Solar = 200.0
        if not isinstance(self.UVI, float):
            self.UVI = 200.0
        if not isinstance(self.RainRate, float):
            self.RainRate = 200.0
        if not isinstance(self.RainDaily, float):
            self.RainDaily = 200.0
        if not isinstance(self.RainEvent, float):
            self.RainEvent = 200.0
        if not isinstance(self.RainHourly, float):
            self.RainHourly = 200.0
        if not isinstance(self.RainWeekly, float):
            self.RainWeekly = 200.0
        if not isinstance(self.RainMonthly, float):
            self.RainWeekly = 200.0
        if not isinstance(self.RainYearly, float):
            self.RainYearly = 200.0
        if not isinstance(self.WindSpeed, float):
            self.WindSpeed = 200.0
        if not isinstance(self.WindGust, float):
            self.WindGust = 200.0
        if not isinstance(self.WindDirection, float):
            self.WindDirection = 200.0
        if not isinstance(self.PressureRelative, float):
            self.PressureRelative = 200.0
        if not isinstance(self.PressureAbsolute, float):
            self.PressureAbsolute = 200.0


