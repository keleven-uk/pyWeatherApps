###############################################################################################################
#    myConfig.py    Copyright (C) <2023 - 2024>  <Kevin Scott>                                                #
#                                                                                                             #
#    A class that acts has a wrapper around the configure file - config.toml.                                 #
#    The configure file is first read, then the properties are made available.                                #
#    The configure file is currently in toml format.                                                          #
#                                                                                                             #
###############################################################################################################
#    Copyright (C) <2023 - 2024>  <Kevin Scott>                                                               #
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

import toml

from src.console import console


class Config():
    """  A class that acts has a wrapper around the configure file - config.toml.
         The configure file is hard coded and lives in the same directory has the main script.
         The configure file is first read, then the properties are made available.

         If config.toml is not found, a default configure file is generated.

         usage:
            myConfig = myConfig.Config()
    """

    FILE_NAME = "Config.toml"

    def __init__(self):
        try:
            with open(self.FILE_NAME, "r") as configFile:       # In context manager.
                self.config = toml.load(configFile)             # Load the configure file, in toml.
        except FileNotFoundError:
            console.print("Configure file not found.", "warning")
            console.print("Writing default configure file.", "warning")
            console,print("Please check config values.", "warning")
            self._writeDefaultConfig()
            console.print("Running program with default configure settings.", "warning")
        except toml.TomlDecodeError:
            console.print("Configure file can't be read.", "warning")
            console.print("Writing default configure file.", "warning")
            console,print("Please check config values.", "warning")
            self._writeDefaultConfig()
            console.print("Running program with default configure settings.", "warning")

    @property
    def NAME(self):
        """  Returns application name.
        """
        return self.config["INFO"]["myNAME"]

    @property
    def VERSION(self):
        """  Returns application Version.
        """
        return self.config["INFO"]["myVERSION"]

    @property
    def MAIN_WB(self):
        """  return should be like - data\\2023\\db\\July2023.xlsx
        """
        data_dir  = self.config["DATA"]["data_dir"]
        db_year   = self.config["DATA"]["year"]
        db_dir    = self.config["DATA"]["db_dir"]
        month     = self.config["DATA"]["month"]
        year      = self.config["DATA"]["year"]
        extension = "xlsx"
        return f"{data_dir}\\{db_year}\\{db_dir}\\{month}{year}.{extension}"

    @property
    def MAIN_DB(self):
        """  return should be like - data\\2023\\db\\July2023.sql
        """
        data_dir  = self.config["DATA"]["data_dir"]
        db_year   = self.config["DATA"]["year"]
        db_dir    = self.config["DATA"]["db_dir"]
        month     = self.config["DATA"]["month"]
        year      = self.config["DATA"]["year"]
        extension = "sql"
        return f"{data_dir}\\{db_year}\\{db_dir}\\{month}{year}.{extension}"

    @property
    def RECORD_FILES(self):
        """  return should be like - data\\records\\July2013.pickle
        """
        data_dir  = self.config["DATA"]["data_dir"]
        rec_year  = self.config["DATA"]["year"]
        rec_dir   = self.config["DATA"]["rec_dir"]
        filename  = self.config["DATA"]["month"]
        year      = self.config["DATA"]["year"]
        extension = "pickle"
        return f"{data_dir}\\{rec_year}\\{rec_dir}\\{filename}{year}.{extension}"

    @property
    def YEAR_RECORD_FILES(self):
        """  return should be like - data\\2023\records\\2033.pickle
        """
        data_dir  = self.config["DATA"]["data_dir"]
        rec_year  = self.config["DATA"]["year"]
        rec_dir   = self.config["DATA"]["rec_dir"]
        year      = self.config["DATA"]["year"]
        extension = "pickle"
        return f"{data_dir}\\{rec_year}\\{rec_dir}\\{year}.{extension}"

    @property
    def ALLTIME_RECORD_FILES(self):
        """  return should be like - data\\records\\July2013.pickle
        """
        data_dir  = self.config["DATA"]["data_dir"]
        extension = "pickle"
        return f"{data_dir}\\allTime.{extension}"

    @property
    def TARGET_FILES(self):
        """  return should be like - data\\2023\\July2003\\July2023\\all*.xlsx
        """
        data_dir = self.config["DATA"]["data_dir"]
        xl_dir   = self.config["DATA"]["xl_dir"]
        month    = self.config["DATA"]["month"]
        year     = self.config["DATA"]["year"]
        target   = self.config["DATA"]["target"]
        return f"{data_dir}\\{year}\\{xl_dir}\\{month}\\{target}"

    @property
    def TARGET(self):
        """  return should be like - all*.xlsx
        """
        target   = self.config["DATA"]["target"]
        return f"{target}"

    @property
    def MONTH(self):
        month = self.config["DATA"]["month"]
        return f"{month}"

    @property
    def YEAR(self):
        data_dir = self.config["DATA"]["year"]
        return f"{data_dir}"

    @property
    def DATA_DIR(self):
        data_dir = self.config["DATA"]["data_dir"]
        return f"{data_dir}"

    @property
    def REC_DIR(self):
        rec_dir = self.config["DATA"]["rec_dir"]
        return f"{rec_dir}"

    @property
    def DB_DIR(self):
        db_dir = self.config["DATA"]["db_dir"]
        return f"{db_dir}"

    @property
    def XL_DIR(self):
        db_dir = self.config["DATA"]["xl_dir"]
        return f"{db_dir}"

    @property
    def DB_TYPE(self):
        db_type = self.config["DB"]["type"]
        return f"{db_type}"

    @property
    def ARCHIVE_TYPE(self):
        archive_type = self.config["ARCHIVE"]["type"]
        return f"{archive_type}"



    def _writeDefaultConfig(self):
        """ Write a default configure file.
            This is hard coded  ** TO KEEP UPDATED **
        """
        config = dict()

        config["INFO"]    = {"myVERSION" : "2024.27",
                             "myNAME"    : "pyWeatherApp"}

        config["DATA"]    = {"data_dir"  : "data",
                             "xl_dir"    : "xl",
                             "db_dir"    : "db",
                             "rec_dir"   : "records",
                             "month"     : "January",
                             "year"      : "2024",
                             "target"    : "all*.xlsx"}

        config["DB"]      = {"type"      : "sqlite"}        #  either "sqlite" OR "excel"

        config["ARCHIVE"] = {"ARCHIVE"   : "zip"}           #  type of archive used. - bztar, gztar, tar, xztar or zip


        st_toml = toml.dumps(config)

        with open(self.FILE_NAME, "w") as configFile:       # In context manager.
            configFile.write("#   Configure files for pyDataBuild.py \n")
            configFile.write("#\n")
            configFile.write("#   true and false are lower case \n")
            configFile.write("#\n")
            configFile.write("#   <2023> (c) Kevin Scott \n")
            configFile.write("\n")
            configFile.writelines(st_toml)                  # Write configure file.

        with open(self.FILE_NAME, "r") as configFile:       # In context manager.
            self.config = toml.load(configFile)             # Load the configure file, in toml.
