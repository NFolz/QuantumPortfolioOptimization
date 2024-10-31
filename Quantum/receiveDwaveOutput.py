# Changing D-Wave output into backend input
import numpy
import pandas as pd
import findingEffectiveWeights as few 

# Creating containers for the data
quantumResults = [] # Resulting bit string from the quantum output
finalPortfolio = [] # Final data set of stocks and portfolio weights to be sent to backend
weightings = [] # Different weightings for each variable
tickers = ['IBM','MSFT','AAPL','ALPH','META','TSLA'] # All of the tickers we are using (imported from backend, in order of variables)

# Function that will take the bit string with the highest number of counts from the sampleset input
def getOutput(sampleset):
    # Find the row with the highest 'num_oc.'
    max_occurrence_row = sampleset.loc[sampleset['num_oc.'].idxmax()]

    # Extract values from 'x1_1,' 'x1_2,' and 'x1_3' columns to form the bit string
    bit_string = max_occurrence_row[['x1_1', 'x1_2', 'x1_3']].values

    # Convert the bit string into an array and add it into the quantum results
    quantumResults = list(bit_string)

    return quantumResults

def createVariableList(tick,weights):
    variables = []
    # variables = {}
    for i in tick:
        for j in weights:
            variables.append(i+","+str(j))
            # variables.setdefault(i,j)
            print(variables)
    return variables

def main():
    print("This code creates a list of all the variables we will have, combining their tickers with their portfolio allocation.")
    weightings = few.findWeights()
    variableList = createVariableList(tickers,weightings)
    print("This is the final variable list: " + str(variableList))
    # if 'AAPL' in variableList:
        # print("If the quantum results indicate that AAPL is present, the weight is:", variableList['AAPL'])
    print("If the quantum results indicate that "+str(variableList[7])+" is 1, then we should buy that stock with that % of our portfolio. If the same stock is taken for more than one weighting, these will be summed. That is on the way.")

main()