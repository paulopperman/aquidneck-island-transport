import subprocess
from multiprocessing import Pool
import numpy as np


def generate_trips(run, seed):
	trip_cmd = "od2trips -c sampled_trips.cfg.xml -d od_files/od_sample_{:0>4d}.txt --taz-files ../../tazs/aquidneck_car.taz.xml -o trip_files/sample_{:0>4d}.trips.rou.xml --error-log logs/sample_{:0>4d}_tripgen_log.txt --seed {}".format(run, run, run, seed)
	subprocess.call(trip_cmd, shell=False)


# execute in parallel
if __name__ == '__main__':
	seed = 346

	p = Pool(8)  # set the pool of workers

	num_runs = 1000  # number of runs generated in the experiment design

	seed_vec = np.linspace(start=1, stop=2*num_runs, num=num_runs, dtype=int)  # use different seed for each run

	results = [p.apply_async(generate_trips, args=(i, seed_vec[i])) for i in range(num_runs)]
	out = [p.get() for p in results]

