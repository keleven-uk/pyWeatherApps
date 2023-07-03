###############################################################################################################
#    args   Copyright (C) <2023>  <Kevin Scott>                                                               #
#                                                                                                             #
#    Parse the command line arguments.                                     .                                  #
#                                                                                                             #
#   options:                                                                                                  #
#     -h, --help            show this help message and exit                                                   #
#     -l, --license         Print the Software License.                                                       #
#     -v, --version         Print the version of the application.                                             #
#     -e, --explorer        Load program working directory into file explorer.                                #
#                                                                                                             #
#     For changes see history.txt                                                                             #
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

import os
import sys
import textwrap
import argparse
import colorama

from pathlib import Path

import src.License as License
import src.utils.dataUtils as utils

############################################################################################## parseArgs ######
def parseArgs(appName, appVersion, logger):
    """  Process the command line arguments.

         Checks the arguments and will exit if not valid.

         Exit code 0 - program has exited normally, after print version, licence or help.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description=textwrap.dedent("""\
        Builds a main spreadsheeet out of individual weather data spreadsheets."""),
        epilog=f" Kevin Scott (C) 22023 :: {appName} {appVersion}")

    parser.add_argument("-l", "--license", action="store_true", help="Print the Software License.")
    parser.add_argument("-v", "--version", action="store_true", help="Print the version of the application.")
    parser.add_argument("-e", "--explorer", action="store_true", help="Load program working directory into file explorer.")

    args = parser.parse_args()

    if args.version:
        License.printShortLicense(appName, appVersion, logger, False)
        logger.info(f"Running on {sys.version} Python")
        logger.info(f"End of {appName} V{appVersion}: version")
        print("Goodbye.")
        sys.exit(0)

    if args.license:
        License.printLongLicense(appName, appVersion)
        logger.info(f"End of {appName} V{appVersion} : Printed Licence")
        print("Goodbye.")
        sys.exit(0)

    if args.explorer:
        utils.loadExplorer(logger)             # Load program working directory n file explorer.
        print("Goodbye.")
        sys.exit(0)



