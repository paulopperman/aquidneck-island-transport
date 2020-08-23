import subprocess

# names of od datafiles
od_sets = ['hbnwauto15',
            'hbwauto15',
            'nhbauto15',
            'truck15',
            'hbnwauto25',
            'hbwauto25',
            'nhbauto25',
            'truck25'
            ]

random_seed = 5678
number_of_runs = 10
i = 0

for run in range(0, number_of_runs):
# for run in range(2,3):
    run_number = str(run)
    # calculate routes for the run
    for name in od_sets:
        RANDOM_SEED = str(random_seed + i)
        trips_cmd = "od2trips -c od_data/%s_trip_config.cfg.xml -o trip_files/%s_run%s.trips.rou.xml --error-log logs/%s_run%s_od2trips_errors.txt --seed %s"  % (name, name, run_number, name, run_number, RANDOM_SEED)
        #if (name == 'hbnwauto15') or (name == 'nhbauto15'):
        subprocess.call(trips_cmd, shell=True)
        routes_cmd = "duarouter -c trip_files/%s_router.cfg.xml --route-files trip_files/%s_run%s.trips.rou.xml -o route_files/%s_run%s.rou.xml --error-log logs/%s_run%s_duarouter_errors.txt" % (name, name, run_number, name, run_number, name, run_number)
        #if (name == 'hbnwauto15') or (name == 'nhbauto15'):
        subprocess.call(routes_cmd, shell=True)
        i += 1
