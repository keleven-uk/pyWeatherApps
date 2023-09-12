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

from dataclasses import dataclass


@dataclass
class weatherValues:
    """  A class to hold the all time weather records.

         All values should be numeric when passed in.
    """

    OutdoorTemperature_MAX : float
    OutdoorTemperature_MIN : float
    OutdoorFeelsLike_MAX   : float
    OutdoorFeelsLike_MIN   : float
    OutdoorDewPoint_MAX    : float
    OutdoorDewPoint_MIN    : float
    OutdoorHumidity_MAX    : float
    OutdoorHumidity_MIN    : float
    IndoorTemperature_MAX  : float
    IndoorTemperature_MIN  : float
    IndoorHumidity_MAX     : float
    IndoorHumidity_MIN     : float
    Solar_MAX              : float
    UVI_MAX                : float
    RainRate_MAX           : float
    RainDaily_MAX          : float
    RainEvent_MAX          : float
    RainHourly_MAX         : float
    RainWeekly_MAX         : float
    RainMonthly_MAX        : float
    RainYearly_MAX         : float
    WindSpeed_MAX          : float
    WindGust_AMX           : float
    WindDirection_MAX      : float
    PressureRelative_MAX   : float
    PressureRelative_MIN   : float
    PressureAbsolute_MAX   : float
    PressureAbsolute_MIN   : float




