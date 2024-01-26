from sympy import *
import Weight_Calculator_Module as WCM 
import findingEffectiveWeights as few
import Changing_DWave_Output as cdo 

terms= cdo.createVariableList(cdo.stock_tickers,few.findWeights())

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
    print("The expression is: ")
    print(final_expression)

    return final_expression


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
    final_dict = extract_variable_terms(square_and_expand_expression(create_squared_expression(terms)))
    print("The final dict is: ")
    print(final_dict)

main()