from sympy import *

import numpy
import pandas as pd
import Finding_effective_weights as few

# Creating containers for the data
quantumResults = [] # Resulting bit string from the quantum output
finalPortfolio = [] # Final data set of stocks and portfolio weights to be sent to backend
weightings = [] # Different weightings for each variable
stock_tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN'] # All of the tickers we are using (imported from backend, in order of variables)



def createVariableList(tick,weights): # creating the variables that return as bits  
    variables = []
    for ticker in tick:
        for weight in weights:
            variables+=[str(ticker)+"_"+str(weight)]
    return variables



from sympy import *

def create_squared_expression(terms):
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
    # Take the square of the entire expression
    squared_expression = expression**2

    # Expand the squared expression to handle parentheses and simplifications
    expanded_squared_expr = expand(squared_expression)

    return expanded_squared_expr

    
    # Extracting terms with two variables and their coefficients
def extract_variable_terms(expression):
    terms_dict = expression.as_coefficients_dict()
    variable_terms = {}

    for term, coeff in terms_dict.items():
        variables = [symbol.name for symbol in term.free_symbols]
        
        if len(variables) == 1:
            variable_terms[(variables[0], variables[0])] = coeff
        elif len(variables) == 2:
            variable_terms[tuple(variables)] = coeff

    return variable_terms

# Finding effective weights

import pandas as pd
import numpy as np

# Variables
maxPortfolioWeight = 0.4 # maximum % of portfolio that one single asset can occupy
minPortfolioWeight = 0 # minimum % of portfolio that one single asset can occupy
granularityFactor = 5 # granularity of the weightings, higher the more computationally intensive

def findPK(granFactor, maxPWeight, minPWeight): # Function to be called inside the findWeights one to adjust the PK
    basePK = (1/(2**granFactor))
    print("the base PK is "+ str(basePK))

    effectivePK = ((maxPWeight-minPWeight)*basePK)
    print("the effective PK is "+ str(effectivePK))

    return effectivePK

def findWeights(): # fuction that will find the weights of the assets
    PK = findPK(granularityFactor,maxPortfolioWeight,minPortfolioWeight) # Calling function above using variables defined at the top
    weightList = []
    for i in range(granularityFactor): #iterating the same number of times as the granularity
        weight = (PK * (2**(i))) # finding the weight for that specific term
        weightList.append(weight) # Add the weight to the list
        print("List "+(str(i+1)) + ":" + str(weightList))
    print("The maximum potential weighting of this asset in our portfolio is "+ str((sum(weightList)))+ ". This should be as close to "+str(maxPortfolioWeight)+" as possible.")
    return weightList # return the final list


def square_and_expand_expression(expression):
    # Take the square of the entire expression
    squared_expression = expression**2

    # Expand the squared expression to handle parentheses and simplifications
    expanded_squared_expr = expand(squared_expression)

    # Initialize a list to store squared terms
    squared_terms = []

    # Iterate through the terms in the expanded squared expression
    simplified_expr = 0
    for term in expanded_squared_expr.as_ordered_terms():
        # Check if the term's string representation contains '**2'
        if '**2' in str(term):
            # Convert the term to a string, replace '**2', and convert back to a symbolic expression
            term_str = str(term).replace('**2', '')
            term = sympify(term_str)
            squared_terms.append(term)
        else:
            simplified_expr += term

    print("The modified expanded squared expression is: ")
    print(simplified_expr)

    print("Squared terms with '**2' removed: ")
    print(squared_terms)

    # Add the modified squared terms back to the simplified expression
    simplified_expr += sum(squared_terms)

    print("The final simplified expression is: ")
    print(simplified_expr)

    return simplified_expr

    # Extracting terms with two variables and their coefficients
def extract_variable_terms(expression):
    terms_dict = expression.as_coefficients_dict()
    variable_terms = {}

    for term, coeff in terms_dict.items():
        variables = [symbol.name for symbol in term.free_symbols]
        
        if len(variables) == 1:
            variable_terms[(variables[0], variables[0])] = coeff
        elif len(variables) == 2:
            variable_terms[tuple(variables)] = coeff
    return variable_terms

def main():
    terms = createVariableList(stock_tickers,findWeights())
    final_dict = extract_variable_terms(square_and_expand_expression(create_squared_expression(terms)))
    print("The final dict is: ")
    print(final_dict)

main()