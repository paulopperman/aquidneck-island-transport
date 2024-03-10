# Aquidneck Island Transport Model
This repository contains a network model around Aquidneck Island for use in [SUMO](https://sumo.dlr.de/wiki/Simulation_of_Urban_MObility_-_Wiki) simulations.

![network overview](images/netedit_overview_map.png)

![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)  This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).


## Model Features
The Aquidneck Island Transport Model is a microsimulation model including a model of the transportation network and 
calibrated user demand scenarios built from the Rhode Island Statewide Model and state traffic counter data.  The model
includes accurate lane behaviors, and work is ongoing to accurately model the traffic signal programs.  The model also includes
specific local features, such as routing restrictions and gate behaviors at Naval Station Newport, and shoulder passing on certain streets.

### Planned Updates
This model is under continual development to incorporate more features to realistically model traffic on the island. Some planned future features include:
* Public transportation routes
* Pedestrian user demand and multi-modal trips
* Parking and parking-searching traffic demand

## Running a Simulation
*Model currently working in SUMO v1.11.0*  
Before running the calibrated Aquidneck Island Traffic Model scenarios, the trip and route files need to be generated.
In `demand/scripts/` run `aitm_tripgen.py` to generate the intermediate files for simulation. 
Once the files have been computed, the simulation can be run using one of the configuration files in the scenario directory.
General simulation results are written by default, but additional data can be obtained by modifying the configuration file per the SUMO [documentation](https://sumo.dlr.de/docs/sumo.html).

### Using Docker
From this folder, run 
```docker run -it --name aquidneck --mount type=bind,source="$(pwd),target=/model paulopperman/sumo-docker:latest```
and use the command line interface to run the desired simulation.

## Street Network Source Data

The bounding box for the network model is `[-71.4022,41.4471,-71.1742,41.6578]`.  

The network is built from OpenStreetMap data accessed with the overpass api from the following address: [https://overpass-api.de/api/map?bbox=-71.4022,41.4471,-71.1742,41.6578
](https://overpass-api.de/api/map?bbox=-71.4022,41.4471,-71.1742,41.6578
).  Additional detail and corrections have been made directly to the network file.



