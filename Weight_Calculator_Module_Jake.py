# Module that will be used to calculate the weights
# Taking all variables (Ticker, weight), adding them all together, subtracting 1 from it, and squaring the entire term, then finding the relationship between each as the output
# Final output should respect the final dict format: {('IBM_0.125','MSFT_0.00625'):3,...}

from sympy import *

terms_list = ['IBM_0.4','IBM_0.2','MSFT_0.4','MSFT_0.2','AAPL_0.4','AAPL_0.2']

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


def main():
    expression = create_squared_expression(terms_list)
    print("THis is the expression to be squared: "+str(expression))
    expanded_expression = square_and_expand_expression(expression)
    print("This is the final expanded expression after squaring: "+str(expanded_expression))

    two_variable_terms = extract_variable_terms(expanded_expression)

    # Printing the results
    for term, coeff in two_variable_terms.items():
        print(f"Term: {term}, Coefficient: {coeff}")
    print(two_variable_terms)

main()



