# Calibration Files
These files are used with the `modifiedRouteSampler.py` tool to calibrate flows on the street network.

## Datafile Descriptions
Each calibration datafile is calculated from RI Department of Transportation traffic counts.

### `weekday_mean`
The weekday mean data are the hourly mean bi-directional count aggregated over weekdays (M-F) over the entire history of the available counter data.

### `weekday_survey_2019`
The 2019 weekday survey data are the hourly mean computed for a subset of the counters.  The survey was conducted at a large number of counters
across Aquidneck Island over a 2-weekday period in May 2019.  While this does not give as much statistical confidence in general traffic flow,
 it provides a large number of network measurements that are correlated in time for calibration.
 
### `weekend_mean`
The weekend mean data are the hourly mean bi-directional count aggregated over weekends (Sa-Su) over the entire history of the available counter data.

### `weekday_XX_quantile`
The weekday quantile data are the hourly XX quantile bi-directional count aggregated over weekdays over the entire history of the available counter data.
The different quantiles are provided to calibrate for statistically lighter or heavier traffic days.