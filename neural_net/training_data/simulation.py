'''
Run SUMO with inputs to generate the network training data.
'''
import os, sys
if 'SUMO_HOME' in os.environ:
	tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
	sys.path.append(tools)
else:
	sys.exit('please declare environment variable "SUMO_HOME"')

import numpy as np
import pandas as pd
import traci
from multiprocessing import Pool

sumo_binary = os.path.join(os.environ['SUMO_HOME'], 'bin\sumo.exe')

DETECTOR_IDS = [  # TODO: build this from the xml files next time...
	"190001_1_NB",
	"190001_1_SB",
	"190001_2_NB",
	"190001_2_SB",
	"190004_1_NB",
	"190004_1_SB",
	"190053_1_NB",
	"190053_1_SB",
	"190053_2_NB",
	"190053_2_SB",
	"210001_1_NB",
	"210001_1_SB",
	"270021_1_NB",
	"270021_1_SB",
	"270025_1_NB",
	"270025_1_SB",
	"270025_2_NB",
	"270025_2_SB",
	"270040_1_NB",
	"270040_1_SB",
	"270040_2_NB",
	"270040_2_SB",
	"270045_1_NB",
	"270045_1_SB",
	"270045_2_NB",
	"270045_2_SB",
	"199000_EB",
	"199000_WB",
	"199002_NB",
	"199002_SB",
	"199003_SB",
	"199003_NB",
	"199006_NB",
	"199006_SB",
	"199008_NB",
	"199008_SB",
	"199013_NB",
	"199013_SB",
	"199015_NB",
	"199015_SB",
	"199016_EB",
	"199016_WB",
	"199018_NB",
	"199018_SB",
	"219000_NB",
	"219000_SB",
	"219001_1_NB",
	"219001_1_SB",
	"219001_2_NB",
	"219001_2_SB",
	"219002",
	"219004",
	"219005_EB",
	"219005_WB",
	"219006",
	"219008_SB",
	"219008_NB",
	"219011",
	"219012_NB",
	"219012_SB",
	"219013_NB",
	"219013_SB",
	"219014",
	"219015_NB",
	"219015_SB",
	"219016_NB",
	"219016_SB",
	"219017_NB",
	"219017_SB",
	"219018",
	"219021_NB",
	"219021_SB",
	"219023_1_NB",
	"219023_1_SB",
	"219023_2_NB",
	"219023_2_SB",
	"219024_NB",
	"219024_SB",
	"219025_NB",
	"219025_SB",
	"219027_NB",
	"219027_SB",
	"219030",
	"219031_NB",
	"219031_SB",
	"219032_NB",
	"219032_SB",
	"219033_NB",
	"219033_SB",
	"219034_NB",
	"219034_SB",
	"219035_NB",
	"219035_SB",
	"219036_NB",
	"219036_SB",
	"279008_NB",
	"279008_SB",
	"279011_NB",
	"279011_SB",
	"279013",
	"279015_NB",
	"279015_SB",
	"279016_SB",
	"279016_NB"
	]


def training_run(config_file, steps, run, seed):
	# initialize the sumo instance
	run_label = "run_{:0>4d}".format(run)
	traci.start([sumo_binary, "-c", config_file, "-r", "trip_files/sample_{:0>4d}.trips.rou.xml".format(run), "--seed", str(seed)], label=run_label)
	conn = traci.getConnection(run_label)  # get connector to sumo instance

	count_mat = np.zeros((steps, len(DETECTOR_IDS)))
	step = 0

	# run simulation
	while step < steps:
		conn.simulationStep()
		detector_counts = [conn.inductionloop.getLastStepVehicleNumber(det_id) for det_id in DETECTOR_IDS]  # FIXME: call inductionloop from conn, not traci
		count_mat[step] = detector_counts
		step += 1

	conn.close()
	# get counts
	df = pd.DataFrame(data=count_mat, columns=DETECTOR_IDS)
	# collapse individual lane measurements to get edge total at location
	pat = '([0-9]{6})'
	edge_groups = df.groupby(df.columns.str.extract(pat, expand=False), axis=1)

	sim_results = edge_groups.sum().rolling(3600).sum().max()
	sim_results['run'] = str(run)
	return sim_results.squeeze()


# execute in parallel
if __name__ == '__main__':

	p = Pool(6)
	sim_config_file = "training_samples.sumocfg"
	num_runs = 1000
	num_steps = 7200
	seed_vec = np.linspace(start=3, stop=5 * num_runs, num=num_runs, dtype=int)  # use different seed for each run

	results = [p.apply_async(training_run, args=(sim_config_file, num_steps, run, seed_vec[run])) for run in range(num_runs)]

	out = [r.get() for r in results]

	results_frame = pd.DataFrame(data=out)

	print(results_frame)

	results_frame.to_csv('results.csv')
