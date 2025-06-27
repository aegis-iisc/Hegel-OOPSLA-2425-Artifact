

import sys
from subprocess import TimeoutExpired, run
from subprocess import call
import os, os.path
import csv
import resource
import shlex

prudent       = './prudent.native'
TIMEOUT      = 120                            # Timeout in secs
TEST_DIR     = './prudent_tests/'   # Root directory for the tests   
SYNQUID_TEST_DIR = './synquid/test/' # Root directory for synquid tests
VARIANTS     = ['hegel']#, 'prudent-s', 'prudent-p','prudent-all']    # Configurations
RESULTS      = 'full-stdout.txt'                                      # Output file with synthesis results
TIMERESULTS  = 'full-timings.txt'
FINALRESULTS = 'full-results.txt'

synquid = 'synquid/.stack-work/install/x86_64-linux/829fd6d2eaf2caa5835af398ac756f3b93cc7aaab38945b516f36c6eabb34467/7.10.3/bin/synquid'
hoogle = '/home/ashish/work/purdue/code/git/propsynth_safe/propsynth/hoogle_plus/.stack-work/install/x86_64-linux-custom-yields/7c9f6ae890d280d8c9360ded15d6d920e3b79a48508d2aaa1fae4f6bf29fd09e/8.4.4/bin/hplus'
synquid_loc = 'synquid/.stack-work/install/x86_64-linux/829fd6d2eaf2caa5835af398ac756f3b93cc7aaab38945b516f36c6eabb34467/7.10.3/bin'
hoogle_loc = '/home/ashish/work/purdue/code/git/propsynth_safe/propsynth/hoogle_plus/.stack-work/install/x86_64-linux-custom-yields/7c9f6ae890d280d8c9360ded15d6d920e3b79a48508d2aaa1fae4f6bf29fd09e/8.4.4/bin'

HOOGLE_ROOT = '/home/ashish/work/purdue/code/git/propsynth_safe/propsynth/hoogle_plus'

class Benchmark:
  def __init__(self, name, description):
    self.name = name                # Test file name
    self.description = description  # Label of the benchmark in Fig 9

  def str(self):
    return self.name + ': ' + self.description

class BenchmarkGroup:
  def __init__(self, name, benchmarks):
    self.name = name              # Id
    self.benchmarks = benchmarks  # List of benchmarks in this group
#TODO:: Updtae the benchmarks
ALL_BENCHMARKS = [
  BenchmarkGroup("Hegel",  [
     #RQ2 
     Benchmark('hegel/Cobalt+/NLRRemove', 'NLR Remove'),
     Benchmark('hegel/Cobalt+/FWInvertDel', 'FW Invert Del'),
     Benchmark('hegel/Cobalt+/FWInsert', 'FW Insert'),
     Benchmark('hegel/Cobalt+/FWInvert', 'FW Invert'),
     Benchmark('hegel/Cobalt+/NLInsert', 'NL Insert'),
     Benchmark('hegel/Cobalt+/FWMkCentral', 'FW Mk Central'),
     Benchmark('hegel/Cobalt+/NLInv', 'NL Inv'),
     Benchmark('hegel/Cobalt+/NLRemove', 'NL Remove'),
     Benchmark('hegel/Cobalt+/FWInsCons', 'FW Ins Cons'),
      #RQ1 
    Benchmark('hegel/Hoogle+/revAppend', 'Rev Append'),
    Benchmark('hegel/Hoogle+/nthIcr', 'Nth Incr'),
    Benchmark('hegel/Hoogle+/applyList', 'Apply List'),
    Benchmark('hegel/Hoogle+/nth', 'Nth'),
    Benchmark('hegel/Hoogle+/map', 'Map'),
    Benchmark('hegel/Hoogle+/applyNInv', 'Apply N Inv'),
    Benchmark('hegel/Hoogle+/mapDouble', 'Map Double'),
    Benchmark('hegel/Hoogle+/applyNAdd', 'Apply N Add'),
    Benchmark('hegel/Hoogle+/containsEdge', 'Contains Edge'),
    Benchmark('hegel/Hoogle+/splitAt', 'Split At'),
    Benchmark('hegel/Hoogle+/splitStr', 'Split Str'),
    Benchmark('hegel/Hoogle+/revZip', 'Rev Zip'),
     Benchmark('hegel/Hoogle+/appendN', 'Append N'),
     Benchmark('hegel/Hoogle+/lookUpRange', 'Look Up Range'),
   
   ]),    
]
# TODO Add benchmarks 
Synquid_BENCHMARKS = [
  BenchmarkGroup("synquid+",  [
    Benchmark('hegel/nth', 'Nth incr'),
    Benchmark('hegel/u_test1', 'Test1'),
    Benchmark('hegel/u_test2', 'Test2'),
    Benchmark('hegel/u_test3', 'Test3'),
   ]),    
]

