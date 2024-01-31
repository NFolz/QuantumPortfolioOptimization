# File where the final code will run
# importing all external files and modules
from dwave import * 
from dwave.system import *
from dimod import * 
from itertools import islice
from itertools import *
import time
from sympy import *
import numpy as np
import random as random

# Importing all internal files and modules
import Finding_effective_weights as few # module used to find the weighting system
import Creating_Expression as ce # module used to create the expression, square and expand it, and create the final dictionary with the weights
import returnsFormater as rf # module used to add the returns to the final dict
import ESGScores as esgs # module used to add the ESG scores to the final dict
import CovarianceFunctions as cv  # module used to add the co-variances to the final dict

# All necessary inputs are here
max_portfolio_weight = 0.2 # max weight that any single asset can compose of the portfolio
min_portfolio_weight = 0  # min weight that any single asset can compose of the portfolio
granularity_factor = 6 # the degree of granularity that the weightings will incurr
stock_list = ['AAPL','IBM','GOOGL','MSFT'] # list of all the stocks we will be computing on
covariance_dict = {("AAPL", "AAPL"): 1,
    ("AAPL", "GOOGL"): 0.45,
    ("AAPL", "MSFT"): 0.38,
    ("AAPL", "IBM"): 0.38,  # Include only the relevant entry for IBM

    ("GOOGL", "AAPL"): 0.45,
    ("GOOGL", "GOOGL"): 1,
    ("GOOGL", "MSFT"): 0.26,
    ("GOOGL", "IBM"): 0.26,  # Include only the relevant entry for IBM

    # ... Repeat the structure for other stocks
    ("IBM", "AAPL"): 0.38,
    ("IBM", "GOOGL"): 0.26,
    ("IBM", "MSFT"): 0.26,
    ("IBM", "IBM"): 1 } # Include the self-covariance for IBM} # dict with all the covariances between stocks
returns_dict = {'IBM':0.12,'AAPL':0.1,'GOOGL':0.15,'MSFT':0.2} # dict with the expected returns for each stock
esg_dict = {'IBM':0.12,'AAPL':0.1,'GOOGL':0.15,'MSFT':0.2} # dict with the ESG scores for each stock
returns_penalty_term = 20 # penalty term for the returns
esg_penalty_term = 1 # penalty term for the esg scores
covariance_penalty_term = 5 # penalty term for the covariance
weightings_penalty_term = 100 # penalty term for the weightings
quantum_Sampler = EmbeddingComposite(DWaveSampler()) # The quantum solver we are using

def main():
    #1: Creating the weighted dictionary with the weight constraints
    weighted_dict = ce.multiply_dict_values(ce.extract_variable_terms(ce.square_and_expand_expression(ce.create_squared_expression(ce.createVariableList(stock_list,few.findWeights(granularity_factor,max_portfolio_weight,min_portfolio_weight))))),weightings_penalty_term)
    print("This is the weighted dictionary, which includes all variables: ")
    print(weighted_dict)
    final_dict = weighted_dict

    #2: Adding the returns to the variables
    updated_returns = rf.updateReturns(returns_dict,returns_penalty_term) # first, add the penalty term
    rf.updateFinalLinearDic(final_dict,updated_returns) # next, add the returns to the final dict

    #3: Adding the ESG Scores to the variables
    updated_esg = esgs.updateESG(esg_dict,esg_penalty_term)
    esgs.updateFinalLinearDic(final_dict,updated_esg)

    #4: Adding the Covariance to the variables
    cv.addCovariance(final_dict,ce.multiply_dict_values(covariance_dict,covariance_penalty_term))

    #5: Run it on a quantum computer
    sampleset = quantum_Sampler.sample_qubo(final_dict, num_reads = 1000, chain_strength = 150)

    for datum in islice(sampleset.data(fields=['sample', 'energy']), 5):
        print("Result: ")
        print(datum)
        print("The final weighting of this portfolio would be: ")
        print(ce.calculate_final_weight(datum))

    dwave.inspector.show(sampleset)

main()

