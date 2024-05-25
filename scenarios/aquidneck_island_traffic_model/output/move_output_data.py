import sys, os, shutil
import xml.etree.ElementTree as ET
# add sumo tools to path to continue imports
if "SUMO_HOME" in os.environ:
	sumotools = os.path.join(os.environ['SUMO_HOME'], 'tools/xml')
	sumoxsd = os.path.join(os.environ['SUMO_HOME'], 'data/xsd')
	sys.path.append(sumotools)
else:
	sys.exit("please declare environment variable 'SUMO_HOME'")

import xml2csv

# specify the scenario
scenario_name = "ai25_run0"

# convert standard outputs for the scenario
try:
	xml2csv.main(('./%s/ai_simulation_vehroutes.xml'%(scenario_name), '-x', os.path.join(sumoxsd,'routes_file.xsd')))
	xml2csv.main(('./%s/ai_simulation_summary.xml' % (scenario_name), '-x', os.path.join(sumoxsd, 'summary_file.xsd')))
	xml2csv.main(('./%s/ai_simulation_tripinfo.xml' % (scenario_name), '-x', os.path.join(sumoxsd, 'tripinfo_file.xsd')))
except ValueError:
	sys.exit("Unknown scenario name")

# convert and move additional simulation measurements from ./measurements
add_files = [x for x in os.listdir('../measurements') if x.endswith('.add.xml')]

# parse the measurements file to get the output files
datafiles = []	#initialize empty list
for file in add_files:
	root = ET.parse('../measurements/' + file).getroot()
	for child in root:
		if child.tag == 'edgeData':  #todo look for lane data
			datafiles.append(child.attrib.get('file'))

# # convert and move the output files
for file in datafiles:
	file = file.split('/')[-1]
	xml2csv.main((file, '-x', os.path.join(sumoxsd,'meandata_file.xsd')))
	shutil.move(file, './%s/%s'%(scenario_name,file))
	csvfile = file.removesuffix('.xml') +'.csv'
	shutil.move(csvfile, './%s/%s'%(scenario_name, csvfile))

# convert and move ridot detector files
det_files = ['../../../detectors/output/ridot_detectors/' + x for x in os.listdir('../../../detectors/output/ridot_detectors') if x.endswith('.xml')]

for file in det_files:
	root = ET.parse(file).getroot()
	schema = list(zip(root.attrib.values()))[0][0].split('/')[-1]
	schema_file = os.path.join(sumoxsd,schema)
	xml2csv.main((file, '-x', schema_file))
	filename = file.split('/')[-1]
	shutil.move(file, './%s/ridot_detectors/%s'%(scenario_name, filename))
	shutil.move(file.removesuffix('.xml') + '.csv', './%s/ridot_detectors/%s' % (scenario_name, filename.removesuffix('.xml')+'.csv'))