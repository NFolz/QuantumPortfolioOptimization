# Finding effective weights

import pandas as pd
import numpy as np

# Variables
# maxPortfolioWeight = 0.2 # maximum % of portfolio that one single asset can occupy 
# minPortfolioWeight = 0 # minimum % of portfolio that one single asset can occupy
# granularityFactor = 15 # granularity of the weightings, higher the more computationally intensive
# q = 100 # The weighting factor to make this computationally relevant

def findPK(granFactor, maxPWeight, minPWeight): # Function to be called inside the findWeights one to adjust the PK
    basePK = (1/(2**granFactor))
    print("the base PK is "+ str(basePK))

    effectivePK = ((maxPWeight-minPWeight)*basePK)
    print("the effective PK is "+ str(effectivePK))

    return effectivePK

def findWeights(granularityFactor,maxPortfolioWeight,minPortfolioWeight): # fuction that will find the weights of the assets
    PK = findPK(granularityFactor,maxPortfolioWeight,minPortfolioWeight) # Calling function above using variables defined at the top
    weightList = []
    for i in range(granularityFactor): #iterating the same number of times as the granularity
        weight = (PK * (2**(i))) # finding the weight for that specific term
        weightList.append(weight) # Add the weight to the list
    #     print("List "+(str(i+1)) + ":" + str(weightList))
    # print("The maximum potential weighting of this asset in our portfolio is "+ str((sum(weightList)))+ ". This should be as close to "+str(maxPortfolioWeight)+" as possible.") 
    return weightList # return the final list
    







