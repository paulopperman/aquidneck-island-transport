# Traffic Assignment Zones

### newport_neighborhoods.xml
The `newport_neighborhoods.xml` TAZ file was manually built for simple testing of the Newport network.

## RI State Highway Model TAZs
The `aquidneck_taz.pol.xml` file contains the geometry used in the RI state traffic model and corresponds to the model's O-D data.  It was converted from a shapefile of TAZs using `POLYCONVERT`:  
```
polyconvert --shapefile-prefixes RITAZ15_aquidneck --shapefile.id-column ID --shapefile.guess-projection --proj.utm --offset.x -298290.21 --offset.y -4591339.97 -o aquidneck_taz.pol.xml
```

The offset is taken from the `aquidneck_island.net.xml` network offset.  `edgesInDistrics.py` was used to define the edges in `aquidneck_taz.taz.xml`:  
```
python <SUMO_HOME>\tools\edgesInDistricts.py -n ..\aquidneck_island.net.xml -i -f -s -t aquidneck_taz.pol.xml -o aquidneck_taz.taz.xml
```
### RI TAZs by Mode
`aquidneck_car.taz.xml`, `aquidneck_truck.taz.xml`, and `aquidneck_walk.taz.xml` are generated using the `filterDistricts.py` tool:
```
python <SUMO_HOME>\tools\district\filterDistricts.py -n ../aquidneck_island.net.xml -t aquidneck_taz.taz.xml -o aquidneck_car.taz.xml --vclass passenger
```
The `--vclass` option was set to `pedestrian` and `truck` for the walk and truck TAZs, respectively.
