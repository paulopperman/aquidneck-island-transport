# Rhode Island Statewide Model Origin-Destination Data
These datafiles are extracted from the RISM describing the number of trips between origin and destination traffic analysis zones.
These TAZs are mapped to the network model by the files in the `tazs/` folder in the model repository.  OD files are given
for each of the main vehicular demand types in the RISM:

* **Home-Based Non-Work** *(HBNW)* - Trips between a residence and a non-work location
* **Home-Based Work** *(HBW)* - Trips between a residence and a work location
* **Non-Home-Based** *(NHBW)* - Trips between locations other than a residence
* **Truck** *(Truck)* - Trips for commercial truck traffic

Bridge-to-bridge traffic is estimated as a scaled proportion of trips between aggregate zones served by each bridge.

Trip definitions can be created by running the `OD2TRIPS` tool using a command like:  
```
od2trips -c od_data/<scenario>_trip_config.cfg.xml -o trip_files/<scenario>_run<run_number>.trips.rou.xml --error-log logs/<scenario>_run<run_number>_od2trips_errors.txt --seed <random_seed>
```

