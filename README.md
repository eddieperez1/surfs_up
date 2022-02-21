# surfs_up

## Overview of Project
### Outline
The goal of this project is to investigate the weather data to open up a new surf shop in Oahu, Hawaii. Using sqlite and flask, weather data was display on a local website. Information about temperature trends before opening the surf shop needs to analyzed. Specifically, the temperature data for the months of June and December in Oahu was investigated, in order to determine if the surf and ice cream shop business is sustainable year-round.

### Requirements
The hawaii.sqlite is the database used in this project. The modules flask and sqlalchemy need to be installed to use the code in this project.

## Results
### Deliverable 1
Using Python, Pandas functions and methods, and SQLAlchemy, a query will gather date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of June. This query will be imported into a DataFrame and the summary statistics will be generated.

![screenshot of june temps](/Screenshots/screenshot_of_june_temps.PNG)

### Deliverable 2
Using Python, Pandas functions and methods, and SQLAlchemy, a query will gather date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of June. This query will be imported into a DataFrame and the summary statistics will be generated.

![screenshot of december temps](/Screenshots/screenshot_of_december_temps.PNG)

### Weather Differences between June and December
- A
- B
- C

## Summary
### Outcomes


### Additional Insights


### Query 1
```
june_prcp_df = pd.DataFrame(session.query(Measurement.prcp).filter(extract('month',Measurement.date) == "06").all())
june_prcp_df.rename(columns = {'prcp':'June Precipitation'},inplace = True)
june_prcp_df.describe()
```

![screenshot of june precipitation](/Screenshots/screenshot_of_june_precipitation.PNG)

### Query 2
```
dec_prcp_df = pd.DataFrame(session.query(Measurement.prcp).filter(extract('month',Measurement.date)=="12").all())
dec_prcp_df.rename(columns = {'prcp':'December Precipitation'},inplace = True)
dec_prcp_df.describe()
```

![screenshot of december precipitation](/Screenshots/screenshot_of_december_precipitation.PNG)