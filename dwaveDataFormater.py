

#Penalty coefficient
q = 0.8

#Test data
stocks = {"ibm,apple": 0.76,
          "ibm,microsoft": 0.26,
          "ibm,ibm": 1,
          "microsoft,apple": 0.45,
          "microsoft,microsoft": 1,
          "microsoft,ibm": 0.56,
          "apple,apple": 1,
          "apple,microsoft": 0.66,
          "apple,ibm": 0.38}



#add up covariance for same two companies
def calculate(store):
    calculatedResult={}
    for stock, covar in store.items():
        parts = stock.split(',')
        reversed_key = ','.join(reversed(parts))
        # print(reversed_key)
        if  stock in calculatedResult:
            calculatedResult[stock] += covar
        elif reversed_key in calculatedResult:
            calculatedResult[reversed_key] += covar
        else: 
            calculatedResult[stock] = covar
    return calculatedResult


# apply penalty coefficient to all values stock vovariance values
def updateStore(stocks):
    store = {}
    result=0
    for stock, covar in stocks.items():   
        result = q*covar   
        store.setdefault(stock,result)
    return store
        

relationship= updateStore(stocks)
linearRelationship= calculate(relationship)
print("This is the final linear relationship after applying the penalty term and adding equivalent tickers")
print(linearRelationship)


