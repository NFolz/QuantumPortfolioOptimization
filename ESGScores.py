# returns = {"ibm": 0.76,
#           "microsoft": 0.26,
#           "apple": 0.7,
#           }

q = 0.8


# updates the returns by applying the penalty term to them
def updateESG(updateESG,q):
    
    for stock, returned in updateESG.items():   
        result = q*returned  
        updateESG[stock]=result
    return updateESG
    


#Add Updated returns to final Linear( both tickers are the same) Dictionary
def updateFinalLinearDic(finalDictionary,returnsDic):
    print("hi")
    #Go through List of all Variables
    for key, value in finalDictionary.items():
        stock_symbol_1, stock_symbol_2 = key
        #Split the variable names by format expected to check if they are the same relationship
        
        #if they are, create new element in result. Add the value from master dictionary and the value from updated stock returns dictionary
        if stock_symbol_1 == stock_symbol_2:
            finalDictionary[key] = finalDictionary.get(key, 0)
            finalDictionary[key] -= returnsDic.get(stock_symbol_1.split("_")[0])
            print(str(finalDictionary[key]))

