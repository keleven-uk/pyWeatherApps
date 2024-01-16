@rem   Simple build script for pyWeatherApps.py.
@rem   Allows multiple builds using a range of years and months.
@rem
@rem  main.py -c -m %%m -y %%y    <> To print out config for each month, year
@rem  main.py -Cb -m %%m -y %%y   <> To create and build for each month, year
@rem  main.py -Cbr -m %%m -y %%y  <> To create, build and report for each month, year
@rem
@rem  The python environment must be activated.
@rem
@rem   <2023> (c) Kevin Scott

@echo OFF

@rem FOR %%y IN (2023) DO (
@rem     FOR %%m IN (July August September October November December) DO (
@rem         main.py -r -m %%m -y %%y
@rem     )
@rem )
@rem main.py -rA

main.py -Cb
main.py -r

