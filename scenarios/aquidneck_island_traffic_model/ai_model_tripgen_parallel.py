import subprocess
from multiprocessing import Pool, Process


# names of od datafiles




def generate_routes(od_name, random_seed, run):
    RANDOM_SEED = str(random_seed + run)
    run_number = str(run)
    trips_cmd = "od2trips -c od_data/%s_trip_config.cfg.xml -o trip_files/%s_run%s.trips.rou.xml --error-log logs/%s_run%s_od2trips_errors.txt --seed %s"  % (od_name, od_name, run_number, od_name, run_number, RANDOM_SEED)
    print('generating trips for %s run %s' % (od_name, run_number))
    subprocess.call(trips_cmd, shell=False)
    # print('generating routes for %s run %s' % (od_name, run_number))
    # routes_cmd = "duarouter -c trip_files/%s_router.cfg.xml --route-files trip_files/%s_run%s.trips.rou.xml -o route_files/%s_run%s.rou.xml --error-log logs/%s_run%s_duarouter_errors.txt" % (od_name, od_name, run_number, od_name, run_number, od_name, run_number)
    # subprocess.call(routes_cmd, shell=False)



# for run in range(0, number_of_runs):
# # for run in range(2,3):
#     run_number = str(run)
#     # calculate routes for the run
#     for name in od_sets:
#         RANDOM_SEED = str(random_seed + i)
#         i += 1



if __name__ == '__main__':
    od_sets = ['hbnwauto15',
                'hbwauto15',
                'nhbauto15',
                'truck15',
                'hbnwauto25',
                'hbwauto25',
                'nhbauto25',
                'truck25',
                ]
    random_seed = 6789
    number_of_runs = 10
    i = 0

    p = Pool(4)

    for od_name in od_sets:
        random_seed += i
        print(od_name)
        # for run in range(0,number_of_runs):
        results = [p.apply_async(generate_routes, args=(od_name, random_seed, run)) for run in range(0, number_of_runs)]
        out = [p.get() for p in results]
        i += 1
