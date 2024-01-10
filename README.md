 PyMP3duplicate.

    PyDataBuild.

    Scans a given directory for excel spreadsheets the contains daily weather data and for
     new data then adds them to a main spreadsheet or SQLite3 database.

    The apps include -
     pyDataXBuild - scans a number of excel files and merges into one file.
     pyDataXReport - scans the main file and finds the highs and lows.
     pyDataSQLBuild - scans a number of excel files and merges into one SQLite3 database.
     pyDataSQLReport - scans the main SQL file and finds the highs and lows.

To install dependencies pip -r requirements.txt

usage: main.py [-h] [-l] [-v] [-e] [-b] [-r] [-Y] [-A] [-C] [-CY] [-V] [-c] [-m MONTH] [-y YEAR] [infile]

Builds a main data store out of individual weather data spreadsheets.
The data store can be either an Excel spreadsheet or a SQLite3 database.
The type of data store is specified in config.toml.

    usage: main.py [-h] [-l] [-v] [-e] [-b] [-r] [-Y] [-A] [-C] [-CY] [-V] [-c] [-m MONTH] [-y YEAR] [infile]

    Builds a main data store out of individual weather data spreadsheets.
    The data store can be either an Excel spreadsheet or a SQLite3 database.
    The type of data store is specified in config.toml.

    positional arguments:
      infile

    options:
      -h, --help            show this help message and exit
      -l, --license         Print the Software License.
      -v, --version         Print the version of the application.
      -e, --explorer        Load program working directory into file explorer.
      -b, --build           Build the data - consolidate the spreadsheets.
      -r, --report          Report on the data - finds the monthly highs and lows.
      -Y, --Yreport         Report on the data - finds the yearly highs and lows.
      -A, --Areport         Report on the data - finds the all time highs and lows.
      -C, --Create          Creates the SQLite3 database and tables. [WARNING WILL DROP TABLES IF EXITS].
      -CY, --CreateYES      Creates the SQLite3 database and tables. **DOES NOT ASK** [WARNING WILL DROP TABLES IF EXITS].
      -V, --Verbose         Verbose - print more detail.
      -c, --config          Print out the config values.
      -m MONTH, --month MONTH
                            Month of data files.
      -y YEAR, --year YEAR  Year of data files.

     Kevin Scott (C) 2023 - 2024 :: pyWeatherApp V2023.26

For changes see history.txt
