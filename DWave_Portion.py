from dwave.system import DWaveSampler, EmbeddingComposite
import random
sampler = EmbeddingComposite(DWaveSampler())

def build_relationships(*variables, linear=None, quadratic=None):
    """
    Build a dictionary representing relationships between variables.

    Parameters:
        *variables: Variable names (as strings).
        linear: Dictionary for linear relationships (default is None).
        quadratic: Dictionary for quadratic relationships (default is None).

    Returns:
        A dictionary representing relationships between variables.
    """
    if linear is None:
        linear = {}
    if quadratic is None:
        quadratic = {}

    # Add linear relationships for each variable with itself
    for variable in variables:
        linear[(variable, variable)] = 1

    # Add quadratic relationships between different variables
    for i in range(len(variables)):
        for j in range(i + 1, len(variables)):
            quadratic[(variables[i], variables[j])] = random.randint(-10,10)

    # Combine linear and quadratic relationships
    relationships = {**linear, **quadratic}

    return relationships

# Example usage:
def main():
    stock_tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'FB', 'NFLX', 'NVDA', 'V', 'PYPL',
                 'INTC', 'CSCO', 'GS', 'JPM', 'IBM', 'GE', 'DIS', 'VZ', 'KO', 'PEP',
                 'WMT', 'COST', 'AMGN', 'GILD', 'PFE', 'BA', 'CAT', 'CVX', 'XOM', 'GS',
                 'HD', 'IBM', 'JNJ', 'MCD', 'MRK', 'NKE', 'P&G', 'TRV', 'UNH', 'UTX',
                 'WBA', 'MMM', 'CVS', 'ABT', 'ABBV', 'MO', 'JPM', 'BAC', 'WFC', 'C',
                 'MET', 'AXP', 'GS', 'USB', 'CME', 'GS', 'MS', 'JPM', 'GS', 'GS', 'AAPL',
                 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'FB', 'NFLX', 'NVDA', 'V', 'PYPL',
                 'INTC', 'CSCO', 'GS', 'JPM', 'IBM', 'GE', 'DIS', 'VZ', 'KO', 'PEP']

    relationships_dict = build_relationships(*stock_tickers)

    print(relationships_dict)

    sampleset = sampler.sample_qubo(relationships_dict, num_reads=1000)

    print(sampleset)

main()