###############################################################################################################
#    myConfig.py    Copyright (C) <2023>  <Kevin Scott>                                                       #
#                                                                                                             #
#    A class that acts has a wrapper around the configure file - config.toml.                                 #
#    The configure file is first read, then the properties are made available.                                #
#    The configure file is currently in toml format.                                                          #
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

import toml
import colorama


class Config():
    """  A class that acts has a wrapper around the configure file - config.toml.
         The configure file is hard coded and lives in the same directory has the main script.
         The configure file is first read, then the properties are made available.

         If config.toml is not found, a default configure file is generated.

         usage:
            myConfig = myConfig.Config()
    """

    FILE_NAME = "config.toml"

    def __init__(self):
        try:
            with open(self.FILE_NAME, "r") as configFile:       # In context manager.
                self.config = toml.load(configFile)             # Load the configure file, in toml.
        except FileNotFoundError:
            print(f"{colorama.Fore.RED}Configure file not found. {colorama.Fore.RESET}")
            print(f"{colorama.Fore.YELLOW}Writing default configure file. {colorama.Fore.RESET}")
            self._writeDefaultConfig()
            print(f"{colorama.Fore.GREEN}Running program with default configure settings. {colorama.Fore.RESET}")
        except toml.TomlDecodeError:
            print(f"{colorama.Fore.RED}Error reading configure file. {colorama.Fore.RESET}")
            print(f"{colorama.Fore.YELLOW}Writing default configure file. {colorama.Fore.RESET}")
            self._writeDefaultConfig()
            print(f"{colorama.Fore.GREEN}Running program with default configure settings. {colorama.Fore.RESET}")

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
        location  = self.config["DATA"]["directory"]
        filename  = self.config["DATA"]["mainwWorkBook"]
        extension = "xlsx"
        return f"{location}\\{filename}.{extension}"



    def _writeDefaultConfig(self):
        """ Write a default configure file.
            This is hard coded  ** TO KEEP UPDATED **
        """
        config = dict()

        config["INFO"] = {"myVERSION": "2023.5.beta",
                          "myNAME"   : "pyDataBuild"}


        st_toml = toml.dumps(config)

        with open(self.FILE_NAME, "w") as configFile:       # In context manager.
            configFile.write("#   Configure files for pyDataBuild.py \n")
            configFile.write("#\n")
            configFile.write("#   true and false are lower case \n")
            configFile.write("#   location needs double \ i.e. c:\\tmp\\music - well, on windows any way. \n")
            configFile.write("#\n")
            configFile.write("#   <2023> (c) Kevin Scott \n")
            configFile.write("\n")
            configFile.writelines(st_toml)                  # Write configure file.

        with open(self.FILE_NAME, "r") as configFile:       # In context manager.
            self.config = toml.load(configFile)             # Load the configure file, in toml.