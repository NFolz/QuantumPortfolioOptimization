from sympy import *

terms = ['X_2', 'Y_3', 'Z_4']

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

    # Remove squares for terms with a single variable
    final_expression = final_expression.as_ordered_terms()

    for i, term in enumerate(final_expression):
        if isinstance(term, Pow) and term.exp == 2 and len(term.free_symbols) == 1:
            final_expression[i] = term.base

    return sum(final_expression)

def combine_like_terms(expression):
    combined_expression = 0
    terms_dict = expression.as_coefficients_dict()

    for term, coeff in terms_dict.items():
        if isinstance(term, Pow) and term.exp == 2 and len(term.free_symbols) == 1:
            base = term.as_coeff_mul()[1][0]
            coefficient = term.as_coefficients_dict()[base]
            combined_expression += coefficient * base
        else:
            combined_expression += term * coeff

    return combined_expression


def main():
    squaredExpression = create_squared_expression(terms)
    print(squaredExpression)
    
    combinedExpression = combine_like_terms(squaredExpression)
    print(combinedExpression)

main()


