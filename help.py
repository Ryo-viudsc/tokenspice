#!/usr/bin/env python 

if __name__== '__main__':            

    #set help message
    help = """
Usage: help  

TOOLS: 

  === Help ===
  ./help.py [[this file]]

  === Generate results and plot ===
  ./run_1.py [[Do 1 run. Input conf file. Output rundir w/ csv and dbs.]]
  ./plot_1.py [[Plot results from 1 run. Input csv. Output pngs.]]
  Example flow: see bottom

  === Running tests === 
  python -m unittest [[run all tests]]
  python -m unittest util.test [[run all tests in util.test directory]]
  python -m unittest util.test.ConstantsTest [[run all tests in util.test.ConstantsTest class]]
  python -m unittest util.test.ConstantsTest.testINF [[run one test]]
  -Add "-v" to command line to make all loglevels DEBUG

  === Config files, with params to change === 
  -System parameters: ~/tokenspice.conf
  -Logging: ./logging.conf

  == Example flow ==
  rm -rf outdir_csv; ./run_1.py 10 outdir_csv 1>out.txt 2>&1 &
  tail -f out.txt
  rm -rf outdir_png; ./plot_1.py outdir_csv outdir_png
  eog outdir_png
"""
    print(help)
