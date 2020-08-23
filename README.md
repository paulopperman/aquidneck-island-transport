# Aquidneck Island Transport Model
This repository contains a network model around Aquidneck Island for use in [SUMO](https://sumo.dlr.de/wiki/Simulation_of_Urban_MObility_-_Wiki) simulations.

![network overview](images/netedit_overview_map.png)

![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)  This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

This code base is designed to allow customization of the SUMO network based on OpenStreetMap data, in such a way that it can be reconstituted from scratch using `netconvert`.

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
Before running the calibrated Aquidneck Island Traffic Model scenarios, the trip and route files need to be generated.
In `scenarios/aquidneck_island_traffic_model/` run `ai_tripgen.py` to generate the intermediate files for simulation. 
Once the files have been computed, the simulation can be run using one of the configuration files in the scenario directory.
General simulation results are written by default, but additional data can be obtained by modifying the configuration file per the SUMO [documentation](https://sumo.dlr.de/docs/sumo.html).

### Using Docker
From this folder, run 
```docker run -it --name aquidneck --mount type=bind,source="$(pwd),target=/model paulopperman/sumo-docker:latest```
and use the command line interface to run the desired simulation.

## Mapping Workflow

1. Obtain source data
Download the OpenStreetMap data from overpass by navigating to [https://overpass-api.de/api/map?bbox=-71.4022,41.4471,-71.1742,41.6578
](https://overpass-api.de/api/map?bbox=-71.4022,41.4471,-71.1742,41.6578
) in a browser.
2. Run netconvert
Run `netconvert -c netconvert_configuration.netc.cfg`
3. Extract polygons
  Run `polyconvert -c polyconvert_configuration.cfg.xml` to create the polygon file.

As much as possible should be included by editing either the OpenStreetMap database (for errors or clarifications, following the [contribution guidelines](https://wiki.openstreetmap.org/wiki/Good_practice)) or in the [netconvert configuration file](netconvert_configuration.netc.cfg) to tweak how the source data is translated.

### Tracking network changes

Network patch files are generated using the `netdiff.py` tool included with SUMO.  Tool documentation is [here](https://sumo.dlr.de/docs/Tools/Net.html#netdiffpy).  To rebuild the model using new baseline data:
```
netconvert --sumo-net-file baseline.net.xml -n patches\aquidneck_island_diff.nod.xml -e patches\aquidneck_island_diff.edg.xml -x patches\aquidneck_island_diff.con.xml -i patches\aquidneck_island_diff.tll.xml -o aquidneck_island.net.xml
```

Run the `netdiff.py` tool to update the patch files in the `patches/` directory prior to merging any network changes into the `master` branch.


