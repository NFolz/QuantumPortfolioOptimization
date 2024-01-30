returns = {"ibm": 0.76,
          "microsoft": 0.26,
          "apple": 0.7,
          }

q = 0.8


# updates the returns by applying the penalty term to them
def updateReturns(returns):
    updatedReturns ={}
    for stock, returned in returns.items():   
        result = q*returned  
        updatedReturns.setdefault(stock,result)
    return updatedReturns


#Add Updated returns to final Linear( both tickers are the same) Dictionary
def updateFinalLinearDic(finalDictionary,returnsDic):
    
    #Go through List of all Variables
    for stock in finalDictionary:
        #Split the variable names by format expected to check if they are the same relationship
        word = stock.split(",")[0]
        word2 =stock.split(",")[1]
        #if they are, create new element in result. Add the value from master dictionary and the value from updated stock returns dictionary
        if word==word2:

            finalDictionary[stock] = finalDictionary.get(stock, 0)
            finalDictionary += returnsDic.get(stock.split("_")[0])

            # finalDictionary[stock] += finalDictionary[stock]+b[word]
    
    #Return the updated linear dictionary
   


