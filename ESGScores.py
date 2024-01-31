# returns = {"ibm": 0.76,
#           "microsoft": 0.26,
#           "apple": 0.7,
#           }

q = 0.8


# updates the returns by applying the penalty term to them
def updateE(updateESG,q):
    
    for stock, returned in updateESG.items():   
        result = q*returned  
        updateESG[stock]=result
    


#Add Updated returns to final Linear( both tickers are the same) Dictionary
def updateFinalLinearDic(a,b):
    result = {}
    #Go through List of all Variables
    for stock in a:
        #Split the variable names by format expected to check if they are the same relationship
        word = stock.split("_")[0]
        word2 =stock.split("_")[2]
        #if they are, create new element in result. Add the value from master dictionary and the value from updated stock returns dictionary
        if word==word2:
            result.setdefault(stock,0)
            result[stock] += a[stock]+b[word]
    
    #Return the updated linear dictionary
    return result

