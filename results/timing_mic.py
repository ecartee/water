import os
import time

n= range(360,4000,360)
procs= [1, 4, 9, 16, 25, 36, 64, 81, 100, 144, 225]
rounds= [1]

indx = 0

for np in procs:
  for nr in rounds:
    for ni in n:
      fname = "{}.pbs".format(indx)
      out = open(fname,'w')
      s = '''#!/bin/sh -l
#PBS -l nodes=1:ppn=24
#PBS -l walltime=0:60:00
#PBS -N lshallow
#PBS -j oe
module load cs5220
cd $PBS_O_WORKDIR
'''
      out.write(s)

      line = "./../lshallow ../tests.lua dam {} {} {} 1\n".format(ni, np, nr)
      out.write(line)
      indx = indx + 1
      out.close()
      os.system("qsub {}".format(fname))
