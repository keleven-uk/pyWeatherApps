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