Hplus_BENCHMARKS = [
  BenchmarkGroup("hplus",  [
  Benchmark('hegel/Hoogle+/json/nth', 'Nth incr'),
  Benchmark('hegel/Hoogle+/json/u_test1', 'Test1'),
  Benchmark('hegel/Hoogle+/json/u_test2', 'Test2'),
  Benchmark('hegel/Hoogle+/json/u_test3', 'Test3'),
    ]),    
]


class SynthesisResultRQ2:
    def __init__(self, tool, name, time, spec_size, code_size, branches):
        self.name = name
        self.tool = tool
        self.time = time        
        self.spec_size = spec_size
        self.code_size = code_size
        self.branches = branches
    
    def __str__(self):
        return self.name + ', ' + self.tool + ', ' \
               '{0:0.2f}'.format(self.time) + ', ' + \
               str(self.code_size) + ', ' + str(self.spec_size) + ', ' + str(self.branches)


# Run a single benchmark
def run_benchmark_variants(file, variant):
  '''Run single benchmark'''
  cpu_time = 0
  with open(RESULTS, "a") as outfile:
    print ('Running Varinat '+variant, file)
    if variant == 'hegel':
        usage_start = resource.getrusage(resource.RUSAGE_CHILDREN)
        try:
            run(['time', prudent,  '-bi', '-cdcl', '-k', '3', file], timeout =TIMEOUT,  stdout=outfile)
            usage_end = resource.getrusage(resource.RUSAGE_CHILDREN)    
            cpu_time = usage_end.ru_utime - usage_start.ru_utime    
        except TimeoutExpired:
            cpu_time = 1000        
        
        
    elif variant == 'hegel-s':
        usage_start = resource.getrusage(resource.RUSAGE_CHILDREN)
        try:
            run(['time', prudent, '-cdcl', file], timeout =TIMEOUT,  stdout=outfile)
            usage_end = resource.getrusage(resource.RUSAGE_CHILDREN)    
            cpu_time = usage_end.ru_utime - usage_start.ru_utime    
        except TimeoutExpired:
            cpu_time = 1000        
        
    elif variant == 'hegel-p':
        
        usage_start = resource.getrusage(resource.RUSAGE_CHILDREN)
        try:
            run(['time', prudent, '-bi', file], timeout =TIMEOUT,  stdout=outfile)
            usage_end = resource.getrusage(resource.RUSAGE_CHILDREN)    
            cpu_time = usage_end.ru_utime - usage_start.ru_utime    
        except TimeoutExpired:
            cpu_time = 1000        
        
     
    elif variant == 'hegel-a':
        usage_start = resource.getrusage(resource.RUSAGE_CHILDREN)
        try:
            run(['time', prudent, file], timeout =TIMEOUT,  stdout=outfile)
            usage_end = resource.getrusage(resource.RUSAGE_CHILDREN)    
            cpu_time = usage_end.ru_utime - usage_start.ru_utime    
        except TimeoutExpired:
            cpu_time = 1000        
    
    else:
        usage_start = resource.getrusage(resource.RUSAGE_CHILDREN)
        try:
            run(['time', prudent, '-bi', '-cdcl', '-k', '3', file], timeout =TIMEOUT,  stdout=outfile)
            usage_end = resource.getrusage(resource.RUSAGE_CHILDREN)    
            cpu_time = usage_end.ru_utime - usage_start.ru_utime    
        except TimeoutExpired:
            cpu_time = 1000        
       
    with open(TIMERESULTS, 'a') as f:
        f.write("\n "+file+"_"+variant+" : "+str(cpu_time))
        f.close ()    
  return cpu_time 
    ## create a csv file for each category with [name, tim1cob, timefw, timebw, timenocdcl, size]
    ## read the csv and build the graph.
    #read_csv()


def run_benchmark_hegel(file):
  '''Run single benchmark'''
  cpu_time = 0
  with open(RESULTS, "a") as outfile:
    print ('Running Hegel', file)
    usage_start = resource.getrusage(resource.RUSAGE_CHILDREN)
    try:
        run(['time', prudent,  '-bi', '-cdcl', '-k', '2', file], timeout =TIMEOUT,  stdout=outfile)
        usage_end = resource.getrusage(resource.RUSAGE_CHILDREN)    
        cpu_time = usage_end.ru_utime - usage_start.ru_utime    
    except TimeoutExpired:
        cpu_time = 1000        
    with open(TIMERESULTS, 'a') as f:
        f.write("\n "+file+"_Hegel : "+str(cpu_time))
        f.close ()    
  return cpu_time 
    

def run_benchmark_synquid(file):
  '''Run single benchmark using Synquid'''
  
  cpu_time = 0
  with open(RESULTS, "a") as outfile:
    print ('Running Synquid on', file)
    usage_start = resource.getrusage(resource.RUSAGE_CHILDREN)
    try:
        run(['time', 'stack',  'exec',  '--', 'synquid', file], timeout =TIMEOUT,  stdout=outfile)
        usage_end = resource.getrusage(resource.RUSAGE_CHILDREN)    
        cpu_time = usage_end.ru_utime - usage_start.ru_utime    
    except TimeoutExpired:
        cpu_time = 1000        
    
    with open(TIMERESULTS, 'a') as f:
        f.write("\n "+file+"_Synquid : "+str(cpu_time))
        f.close ()    
    
  return cpu_time 

