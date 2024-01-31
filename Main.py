# File where the final code will run
# importing all external files and modules
from dwave import * 
from dimod import * 
from itertools import *
import time
from sympy import *
import numpy as np
import random as random

# Importing all internal files and modules
import Finding_effective_weights as few # module used to find the weighting system
import Creating_Expression as ce # module used to create the expression, square and expand it, and create the final dictionary with the weights
 # module used to add the returns to the final dict
 # module used to add the ESG scores to the final dict
 # module used to add the co-variances to the final dict

# All necessary inputs are here
max_portfolio_weight = 0 # max weight that any single asset can compose of the portfolio
min_weight = 0  # min weight that any single asset can compose of the portfolio
granularity_factor = 0 # the degree of granularity that the weightings will incurr
stock_list = [] # list of all the stocks we will be computing on
covariance_dict = {} # dict with all the covariances between stocks
returns_dict = {} # dict with the expected returns for each stock
esg_dict = {} # dict with the ESG scores for each stock

