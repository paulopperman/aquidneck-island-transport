---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---
# About the Model
The Aquidneck Island Transport Model is a transportation microsimulation model of Aquidneck Island built 
using [SUMO](https://www.eclipse.org/sumo/).  It is capable of simulating cars, buses, bikes, pedestrians, 
and many other modes of transportation to study how traffic flows on the local transportation network.

<img id="full_map" alt="The full Aquidneck Island Transport Model network" src="assets/img/full_network.png">

This model is a community built and maintained tool for understanding the local 
transportation network to help develop meaningful recommendations for changes and to provide a 
validated point of comparison with other public and private traffic analyses.  It is open source and open data released
under the [CC BY-SA-4.0 license](https://creativecommons.org/licenses/by-sa/4.0/) for use by anyone studying
transportation on Aquidneck Island.


### Network Model
The network model represents the roads, sidewalks, and bike paths on Aquidneck Island out to just beyond the bridges. It
includes traffic signals and is capable of simulating parking.  The network model is built from
[OpenStreetMap](https://openstreetmap.org) data and local surveys to capture the unique features of the local streets:

* Pedestrian routes
* Traffic signals
* Naval Station Newport traffic restrictions


### Demand Model
The Aquidneck Island Transport Model includes a [baseline set](https://github.com/paulopperman/aquidneck-island-transport/tree/master/scenarios/aquidneck_island_traffic_model) of traffic scenarios generated from the 
[Rhode Island Statewide Model](http://www.planning.ri.gov/planning-areas/transportation/travel-demand-model.php)
and calibrated against [RIDOT](http://www.dot.ri.gov) traffic counts. Additional scenarios can be added easily using
the tools included with the SUMO software.  Because the model is capable of simulating multiple travel modes, it can be 
model trips by individual people from an origin to a destination using any types of transportation available.


# Use Cases
The Aquidneck Island Transport Model is a general model that is intended to be tailored to study specific issues before 
any changes are made on the street network. It can be used as a point of comparison with studies conducted by governments and private organizations to check their 
assumptions, and it can be used by planners as additional data in a project study.  Here are just a few examples of questions
the model could be used to answer:

##### Traffic Pattern Changes
* How does a road closure affect traffic in the immediate area?
* Are there ripple-effects of the change elsewhere on the Island?
* Where should sensors be deployed during a test of a new traffic pattern?

##### Human-Friendly Network
* Do safe pedestrian routes exist in an area?
* Would pedestrian and bicycle infrastructure improvements actually impact motor vehicle trips in the area?
* Are alternative transportation modes more effective for a project than car-centric planning?

##### Parking Policy
* How does parking affect traffic today?
* How would parking changes impact traffic?
* Are mass transportation or pedestrian routes viable for new parking schemes?

##### Traffic Signal Optimization
* How do traffic signal timings impact traffic on the Island?
* Are there signals that could be optimized to improve traffic flow?
* How could new traffic signal technology improve transportation on the Island?

##### Vehicle Restrictions
* Where would large vehicles go if certain roads become restricted to truck traffic?
* Would emissions or safety be impacted by vehicle restrictions in an area?
* Are businesses affected by altered logistics routes?

##### Special Events and Emergency Planning
* How does extreme traffic flow impact the network?
* How would natural events like flooding impact traffic flow?
* What is the risk of blocking emergency responders with traffic?
* How would alternative modes of transportation help traffic flow, emissions, and safety?