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
- June average temperature is higher than December average temperature
- June maximum temperature is higher than December maximum temperature
- June minimum temperature is lower than December minimum temperature

## Summary
### Outcomes

The results show that the temperature during the June and December average temperatures are higher than 70 degrees F. Thus, the weather in Oahu, Hawaii is good for making a surfing shop. The standard deviation is 3.257417 and 3.745920 for June and December temperatures respectively, therefore the variance in temperature is not large enough to close the surfing shop due to temperature. The max temperature is 85 degress F and 83 degrees F for June and December temperatures respectively, hence it will not get too hot for surfers.

### Additional Insights

To make more in depth analysis, the precepitation for months of June and December were investigated. The June precipitation was found using Query 1 below and the December precipitation was found using Query 2 below. Whether it rains a lot in certain months can be critical information to determine when to have the surfing shop open. It may be beneficial to analyze more months between June and December. From the precipitation data, the average precipitation is 0.136360 and 0.216819 inches for June and Decemeber precipitation respectively.

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
