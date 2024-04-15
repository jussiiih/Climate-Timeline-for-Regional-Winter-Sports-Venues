import pandas as pd

vuokatti2004_2009 = pd.read_csv("snow depth\\Vuokatti\\Sotkamo Saviaho_ 1.1.2004 - 31.12.2009_d3075c19-89de-43d7-9bfe-8b6fa99af96e.csv")
vuokatti2010_2024  = pd.read_csv("snow depth\\Vuokatti\\Sotkamo Kuolaniemi_ 1.1.2010 - 1.1.2024_c3dedb06-4bf1-4b48-a353-0ac9504da276.csv")

file = pd.concat([vuokatti2004_2009, vuokatti2010_2024])

file["Date"] = pd.to_datetime(file[["Year", "Month", "Day"]]) 
file.drop(["Year", "Month", "Day", "Time [Local time]", "Observation station"], axis=1, inplace = True)
file.to_csv("C:\\Code\\Tuulikaappi\\snow depth\\Valmis\\vuokatti_snow_depth.csv", index=False) 