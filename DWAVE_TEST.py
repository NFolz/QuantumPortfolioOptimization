from dwave.system import *
from dimod import *
from itertools import islice
import Finding_effective_weights as few
import time 
from sympy import *
import numpy as np
import random as random
from returnsFormater import updateFinalLinearDic
from dwaveDataFormater import stock_values
from CovarianceFunctions import covariances, addCovariance

# Initialize classical and quantum samplers
classical_Sampler = ExactSolver()
quantum_Sampler = EmbeddingComposite(DWaveSampler())

# Module that will be used to calculate the weights
# Taking all variables (Ticker, weight), adding them all together, subtracting 1 from it, and squaring the entire term, then finding the relationship between each as the output
# Final output should respect the final dict format: {('IBM_0.125','MSFT_0.00625'):3,...}

def createVariableList(tick, weights):
    """Create a list of variables combining tickers and weights."""
    variables = []
    for ticker in tick:
        for weight in weights:
            variables += [str(ticker) + "_" + str(weight)]
    return variables

# Define a list of tickers
tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'FB', 'NFLX', 'NVDA', 'V', 'PYPL']

# Create a list of terms combining tickers and weights
terms_list = createVariableList(tickers, few.findWeights(5,0.2,0))

def create_squared_expression(terms):
    """Create a squared expression based on the input terms."""
    # Define the variable
    x = symbols('x')

    # Initialize an empty expression
    expression = 0

    # Loop through each term in the list
    for term in terms:
        # Split the term into ticker and coefficient
        ticker, coefficient_str = term.split('_')
        
        # Convert coefficient to a floating-point number
        coefficient = float(coefficient_str)
        
        # Create the symbolic variable for the ticker
        ticker_symbol = symbols(term)
        
        # Add the term to the expression
        expression += (coefficient * ticker_symbol)

    # Expand the expression to handle parentheses and simplifications
    expanded_expr = expand(expression)

    # Subtract 1 from the final expression
    final_expression = expanded_expr - 1

    return final_expression

def square_and_expand_expression(expression):
    """Square and expand the given expression."""
    # Take the square of the entire expression
    squared_expression = expression**2

    # Expand the squared expression to handle parentheses and simplifications
    expanded_squared_expr = expand(squared_expression)

    return expanded_squared_expr

def extract_variable_terms(expression):
    """Extract terms with two variables and their coefficients."""
    terms_dict = expression.as_coefficients_dict()
    variable_terms = {}

    for term, coeff in terms_dict.items():
        variables = [symbol.name for symbol in term.free_symbols]
        
        if len(variables) == 1:
            variable_terms[(variables[0], variables[0])] = coeff
        elif len(variables) == 2:
            variable_terms[tuple(variables)] = coeff

    return variable_terms

def calculate_final_weight(datum):
    """Calculate the final weight based on the sample datum."""
    final_weight = 0.0

    # Assuming datum is a Sample object and has a 'sample' attribute
    data_dict = datum.sample

    for key, value in data_dict.items():
        if value == 1:
            # Extract the float value after the underscore
            _, float_value_str = key.split('_')
            float_value = float(float_value_str)

            # Add the float value to the final weight
            final_weight += float_value

    return final_weight

def subtract_0_1_for_matching_tuples(input_dict):
    result_dict = {}
    
    for key, value in input_dict.items():
        stock_symbol_1, stock_symbol_2 = key
        if stock_symbol_1 == stock_symbol_2:
            result_dict[key] = value - 0.1
        else:
            result_dict[key] = value
    
    return result_dict

def subtract_0_1_and_10000_for_msft(input_dict):
    result_dict = {}
    
    for key, value in input_dict.items():
        stock_symbol_1, stock_symbol_2 = key
        if stock_symbol_1 == stock_symbol_2:
            if 'MSFT' in stock_symbol_1 and 'MSFT' in stock_symbol_2:
                result_dict[key] = value - 10
            else:
                result_dict[key] = value - 0.1
        else:
            result_dict[key] = value
    
    return result_dict

def multiply_dict_values(input_dict, factor):
    multiplied_dict = {key: value * factor for key, value in input_dict.items()}
    return multiplied_dict

def main():
    # print(terms_list)
    expression = create_squared_expression(terms_list)
    print("This is the expression to be squared: " + str(expression))
    expanded_expression = square_and_expand_expression(expression)
    print("This is the final expanded expression after squaring: " + str(expanded_expression))

    two_variable_terms = multiply_dict_values(extract_variable_terms(expanded_expression),3000)
    # updateFinalLinearDic(two_variable_terms,stock_values)
    # addCovariance(two_variable_terms,covariances)

    # Printing the results of the strictly weighted dictionary
    # for term, coeff in two_variable_terms.items():
    #     print(f"Term: {term}, Coefficient: {coeff}")
    # print("The weightings dictionary: ")
    # print(two_variable_terms)

    # final_dict = subtract_0_1_and_10000_for_msft(subtract_0_1_for_matching_tuples(two_variable_terms))



    # Printing the results of the weight + arbitrary negative values dictionary
    # for term, coeff in final_dict.items():
    #     print(f"Term: {term}, Coefficient: {coeff}")
    # print("The complex dictionary: ")
    # print(final_dict)

    Q = two_variable_terms

    # classical_start_time = time.time()

    try:
        sampleset = classical_Sampler.sample_qubo(Q, num_reads=1000)
    except Exception as e:
        print(f"An error occurred: {e}")
        sampleset = None  # Set sampleset to None to avoid issues later

    # classical_end_time = time.time()

    # classical_time_difference = classical_end_time - classical_start_time

    # if sampleset:
    #     print("The classical solving time was: " + str(classical_time_difference) + " seconds")

    quantum_start_time = time.time()
    sampleset = quantum_Sampler.sample_qubo(Q, num_reads=1000, chain_strength = 150)
    quantum_end_time = time.time()
    quantum_time_difference = quantum_end_time - quantum_start_time
    print("The quantum solving time was: " + str(quantum_time_difference) + " seconds")
    
    for datum in islice(sampleset.data(fields=['sample', 'energy']), 5):
        print("Result: ")
        print(datum)
        print("The final weighting of this portfolio would be: ")
        print(calculate_final_weight(datum))

    dwave.inspector.show(sampleset)
main()