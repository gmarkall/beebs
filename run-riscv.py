#!/usr/bin/env python3

import os
import subprocess
from all_benchmarks import names
from concurrent.futures import ThreadPoolExecutor, as_completed

WORKDIR = os.path.abspath(os.path.dirname(__file__))

WORKERS = 8

def run(bm, outfile):
    bm_path = os.path.join(WORKDIR, 'src', bm, bm)
    args = [
        './emulator-Top-DefaultConfig',
        '+dramsim',
        '+max-cycles=100000000',
        'pk',
        bm_path
        ]
    return bm, " ".join(args), subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


with open("log_file.txt", "w") as outfile:

    executor = ThreadPoolExecutor(max_workers=WORKERS)
    jobs = { executor.submit(run, bm, outfile): bm for bm in names }
    all_success = True

    results = {}
    done_count = 1

    for worker in as_completed(jobs):
        try:
            bm, args, result = worker.result()
            stdout = result.stdout.decode('utf-8')
            stderr = result.stderr.decode('utf-8')

            print("Finished running %s (%s / %s)" % (bm, done_count, len(names)))
            print("Finished running %s with:\n\n%s\n" % (bm, args), file=outfile)
            print("Output:\n\n%s\n" % stdout, file=outfile)
            print("Errors:\n\n%s\n" % stderr, file=outfile)

            if result.returncode != 0:
                print("Error running %s" % bm, file=outfile)
                print("Err code %s" % result.returncode, file=outfile)
                all_success = False
            else:
                count_lines = [ line for line in stdout.splitlines() if 'Cycle count'  in line ]
                if len(count_lines) != 1:
                    print("Error getting cycle count for %s" % bm, file=outfile)
                else:
                    count = int(count_lines[0].split()[4])
                    results[bm] = count
        except Exception as exc:
            import traceback
            print("Job %s generated an exception: %s" % (worker, exc), file=outfile)
            traceback.print_exc(file=outfile)
            all_success = False

        done_count += 1
        outfile.flush()

    if all_success:
        print("All ran successfully", file=outfile)
        print("All ran successfully")
    else:
        print("Some failures", file=outfile)
        print("Some failures")

with open("results.txt", "w") as outfile:
    for bm, count in results.items():
        print("%s\t%s" % (bm, count))
        print("%s\t%s" % (bm, count), file=outfile)

