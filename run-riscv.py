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

    for worker in as_completed(jobs):
        try:
            bm, args, result = worker.result()

            print("Finished running %s with:\n\n%s\n" % (bm, args), file=outfile)
            print("Output:\n\n%s\n" % result.stdout.decode('utf-8'), file=outfile)
            print("Errors:\n\n%s\n" % result.stderr.decode('utf-8'), file=outfile)

            if result.returncode != 0:
                print("Error running %s" % bm, file=outfile)
                print("Err code %s" % result.returncode, file=outfile)
                all_success = False
        except Exception as exc:
            import traceback
            print("Job %s generated an exception: %s" % (worker, exc), file=outfile)
            traceback.print_exc(file=outfile)
            all_success = False

    if all_success:
        print("All ran successfully", file=outfile)
    else:
        print("Some failures", file=outfile)
