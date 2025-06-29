import subprocess
import os
import csv
import time
import statistics
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from colorama import init, Fore, Back, Style
from benchmark import *
from synthesis import HPLUS_CMD, CMD_OPTS, FNULL

INFERENCE_RESULT = 'inference.tsv'
INFERENCE_CSV = 'inference-stats.tsv'
INFERENCE_GRAPH = 'inference-heatmap.png'
INFERENCE_USER_GRAPH = 'inference-user.png'

class InferenceResult:
    def __init__(self, benchmark, gen_examples, num_examples, num_vars,
                inf_types, correct_rank, prefilter_cnt, postfilter_cnt):
        self.benchmark = benchmark
        self.gen_examples = gen_examples
        self.inf_types = inf_types
        self.rank = correct_rank
        self.num_examples = num_examples
        self.num_vars = num_vars
        self.prefilter_cnt = prefilter_cnt
        self.postfilter_cnt = postfilter_cnt

    def add_example(self, example):
        self.gen_examples.append(example)

    def add_type(self, typ):
        self.inf_types.append(typ)

    def __str__(self):
        return '{benchmark: ' + str(self.benchmark) + \
               ', examples: ' + str(self.gen_examples) + \
               ', inferred types: ' + str(self.inf_types) + \
               ', rank: ' + str(self.rank) + '}'

    def __repr__(self):
        return self.__str__()

class RankEntry:
    def __init__(self, fst_rank, snd_rank, other_rank, no_rank):
        self.fst_rank = fst_rank
        self.snd_rank = snd_rank
        self.other_rank = other_rank
        self.no_rank = no_rank

    def __str__(self):
        return '{rank 1: ' + str(self.fst_rank) + \
                'rank 2: ' + str(self.snd_rank) + \
                'rank 3-10: ' + str(self.other_rank) + \
                'no answer: ' + str(self.no_rank) + '}'

    def __repr__(self):
        return self.__str__()

class TableEntry:
    def __init__(self, num_vars, num_exs, rank, prefilter, postfilter):
        self.num_vars = num_vars
        self.num_exs = num_exs
        self.rank = rank
        self.prefilter_gens = prefilter
        self.postfilter_gens = postfilter

def parse_inference_results(benchmarks, file_path):
    results = []
    with open(file_path, 'r') as f:
        log_reader = csv.DictReader(f, delimiter='\t')
        curr_result = None
        for row in log_reader:
            name = row['bm_name']
            if name == '':
                curr_result.add_example(row['gen_exs'])
                curr_result.add_type(row['inf_typs'])
            else:
                # add the result into the results list
                if curr_result:
                    results.append(curr_result)

                # sanity check
                benchmark = find_benchmark_in_groups(name, benchmarks)
                assert benchmark, \
                    f'Benchmark name {name} does not match that in the log file, please check'
                gen_examples = [row['gen_exs']]
                num_examples = int(row['num_exs'])
                num_vars = int(row['var_counts'])
                inf_typs = [row['inf_typs']]
                rank = int(row['rank']) if row['rank'] != 'NO ANSWER' else 11
                prefilter = int(row['prefilter_counts']) if row['prefilter_counts'] != '' else None
                postfilter = int(row['postfilter_counts']) if row['postfilter_counts'] != '' else None
                curr_result = InferenceResult(benchmark, gen_examples, num_examples, num_vars,
                                              inf_typs, rank, prefilter, postfilter)

    return results

def group_by_counts(inference_results):
    group_result = {}
    for r in inference_results:
        key = (r.num_vars, r.num_examples)
        if key not in group_result:
            group_result[key] = [r]
        else:
            group_result[key].append(r)

    return group_result

