@rem   Simple build script for pyWeatherApps.py.
@rem   Allows multiple builds using a range of years and months.
@rem
@rem  main.py -C -m %%m -y %%y    <> To print out config for each month, year 
@rem  main.py -cb -m %%m -y %%y   <> To create and build for each month, year 
@rem  main.py -cbr -m %%m -y %%y  <> To create, build and report for each month, year
@rem
@rem  The python environment must be activated.
@rem
@rem   <2023> (c) Kevin Scott

@echo OFF

FOR %%y IN (2023) DO (
    FOR %%m IN (July August September) DO (
    main.py -r -m %%m -y %%y)
)

