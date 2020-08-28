"""
AITM Model Route Generator - Parallel
This script generates the necessary intermediate files and final calibrated routes for the ATIM baseline weekday demand model.

The script may flag warnings that valid routes are not available.  This is expected behavior resulting from the application
of the RISM macroscopic demand model to the microscopic network.  These missing routes do not affect the simulation behavior,
and are corrected for in the calibration step.

This script is capable of running processes in parallel to speed execution.  The number of parallel processes can be set
by the number of workers in the pool p.
"""

import subprocess
from multiprocessing import Pool, Process

import os

os.environ.setdefault('PYTHONPATH',"C:\Anaconda3\envs\gis\python.exe")


def generate_trips(od_name, random_seed, run):
    RANDOM_SEED = str(random_seed + run)
    run_number = str(run)

    # create edge-to-edge trips in the network corresponding to the OD matrix
    trips_cmd = "od2trips -c od_data/%s_trip_config.cfg.xml -o trip_files/%s_run%s.trips.rou.xml --error-log logs/%s_run%s_od2trips_errors.txt --seed %s"  % (od_name, od_name, run_number, od_name, run_number, RANDOM_SEED)
    print('generating trips for %s run %s' % (od_name, run_number))
    # subprocess.call(trips_cmd, shell=False)

def generate_routes(run_number):
    # create routes in the network for each trip
    print('generating routes for run %s' % run_number)
    routes_cmd = "duarouter -c trip_files/ai15_router.cfg.xml  -o route_files/ai15_run%s.rou.xml --vtype-output route_files/ai15_run%s.vtypes.xml --error-log logs/ai15_run%s_duarouter_errors.txt" % (run_number, run_number, run_number)
    # subprocess.call(routes_cmd, shell=False)

    # calibrate trips in the network to match real world traffic counts
    print('calibrating routes for run %s' % run_number)
    # TODO: improve efficiency of calibration
    calibration_cmd = "python ../../tools/modifiedRouteSampler.py -r ./route_files/ai15_run%s.rou.xml --edgedata-files ./calibration/weekday_survey_2019.xml --optimize 20 --optimize-input -a 'type=\"nhbCar\"' --write-route-ids --mismatch-output ./logs/ai15_run%s_calibration_logs.txt -o ./route_files/ai15_run%s_weekday_survey_calibrated.rou.xml" % (run_number, run_number,  run_number)
    subprocess.call(calibration_cmd, shell=False)


if __name__ == '__main__':
    od_sets = ['hbnwauto15',
                'hbwauto15',
                'nhbauto15',
                'truck15',
                # 'hbnwauto25',  # do not include RISM25 demand since RISM15 is used for base calibration
                # 'hbwauto25',
                # 'nhbauto25',
                # 'truck25',
                ]
    random_seed = 6789
    number_of_runs = 10
    i = 0

    p = Pool(4)

    for od_name in od_sets:
        random_seed += i
        print(od_name)

        results = [p.apply_async(generate_trips, args=(od_name, random_seed, run)) for run in range(0, number_of_runs)]
        out = [p.get() for p in results]
        i += 1

    results = [p.apply_async(generate_routes, args=(run,)) for run in range(0, number_of_runs)]
    out = [p.get() for p in results]