def create_table_entry(result_groups):
    # first round: collect the info between experiments
    rank_map = {}
    prefilter_map = {}
    postfilter_map = {}
    for group in result_groups:
        for k, results in group.items():
            # store the aggregated counts
            if k not in rank_map:
                rank_map[k] = []
                prefilter_map[k] = []
                postfilter_map[k] = []

            ranks = list(map(lambda x: x.rank, results))
            rank_map[k] = rank_map[k] + ranks
            prefilters = list(map(lambda x: x.prefilter_cnt, results))
            prefilter_map[k] = prefilter_map[k] + prefilters
            postfilters = list(map(lambda x: x.postfilter_cnt, results))
            postfilter_map[k] = postfilter_map[k] + postfilters

    # second round: update the aggregated info
    result_map = {}
    for k in result_groups[0].keys():
        sorted_ranks = sorted(rank_map[k])
        rank = int(statistics.median(sorted_ranks))
        prefilters = prefilter_map[k]
        prefilter_gens = (min(prefilters), max(prefilters))
        postfilters = postfilter_map[k]
        postfilter_gens = (min(postfilters), max(postfilters))

        # create the entry
        nv, ne = k
        entry = TableEntry(nv, ne, rank, prefilter_gens, postfilter_gens)
        result_map[k] = entry

    return result_map

def format_number(value):
    return '{:,}'.format(value)

def run_inference_each(logfile, suite, benchmark, use_study_data=False):
    command = HPLUS_CMD + ['evaluation', '--out-file', logfile,
                                         '--benchmark', benchmark.name,
                                         '--benchmark-suite', suite,
                                         '--use-study-data={}'.format(use_study_data)]
    # start the timer
    start = time.time()
    try:
        return_code = subprocess.check_call(command, stderr=FNULL)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return_code = -1
    end = time.time()
    # end the timer and print the consumed time
    print('{0:0.2f}'.format(end - start), end=' ')

    if return_code:
        print(Fore.RED + 'FAIL' + Style.RESET_ALL, end='\n')
    else: # Synthesis succeeded: code metrics from the output and record synthesis time
        print(Fore.GREEN + 'OK' + Style.RESET_ALL, end='\n')

def get_rank_details(result_groups):
    rank_map = {}
    for group in result_groups:
        for k, r in group.items():
            ranks = list(map(lambda x: x.rank, r))
            rank_fst = ranks.count(1)
            rank_snd = ranks.count(2)
            rank_no_ans = ranks.count(11)
            rank_other = len(ranks) - rank_fst - rank_snd - rank_no_ans
            rank_per_exp = RankEntry(rank_fst, rank_snd, rank_other, rank_no_ans)

            if k not in rank_map:
                rank_map[k] = []
            rank_map[k].append(rank_per_exp)
    return rank_map

def rank_to_percent(rank_map):
    percent_map = {}
    for k, rs in rank_map.items():
        ranks = None
        for r in rs:
            np_rank = np.array([r.fst_rank, r.snd_rank, r.other_rank, r.no_rank])
            ranks = np_rank if ranks is None else np.vstack((ranks, np_rank))
        percents = ranks / ranks.sum(axis=1)[:, None]
        # percents = ranks / ranks.sum()
        percents = np.mean(percents, axis=0)
        percent_map[k] = percents

    return percent_map

def plot_heatmap(output_dir, results):
    # collect the data into a list
    ranks = get_rank_details(results)
    percent_map = rank_to_percent(ranks)
    data = None
    # iterate var nums from small to large
    for vn in range(0, 5):
        # iterate ex nums from large to small
        for en in range(3, 0, -1):
            k = (vn, en)
            if k in percent_map:
                v = percent_map[k]
            else:
                v = np.zeros(4)
            data = v if data is None else np.vstack((data, v))

    fig, ax = plt.subplots(figsize=(4, 9.25))
    im = ax.imshow(data, cmap='RdPu')
    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel('', rotation=-90, va="bottom")
    # set labels
    ax.set_xticks([0.0, 1.0, 2.0, 3.0])
    ax.set_xticklabels(['rank 1', 'rank 2', 'rank 3-10', 'no answer'])
    ax.set_yticks(np.arange(0, 15))
    ax.set_yticklabels(['3', '2', '1'] * 5)
    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right",
             rotation_mode="anchor")

    # clone a y-axis
    ax2 = ax.twinx()
    ax2.spines['right'].set_position(('axes', -0.2))
    ax2.spines['right'].set_visible(True)
    # set major ticks
    ax2.yaxis.set_major_locator(ticker.FixedLocator([0.1, 0.3, 0.5, 0.7, 0.9]))
    ax2.yaxis.set_major_formatter(ticker.FixedFormatter(['4 type vars',
                                                         '3 type vars',
                                                         '2 type vars',
                                                         '1 type var',
                                                         '0 type var']))
    ax2.tick_params(axis='y', length=2, which='major', direction='out',
                    labelleft=True, labelright=False, labelrotation=90, pad=40)
    for tick in ax2.yaxis.get_major_ticks():
        tick.label1.set_verticalalignment('center')
    # set minor ticks
    ax2.yaxis.set_minor_locator(ticker.FixedLocator([0, 0.2, 0.4, 0.6, 0.8, 1.0]))
    ax2.yaxis.set_minor_formatter(ticker.NullFormatter())
    ax2.tick_params(axis='y', length=6, which='minor')

    ycoords = [0.2, 0.4, 0.6, 0.8]
    for yc in ycoords:
        plt.axhline(y=yc, color='k', linewidth=1)

    fig.tight_layout()
    plt.savefig(os.path.join(output_dir, INFERENCE_GRAPH))