# How do we run the Hoogle+ tool
def run_benchmark_hoogle(json_file):
  '''Run single benchmark using Hoogle'''
  cpu_time = 0
  # Read the JSON content
  with open(json_file, 'r') as f:
    json_data = f.read()

  with open(RESULTS, "a") as outfile:
    print ('Running HPlus on', json_file)
    usage_start = resource.getrusage(resource.RUSAGE_CHILDREN)
    try:
        
        cmd =   ['stack', 'exec', '--', 'hplus', f'--disable-filter=False', f'--json={json_data}']
        
        
        
        print("Running command:")
        print(' '.join(shlex.quote(arg) for arg in cmd))
        
        run(
            cmd,
            cwd = HOOGLE_ROOT,
            text=True,
            timeout=TIMEOUT,  # You can set a timeout if needed
            #stdout=outfile
        )
        usage_end = resource.getrusage(resource.RUSAGE_CHILDREN)    
        cpu_time = usage_end.ru_utime - usage_start.ru_utime    
    except TimeoutExpired:
        cpu_time = 1000        
    
    with open(TIMERESULTS, 'a') as f:
        f.write("\n "+json_file+"_Hooogle+ : "+str(cpu_time))
        f.close ()    
    
  return cpu_time 


def test_hegel():
  '''Test all enabled configurations of each benchmark'''
  csvresults = dict()
  for group in groups:
    for b in group.benchmarks:
      test = TEST_DIR + b.name
      testFileName = test + '.spec'
      #hardcoded for test
      codeSize = 4
      specSize = 3
      branches = 0
      row = dict()
      if not os.path.isfile(testFileName):
        print ("Test file not found:", testFileName)
      else:
        # run_benchmark(testFileName, 'none') # Run default configuration
        with open(TIMERESULTS, 'a') as f:
            f.write("\n ********************************")
            f.close ()    
        row['hegel'] = run_benchmark_hegel(testFileName) # Run variant
        if not (test in csvresults):
          csvresults[test] = SynthesisResultRQ2(test, 'Hegel', row['hegel'], codeSize, specSize, branches)  

  return csvresults         
       


def test_synquid():
  '''Test all enabled configurations of each benchmark'''
  csvresults = dict()
  for test in synquid_test:
    for b in test.benchmarks:
      test = SYNQUID_TEST_DIR + b.name
      testFileName = test + '.sq'
      codeSize = 4
      specSize = 3
      branches = 0
      
      row = dict()
      if not os.path.isfile(testFileName):
        print ("Test file not found:", testFileName)
      else:
        # run_benchmark(testFileName, 'none') # Run default configuration
        with open(TIMERESULTS, 'a') as f:
            f.write("\n ********************************")
            f.close ()    
        row['synquid'] = run_benchmark_synquid(testFileName) # Run variant
        if not (test in csvresults):
           csvresults[test] = SynthesisResultRQ2(test, 'Synuid', row['synquid'], codeSize, specSize, branches)  
  print(csvresults)
  return csvresults         
              
    
def test_hoogle():
  '''Test HooglePlsueach benchmark'''
  csvresults = dict()
  for test in hoogle_test:
    for b in test.benchmarks:
      test = TEST_DIR + b.name
      testFileName = test + '.json'
      codeSize = 4
      specSize = 3
      branches = 0
      
      row = dict()
      if not os.path.isfile(testFileName):
        print ("Test file not found:", testFileName)
      else:
        # run_benchmark(testFileName, 'none') # Run default configuration
        with open(TIMERESULTS, 'a') as f:
            f.write("\n ********************************")
            f.close ()    
        row['hoogle'] = run_benchmark_hoogle(testFileName) # Run variant
        if not (test in csvresults):
           csvresults[test] = SynthesisResultRQ2(test, 'Hoogle', row['hoogle'], codeSize, specSize, branches)  
  print(csvresults)
  return csvresults         
        
          
if __name__ == '__main__':
  
  
  # Add Syqnuid and Hoogle PATH to the $PATh
  os.environ['PATH'] = synquid_loc + os.pathsep + os.environ['PATH']
  os.environ['PATH'] = hoogle_loc + os.pathsep + os.environ['PATH']

  
  if os.path.isfile(RESULTS):        
    os.remove(RESULTS)
    
  variants = VARIANTS
  groups = ALL_BENCHMARKS
  synquid_test = Synquid_BENCHMARKS
  hoogle_test = Hplus_BENCHMARKS
  csvres = dict()
  csvres = csvres | test_hegel()
  csvres = csvres | test_synquid()
  csvres = csvres | test_hoogle ()
  with open(FINALRESULTS, 'a') as f:
    for row in csvres:
      f.write (str(csvres[row]))   
      f.write ('\n')
    f.close ()    

