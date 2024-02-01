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
granularity_factor = 5 # the degree of granularity that the weightings will incurr
stock_ticker_list = ['AAPL', 'IBM', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'NVDA', 'NFLX', 'V', 'GS']
covariance_dict = {
    ("AAPL", "AAPL"): 1,
    ("AAPL", "GOOGL"): 0.45,
    ("AAPL", "MSFT"): 0.38,
    ("AAPL", "IBM"): 0.38,
    ("AAPL", "AMZN"): 0.32,
    ("AAPL", "TSLA"): 0.28,
    ("AAPL", "NVDA"): 0.21,
    ("AAPL", "NFLX"): 0.25,
    ("AAPL", "V"): 0.35,
    ("AAPL", "GS"): 0.3,

    ("GOOGL", "AAPL"): 0.45,
    ("GOOGL", "GOOGL"): 1,
    ("GOOGL", "MSFT"): 0.26,
    ("GOOGL", "IBM"): 0.26,
    ("GOOGL", "AMZN"): 0.3,
    ("GOOGL", "TSLA"): 0.18,
    ("GOOGL", "NVDA"): 0.15,
    ("GOOGL", "NFLX"): 0.2,
    ("GOOGL", "V"): 0.32,
    ("GOOGL", "GS"): 0.28,

    ("MSFT", "AAPL"): 0.38,
    ("MSFT", "GOOGL"): 0.26,
    ("MSFT", "MSFT"): 1,
    ("MSFT", "IBM"): 0.26,
    ("MSFT", "AMZN"): 0.29,
    ("MSFT", "TSLA"): 0.15,
    ("MSFT", "NVDA"): 0.18,
    ("MSFT", "NFLX"): 0.23,
    ("MSFT", "V"): 0.3,
    ("MSFT", "GS"): 0.25,

    ("IBM", "AAPL"): 0.38,
    ("IBM", "GOOGL"): 0.26,
    ("IBM", "MSFT"): 0.26,
    ("IBM", "IBM"): 1,
    ("IBM", "AMZN"): 0.24,
    ("IBM", "TSLA"): 0.12,
    ("IBM", "NVDA"): 0.15,
    ("IBM", "NFLX"): 0.2,
    ("IBM", "V"): 0.28,
    ("IBM", "GS"): 0.23,

    ("AMZN", "AAPL"): 0.32,
    ("AMZN", "GOOGL"): 0.3,
    ("AMZN", "MSFT"): 0.29,
    ("AMZN", "IBM"): 0.24,
    ("AMZN", "AMZN"): 1,
    ("AMZN", "TSLA"): 0.4,
    ("AMZN", "NVDA"): 0.35,
    ("AMZN", "NFLX"): 0.45,
    ("AMZN", "V"): 0.38,
    ("AMZN", "GS"): 0.42,

    ("TSLA", "AAPL"): 0.28,
    ("TSLA", "GOOGL"): 0.18,
    ("TSLA", "MSFT"): 0.15,
    ("TSLA", "IBM"): 0.12,
    ("TSLA", "AMZN"): 0.4,
    ("TSLA", "TSLA"): 1,
    ("TSLA", "NVDA"): 0.5,
    ("TSLA", "NFLX"): 0.3,
    ("TSLA", "V"): 0.45,
    ("TSLA", "GS"): 0.38,

    ("NVDA", "AAPL"): 0.21,
    ("NVDA", "GOOGL"): 0.15,
    ("NVDA", "MSFT"): 0.18,
    ("NVDA", "IBM"): 0.15,
    ("NVDA", "AMZN"): 0.35,
    ("NVDA", "TSLA"): 0.5,
    ("NVDA", "NVDA"): 1,
    ("NVDA", "NFLX"): 0.4,
    ("NVDA", "V"): 0.48,
    ("NVDA", "GS"): 0.32,

    ("NFLX", "AAPL"): 0.25,
    ("NFLX", "GOOGL"): 0.2,
    ("NFLX", "MSFT"): 0.23,
    ("NFLX", "IBM"): 0.2,
    ("NFLX", "AMZN"): 0.45,
    ("NFLX", "TSLA"): 0.3,
    ("NFLX", "NVDA"): 0.4,
    ("NFLX", "NFLX"): 1,
    ("NFLX", "V"): 0.38,
    ("NFLX", "GS"): 0.42,

    ("V", "AAPL"): 0.35,
    ("V", "GOOGL"): 0.32,
    ("V", "MSFT"): 0.3,
    ("V", "IBM"): 0.28,
    ("V", "AMZN"): 0.38,
    ("V", "TSLA"): 0.45,
    ("V", "NVDA"): 0.48,
    ("V", "NFLX"): 0.38,
    ("V", "V"): 1,
    ("V", "GS"): 0.36,

    ("GS", "AAPL"): 0.3,
    ("GS", "GOOGL"): 0.28,
    ("GS", "MSFT"): 0.25,
    ("GS", "IBM"): 0.23,
    ("GS", "AMZN"): 0.42,
    ("GS", "TSLA"): 0.38,
    ("GS", "NVDA"): 0.32,
    ("GS", "NFLX"): 0.42,
    ("GS", "V"): 0.36,
    ("GS", "GS"): 1,
}

returns_dict = {
    'AAPL': 0.1,
    'IBM': 0.12,
    'GOOGL': 0.15,
    'MSFT': 0.2,
    'AMZN': 0.18,
    'TSLA': 0.25,
    'NVDA': 0.22,
    'NFLX': 0.28,
    'V': 0.32,
    'GS': 0.3,
}
esg_dict = {
    'AAPL': 0.1,
    'IBM': 0.12,
    'GOOGL': 0.15,
    'MSFT': 0.2,
    'AMZN': 0.18,
    'TSLA': 0.25,
    'NVDA': 0.22,
    'NFLX': 0.28,
    'V': 0.32,
    'GS': 0.3,
}
returns_penalty_term = 200 # penalty term for the returns
esg_penalty_term = 1 # penalty term for the esg scores
covariance_penalty_term = 15 # penalty term for the covariance
weightings_penalty_term = 9000 # penalty term for the weightings
quantum_Sampler = EmbeddingComposite(DWaveSampler()) # The quantum solver we are using

def main():
    #1: Creating the weighted dictionary with the weight constraints
    variable_list = ce.createVariableList(stock_ticker_list,few.findWeights(granularity_factor,max_portfolio_weight,min_portfolio_weight))
    print("This is the variable list: ")
    print(variable_list)
    expression = ce.create_squared_expression(variable_list)
    print("This is the expression: ")
    print(expression)
    expanded_expression = ce.square_and_expand_expression(expression)
    weighted_dict = ce.multiply_dict_values(ce.extract_variable_terms(expanded_expression),weightings_penalty_term)
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

    first_datum = next(islice(sampleset.data(fields=['sample', 'energy']), 1), None)
    if first_datum:
        sample_dict = first_datum.get('sample', {})
        print("Result: ")
        print(first_datum)
    
    # Calculate the final weights for the first datum
    
    result = ce.calculate_final_portfolio(sample_dict)

    print(result)

    dwave.inspector.show(sampleset)

main()

