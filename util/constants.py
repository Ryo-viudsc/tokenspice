import configparser, os
config = configparser.ConfigParser()
config.read(os.path.expanduser('~/tokenspice.conf'))

SAFETY = config['util'].getboolean('safety')
assert SAFETY is not None

import logging
log = logging.getLogger('constants')

import math

import enforce
if not SAFETY:
    # do nothing, just return the original function
    def noop(f):
        return f
    enforce.runtime_validation = noop

#conveniently set infinity
INF = math.inf
 
#number of seconds in an hour, etc.
S_PER_MIN   = 60
S_PER_HOUR  = S_PER_MIN * 60 
S_PER_DAY   = S_PER_HOUR * 24
S_PER_WEEK  = S_PER_DAY * 7
S_PER_MONTH = S_PER_DAY * 30
S_PER_YEAR  = S_PER_DAY * 365

#
TOTAL_OCEAN_SUPPLY = 1.41e9 
INIT_OCEAN_SUPPLY = 0.49 * TOTAL_OCEAN_SUPPLY
UNMINTED_OCEAN_SUPPLY = TOTAL_OCEAN_SUPPLY - INIT_OCEAN_SUPPLY

OPF_TREASURY_USD = 0e6 #(not the true number)
OPF_TREASURY_OCEAN = 1e6 #(not the true number)
OPF_TREASURY_OCEAN_FOR_OCEAN_DAO = 1e6 #(not the true number)
OPF_TREASURY_OCEAN_FOR_OPF_MGMT = OPF_TREASURY_OCEAN - OPF_TREASURY_OCEAN_FOR_OCEAN_DAO

BDB_TREASURY_USD = 0e6 #(not the true number)
BDB_TREASURY_OCEAN = 1e6  #(not the true number)

#Number of half-lives that bitcoin stops after.
# https://en.bitcoin.it/wiki/Controlled_supply#Projected_Bitcoins_Long_Term
BITCOIN_NUM_HALF_LIVES = 34
