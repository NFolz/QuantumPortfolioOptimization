from dwave.system import *
from dimod import *
from itertools import islice
import Finding_effective_weights as few
import time 
from sympy import *
import numpy as np
import random as random
import dwave.inspector

def createVariableList(tick, weights):
    """Create a list of variables combining tickers and weights."""
    variables = []
    for ticker in tick:
        for weight in weights:
            variables += [str(ticker) + "_" + str(weight)]
    return variables

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

def multiply_dict_values(input_dict, factor):
    multiplied_dict = {key: value * factor for key, value in input_dict.items()}
    return multiplied_dict

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

def calculate_final_portfolio(sample_dict):
    """Calculate the final portfolio based on a sample dictionary."""
    final_weights_dict = {}

    for key, value in sample_dict.items():
        if value == 1:
            parts = key.split('_')
            if len(parts) == 2:
                text_before_underscore, float_value_str = parts
                try:
                    float_value = float(float_value_str)
                    # Add the float value to the corresponding entry in the final_weights_dict
                    final_weights_dict[text_before_underscore] = final_weights_dict.get(text_before_underscore, 0.0) + float_value
                except ValueError:
                    print(f"Error converting {float_value_str} to float in key: {key}")
                    # Handle the error (e.g., log it, continue, or take appropriate action)

    return final_weights_dict


def calculate_sum_of_values(result_dict):
    # Initialize a new dictionary to store the sums
    sums_dict = {}

    # Iterate through the key-value pairs in the result dictionary
    for key, value in result_dict['sample'].items():
        # Check if the value is 1
        if value == 1:
            # Extract the number after the underscore in the key
            _, number_str = key.split('_')
            # Convert the number string to a float and add it to the sums_dict
            sums_dict[key] = sums_dict.get(key, 0) + float(number_str)

    return sums_dict

def process_input_dictionary(input_dict):
    result_dict = {}

    for key, value in input_dict.items():
        # Split the key into ticker and value parts
        ticker, val = key.split('_')

        # Check if the value is 1
        if value == 1:
            # Add the value to the ticker in the result dictionary
            result_dict.setdefault(ticker, 0)
            result_dict[ticker] += float(val)

    return result_dict

def print_investment_strategy(result_dict):
    for ticker, value in result_dict.items():
        print(f"Invest {value * 100:.2f}% in {ticker}")

