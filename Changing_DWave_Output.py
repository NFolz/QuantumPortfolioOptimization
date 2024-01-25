# Changing D-Wave output into backend input
import numpy
import pandas as pd
import Finding_effective_weights as few

# Creating containers for the data
quantumResults = [] # Resulting bit string from the quantum output
finalPortfolio = [] # Final data set of stocks and portfolio weights to be sent to backend
weightings = [] # Different weightings for each variable
tickers = ['IBM','MSFT','AAPL','ALPH','META','TSLA'] # All of the tickers we are using (imported from backend, in order of variables)

def createVariableList(tick,weights): # creating the variables that return as bits  
    variables = {} # dict to hold them
    tickerCount = 1 # first subscript is the ticker one
    for ticker in tick:
        weightCount =1 # second subscript is the weight one
        for weight in weights:
            variables["X_"+str(tickerCount)+"_"+str(weightCount)] = (ticker,weight) # append the variables dict by adding a new key (variable name) and tuple value (the ticker and the weight)
            weightCount+=1
        tickerCount+=1
    return variables

def main():
    print("This code creates a list of all the variables we will have, combining their tickers with their portfolio allocation.")
    weightings = few.findWeights()
    variableList = createVariableList(tickers, weightings)
    print("This is the final variable list: " + str(variableList))
    
    variable_key = 'X_3_2'
    if variable_key in variableList:
        ticker, weight = variableList[variable_key]
        print(f"If the quantum results indicate that {variable_key} is 1, then we should buy {ticker} with {weight} of our portfolio.")
    else:
        print(f"The variable {variable_key} is not present in the variable list.")

main()





