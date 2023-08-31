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
#     -b, --build           Build the data - consolidate the spreadsheets.                                    #
#     -r, --report          Report on the data - finds the highs and lows.                                    #
#     -c, --create          Creates the SQLite3 database and table.                                           #
#     -V, --Verbose         Verbose - print more detail.                                                      #
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

import sys
import textwrap
import argparse

import src.license as License
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
        Builds a main data store out of individual weather data spreadsheets.
        The data store can be either an Excel spreadsheet or a SQLite3 database.
        The type of data store is specified in config.toml."""),
        epilog=f" Kevin Scott (C) 2023 :: {appName} {appVersion}")

    parser.add_argument("-l", "--license",  action="store_true", help="Print the Software License.")
    parser.add_argument("-v", "--version",  action="store_true", help="Print the version of the application.")
    parser.add_argument("-e", "--explorer", action="store_true", help="Load program working directory into file explorer.")
    parser.add_argument("-b", "--build",    action="store_true", help="Build the data - consolidate the spreadsheets.")
    parser.add_argument("-r", "--report",   action="store_true", help="Report on the data - finds the highs and lows.")
    parser.add_argument("-c", "--create",   action="store_true", help="Creates the SQLite3 database and tables. [WARNING WILL DROP TABLES IF EXITS]")
    parser.add_argument("-V", "--Verbose",  action="store_true", help="Verbose - print more detail.")

    args = parser.parse_args()

    if args.version:
        if args.Verbose:
            License.printLongLicense(appName, appVersion, logger)
        else:
            License.printShortLicense(appName, appVersion, logger)
        logger.info(f"Running on {sys.version} Python")
        logger.info(f"Running on {utils.sqlite3Version()} SQLite3")
        logger.info(f"End of {appName} V{appVersion}: version")
        print("Goodbye.")
        sys.exit(0)

    if args.license:
        License.printLongLicense(appName, appVersion, logger)
        logger.info(f"End of {appName} V{appVersion} : Printed Licence")
        print("Goodbye.")
        sys.exit(0)

    if args.explorer:
        utils.loadExplorer(logger)             # Load program working directory n file explorer.
        print("Goodbye.")
        sys.exit(0)

    return(args.build, args.report, args.Verbose, args.create)



