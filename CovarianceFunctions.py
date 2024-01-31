from Changing_DWave_Output_Jake import createVariableList
import Finding_effective_weights as few

#Add Covariance Terms
def addCovariance(finalDictionary,covarianceDictionary):
    #For loop to iterate through dictionary while seperating its key and value pairs
    for key, value in finalDictionary.items():
        #Creating two new variables that store the contents of the tuple that makes up the key
        stock_symbol_1, stock_symbol_2 = key
        
        #Get the stock ticker names from the dictionary so use as the search key in the covariance dictionary
        firstSearchVal=stock_symbol_1.split("_")[0]
        secondSearchVal=stock_symbol_2.split("_")[0]

        #Making the new tuple without weighting to use to search through returns dictionary
        comparisonValue = (firstSearchVal,secondSearchVal)

        # print(comparisonValue)

        #Getting the covariance value related to the variables implemented
        covariance_value = covarianceDictionary.get(comparisonValue)
        # print("The value added is" +str(covariance_value))

        #Ensures that covariance value is not none and then adds that value to the keys current pair value 
        if covariance_value is not None:
            finalDictionary[key] += covariance_value
            # print(str(finalDictionary[key]))



#Testing Values
covariances = {
    ("AAPL", "AAPL"): 1,
    ("AAPL", "GOOGL"): 0.45,
    ("AAPL", "MSFT"): 0.38,
    ("AAPL", "IBM"): 0.38,  # Include only the relevant entry for IBM

    ("GOOGL", "AAPL"): 0.45,
    ("GOOGL", "GOOGL"): 1,
    ("GOOGL", "MSFT"): 0.26,
    ("GOOGL", "IBM"): 0.26,  # Include only the relevant entry for IBM

    # ... Repeat the structure for other stocks
    ("IBM", "AAPL"): 0.38,
    ("IBM", "GOOGL"): 0.26,
    ("IBM", "MSFT"): 0.26,
    ("IBM", "IBM"): 1  # Include the self-covariance for IBM
}

stock_tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'FB', 'NFLX', 'NVDA', 'V', 'PYPL',
                 'INTC', 'CSCO', 'GS', 'JPM', 'IBM', 'GE', 'DIS', 'VZ', 'KO', 'PEP',
                 'WMT', 'COST', 'AMGN', 'GILD', 'PFE', 'BA', 'CAT', 'CVX', 'XOM', 'GS',
                 'HD', 'IBM', 'JNJ', 'MCD', 'MRK', 'NKE', 'P&G', 'TRV', 'UNH', 'UTX',
                 'WBA', 'MMM', 'CVS', 'ABT', 'ABBV', 'MO', 'JPM', 'BAC', 'WFC', 'C',
                 'MET', 'AXP', 'GS', 'USB', 'CME', 'GS', 'MS', 'JPM', 'GS', 'GS', 'AAPL',
                 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'FB', 'NFLX', 'NVDA', 'V', 'PYPL',
                 'INTC', 'CSCO', 'GS', 'JPM', 'IBM', 'GE', 'DIS', 'VZ', 'KO', 'PEP']



