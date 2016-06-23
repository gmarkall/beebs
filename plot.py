#!/usr/bin/env python3

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import OrderedDict

def plot(results, *, show=False, savefile=None):
    bms, counts = zip(*results.items())
    ind = np.arange(len(bms))
    width = 0.8

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, counts, width)
    ax.set_xticks(ind + (width / 2))
    ax.set_xticklabels(bms, rotation=45, ha='right')
    ax.set_xlabel('Benchmark')
    ax.set_ylabel('Cycle count')
    ax.set_title('Cycle count of BEEBS benchmarks on RISC-V')
    if show:
        plt.show()
    if savefile:
        fig.savefig(savefile)

if __name__ == '__main__':
    import sys
    #raw_results  = { '2dfir': 1234, 'cubic': 2543, 'adpcm': 2655, 'aes': 5667 }
    raw_results = {}
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            split = line.split()
            if len(split) > 0: # Ignore blank lines
                bm = split[0].strip()
                cycles = int(split[1])
                raw_results[bm] = cycles
    results = OrderedDict(sorted(raw_results.items(), key=lambda t: t[0]))
    for item in results:
        print(item)
    if results:
        plot(results, show=True, savefile='demo.png')
    else:
        print("No results")
        sys.exit(1)
