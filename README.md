# SUMO Model of Aquidneck Island
This repository contains a network model around Aquidneck Island for use in [SUMO](https://sumo.dlr.de/wiki/Simulation_of_Urban_MObility_-_Wiki) simulations.

![network overview](images/netedit_overview_map.png)

This code base is designed to allow customization of the SUMO network based on OpenStreetMap data, in such a way that it can be reconstituted from scratch using `netconvert`.

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

When editing using NETEDIT, save the network as a new set of plain xml files.  **Work is in progress to generate patch files using xmldiff.**


## Running a Simulation
A sample simulation can be built using the `newport_neighborhoods.xml` traffic assignment zones and `OD2TRIPS`. Build the trip configuration file by calling `OD2TRIPS -c baseline_trip_config.cfg.xml`.  Then run `baseline_sim_config.sumocfg` in SUMO or SUMO-GUI.