def plot_histogram(output_dir, results):
    values = [0] * 11
    for _, rs in results.items():
        for r in rs:
            idx = r.rank - 1
            values[idx] = values[idx] + 1

    x_labels = list(map(str, range(1, 11))) + ['No Answer']
    x = np.arange(len(x_labels))
    _, ax = plt.subplots()
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)
    ax.bar(x, values)
    plt.savefig(os.path.join(output_dir, INFERENCE_USER_GRAPH))

def format_width(w, s):
    return '%*s' % (w, s)

def run_type_inference(suite, groups, output_dir, use_study_data=False):
    all_results = []
    # start the evaluation, run it five times
    times = 1 if use_study_data else 5
    for i in range(times):
        print('Running type inference iteration {}/{}...'.format(i+1, times))
        print('')
        # clear the result file and create the table header
        logfile = os.path.join(output_dir, str(i) + '-' + INFERENCE_RESULT)
        with open(logfile, 'w') as f:
            print("bm_name\tbm_query\tgen_exs\tinf_typs\tnum_exs\trank\tprefilter_counts\tpostfilter_counts\tvar_counts\targ_counts",
                  file = f, end = '\n')
        # call the inference procedure
        for group in groups.values():
            for b in group.benchmarks:
                print(str(b), end=' ')
                run_inference_each(logfile, suite, b, use_study_data)

        results = parse_inference_results(groups, logfile)
        result_group = group_by_counts(results)
        all_results.append(result_group)
        print('')

    print('Inference completed.')
    print('Processing data for graph plotting...')
    # plot the heatmap
    if use_study_data:
        plot_histogram(output_dir, all_results[0])
    else:
        result_table = create_table_entry(all_results)

        # write results into csv
        with open(os.path.join(output_dir, INFERENCE_CSV), 'w+') as outfile:
            # first line of the header
            outfile.write(format_width(15, '# vars'))
            outfile.write(format_width(15, '# exs'))
            outfile.write(format_width(15, 'median rank'))
            outfile.write(format_width(30, 'pre-filter generalizations '))
            outfile.write(format_width(15, ''))
            outfile.write(format_width(30, 'post-filter generalizations\n'))
            # second line of the header
            outfile.write(format_width(15, ''))
            outfile.write(format_width(15, ''))
            outfile.write(format_width(15, ''))
            outfile.write(format_width(15, 'min'))
            outfile.write(format_width(15, 'max'))
            outfile.write(format_width(15, 'min'))
            outfile.write(format_width(15, 'max\n'))
            # table contents
            entries = sorted(result_table.values(), key = lambda e: (e.num_vars, -e.num_exs))
            for entry in entries:
                outfile.write(format_width(15, entry.num_vars))
                outfile.write(format_width(15, entry.num_exs))
                outfile.write(format_width(15, entry.rank if entry.rank != 11 else '-'))
                outfile.write(format_width(15, format_number(entry.prefilter_gens[0])))
                outfile.write(format_width(15, format_number(entry.prefilter_gens[1])))
                outfile.write(format_width(15, format_number(entry.postfilter_gens[0])))
                outfile.write(format_width(15, format_number(entry.postfilter_gens[1])) + '\n')

        print('Inference details are written into {}'.format(os.path.join(output_dir, INFERENCE_CSV)))

        plot_heatmap(output_dir, all_results)
        print('Heatmap is written into {}'.format(os.path.join(output_dir,
                                                               INFERENCE_GRAPH)))

