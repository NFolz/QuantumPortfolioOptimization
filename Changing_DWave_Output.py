# Changing D-Wave output into backend input
import numpy
import pandas as pd
import Finding_effective_weights as few

# Creating containers for the data
quantumResults = [] # Resulting bit string from the quantum output
finalPortfolio = [] # Final data set of stocks and portfolio weights to be sent to backend
weightings = [] # Different weightings for each variable
stock_tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'FB', 'NFLX', 'NVDA', 'V', 'PYPL',
                 'INTC', 'CSCO', 'GS', 'JPM', 'IBM', 'GE', 'DIS', 'VZ', 'KO', 'PEP',
                 'WMT', 'COST', 'AMGN', 'GILD', 'PFE', 'BA', 'CAT', 'CVX', 'XOM', 'GS',
                 'HD', 'IBM', 'JNJ', 'MCD', 'MRK', 'NKE', 'P&G', 'TRV', 'UNH', 'UTX',
                 'WBA', 'MMM', 'CVS', 'ABT', 'ABBV', 'MO', 'JPM', 'BAC', 'WFC', 'C',
                 'MET', 'AXP', 'GS', 'USB', 'CME', 'GS', 'MS', 'JPM', 'GS', 'GS', 'AAPL',
                 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'FB', 'NFLX', 'NVDA', 'V', 'PYPL',
                 'INTC', 'CSCO', 'GS', 'JPM', 'IBM', 'GE', 'DIS', 'VZ', 'KO', 'PEP'] # All of the tickers we are using (imported from backend, in order of variables)

def createVariableList(tick,weights): # creating the variables that return as bits  
    variables = []
    for ticker in tick:
        for weight in weights:
            variables+=[str(ticker)+"_"+str(weight)]
    return variables

def main():
    print("This code creates a list of all the variables we will have, combining their tickers with their portfolio allocation.")
    weightings = few.findWeights()
    variableList = createVariableList(stock_tickers, weightings)
    print("This is the final variable list: " + str(variableList))

main()





