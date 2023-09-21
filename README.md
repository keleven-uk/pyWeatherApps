 PyDataBuild.

  Scans a given directory for excel spreadsheets the contains daily weather data and for
  new data then adds them to a main spreadsheet or SQLite3 database.
    
  The apps include -
                    pyDataXBuild   - scans a number of excel files and merges into one file.
                    pyDataXeport   - scans the main file and finds the highs and lows.
                    pyDataSQLBuild - scans a number of excel files and merges into one SQLite3 database.
                    pyDataSQLeport - scans the main SQL file and finds the highs and lows.


usage: main.py [-h] [-l] [-v] [-e] [-b] [-r] [-rA] [-c] [-V] [-C] [-m MONTH] [-y YEAR] [infile]

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
  -rA, --ATreport       Report on the data - finds the all time highs and lows.
  -c, --create          Creates the SQLite3 database and tables. [WARNING WILL DROP TABLES IF EXITS].
  -V, --Verbose         Verbose - print more detail.
  -C, --Config          Print out the config values.
  -m MONTH, --month MONTH
                        Month of data files.
  -y YEAR, --year YEAR  Year of data files.

 Kevin Scott (C) 2023 :: pyWeatherApp V2023.18.beta


To install dependencies pip -r requirements.txt

For changes see history.txt
