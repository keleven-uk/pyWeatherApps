#############################################################################################################################
#    args   Copyright (C) <2023 - 2025>  <Kevin Scott>                                                                      #
#                                                                                                                           #
#    Parse the command line arguments.                                     .                                                #
#                                                                                                                           #
#   positional arguments:                                                                                                   #
#     infile                                                                                                                #
#                                                                                                                           #
#   options:                                                                                                                #
#     -h, --help            show this help message and exit                                                                 #
#     -l, --license         Print the Software License.                                                                     #
#     -v, --version         Print the version of the application.                                                           #
#     -e, --explorer        Load program working directory into file explorer.                                              #
#     -b, --build           Build the data - consolidate the spreadsheets.                                                  #
#     -r, --report          Report on the data - finds the monthly highs and lows.                                          #
#     -Y, --Yreport         Report on the data - finds the yearly highs and lows.                                           #
#     -A, --Areport         Report on the data - finds the all time highs and lows.                                         #
#     -C, --Create          Creates the SQLite3 database and tables. [WARNING WILL DROP TABLES IF EXITS].                   #
#     -CY, --CreateYES      Creates the SQLite3 database and tables. **DOES NOT ASK** [WARNING WILL DROP TABLES IF EXITS].  #
#     -V, --Verbose         Verbose - print more detail.                                                                    #
#     -c, --config          Print out the config values.                                                                    #
#     -m MONTH, --month MONTH                                                                                               #
#                        Month of data files.                                                                               #
#     -y YEAR, --year YEAR  Year of data files.                                                                             #
#     -as TOFILE, --ToFile TOFILE                                                                                           #
#                        Archive data to file.                                                                              #
#     -al FROMFILE, --FromFile FROMFILE                                                                                     #
#                        Load data from file.                                                                               #
#                                                                                                                           #
#    Kevin Scott (C) 2023 - 2024 :: pyWeatherApp V2024.28                                                                   #
#                                                                                                                           #
#     For changes see history.txt                                                                                           #
#                                                                                                                           #
#############################################################################################################################
#                                                                                                                           #
#    This program is free software: you can redistribute it and/or modify it under the terms of the                         #
#    GNU General Public License as published by the Free Software Foundation, either Version 3 of the                       #
#    License, or (at your option) any later Version.                                                                        #
#                                                                                                                           #
#    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without                      #
#    even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                             #
#    GNU General Public License for more details.                                                                           #
#                                                                                                                           #
#    You should have received a copy of the GNU General Public License along with this program.                             #
#    If not, see <http://www.gnu.org/licenses/>.                                                                            #
#                                                                                                                           #
#############################################################################################################################

import sys
import textwrap
import argparse
import calendar

from pathlib import Path

import src.license as License
import src.utils.dataUtils as utils

############################################################################################## parseArgs ######
def parseArgs(Config, logger):
    """  Process the command line arguments.

         Checks the arguments and will exit if not valid.

         Exit code 0 - program has exited normally, after print version, licence or help.
    """
    months = calendar.month_name[1:]
    years  = ["2023", "2024", "2025"]

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description=textwrap.dedent("""\
        Builds a main data store out of individual weather data spreadsheets.
        The data store can be either an Excel spreadsheet or a SQLite3 database.
        The type of data store is specified in config.toml."""),
        epilog=f" Kevin Scott (C) 2023 - 2024 :: {Config.NAME} V{Config.VERSION}")

    parser.add_argument("-l",  "--license",    action="store_true", help="Print the Software License.")
    parser.add_argument("-v",  "--version",    action="store_true", help="Print the version of the application.")
    parser.add_argument("-e",  "--explorer",   action="store_true", help="Load program working directory into file explorer.")
    parser.add_argument("-b",  "--build",      action="store_true", help="Build the data - consolidate the spreadsheets.")
    parser.add_argument("-r",  "--report",     action="store_true", help="Report on the data - finds the monthly highs and lows.")
    parser.add_argument("-Y",  "--Yreport",    action="store_true",  help="Report on the data - finds the yearly highs and lows.")
    parser.add_argument("-A",  "--Areport",    action="store_true",  help="Report on the data - finds the all time highs and lows.")
    parser.add_argument("-C",  "--Create",     action="store_true", help="Creates the SQLite3 database and tables. [WARNING WILL DROP TABLES IF EXITS].")
    parser.add_argument("-CY", "--CreateYES",  action="store_true", help="Creates the SQLite3 database and tables. **DOES NOT ASK** [WARNING WILL DROP TABLES IF EXITS].")
    parser.add_argument("-V",  "--Verbose",    action="store_true", help="Verbose - print more detail.")
    parser.add_argument("-c",  "--config",     action="store_true", help="Print out the config values.")
    parser.add_argument("-m",  "--month",      action="store", type=str, help="Month of data files.")
    parser.add_argument("-y",  "--year",       action="store", type=str, help="Year of data files.")
    parser.add_argument("-as",  "--ToFile",     action="store", type=Path, help="Archive data to file.")
    parser.add_argument("-al",  "--FromFile",     action="store", type=Path, help="Load data from file.")
    parser.add_argument("infile", nargs="?")

    args = parser.parse_args()

    if args.version:
        print("")
        utils.logPrint(logger, True, f"Running on {sys.version} Python", "info")
        utils.logPrint(logger, True, f"Running on {utils.sqlite3Version()} SQLite3", "info")
        utils.logPrint(logger, True, f"End of {Config.NAME} V{Config.VERSION}: Printed version", "info")
        utils.logPrint(logger, False, "-" * 100, "info")
        print("Goodbye.")
        sys.exit(0)

    if args.license:
        License.printLongLicense(Config.NAME, Config.VERSION, logger)
        logger.info(f"End of {Config.NAME} V{Config.VERSION} : Printed Licence")
        utils.logPrint(logger, False, "-" * 100, "info")
        print("Goodbye.")
        sys.exit(0)

    if args.explorer:
        utils.loadExplorer(logger)              # Load program working directory n file explorer.
        print("Goodbye.")
        sys.exit(0)

    if args.report and args.infile is not None: #  If a filename is given, check it exists.

        path = Path(args.infile)

        if path.is_file():
            print("File exists")
        else:
            utils.logPrint(logger, True, f"ERROR :: {args.infile} does not exist", "warning")
            utils.logPrint(logger, False, "-" * 100, "info")
            print("Goodbye.")
            sys.exit(2)

    if args.month:
        if args.month not in months:
            utils.logPrint(logger, True, f"ERROR :: {args.month} is not a valid month", "danger")
            utils.logPrint(logger, False, "-" * 100, "info")
            print("Goodbye.")
            sys.exit(3)

    if args.year:
        if args.year not in years:
            utils.logPrint(logger, True, f"ERROR :: {args.year} is not a valid year {years}", "danger")
            utils.logPrint(logger, False, "-" * 100, "info")
            print("Goodbye.")
            sys.exit(3)


    return(args.build, args.report, args.Areport, args.Yreport, args.infile, args.Verbose, args.Create, args.CreateYES, args.config, args.month, args.year, args.ToFile, args.FromFile)






