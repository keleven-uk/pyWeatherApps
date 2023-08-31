 PyDataBuild.

  Scans a given directory for excel spreadsheets the contains daily weather data and for
  new data then adds them to a main spreadsheet or SQLite3 database.
    
  The apps include -
                    pyDataXBuild   - scans a number of excel files and merges into one file.
                    pyDataXeport   - scans the main file and finds the highs and lows.
                    pyDataSQLBuild - scans a number of excel files and merges into one SQLite3 database.


usage: main.py [-h] [-l] [-v] [-e] [-b] [-r] [-c] [-V]

Builds a main data store out of individual weather data spreadsheets.
The data store can be either an Excel spreadsheet or a SQLite3 database.
The type of data store is specified in config.toml.

options:
  -h, --help      show this help message and exit
  -l, --license   Print the Software License.
  -v, --version   Print the version of the application.
  -e, --explorer  Load program working directory into file explorer.
  -b, --build     Build the data - consolidate the spreadsheets.
  -r, --report    Report on the data - finds the highs and lows.
  -c, --create    Creates the SQLite3 database and tables.
  -V, --Verbose   Verbose - print more detail.

 Kevin Scott (C) 2023 :: pyWeatherApp 2023.13


For changes see history.txt
