

# stock_tickers = ["ibm","apple","microsoft"]
stock_tickers = ["ibm_0.125","apple_0.234","microsoft_0.325"]

#Penalty coefficient
q = 0.8

#Test data
stocks = {"ibm,apple": 0.38,
          "ibm,microsoft": 0.26,
          "ibm,ibm": 1,
          "microsoft,apple": 0.45,
          "microsoft,microsoft": 1,
          "microsoft,ibm": 0.26,
          "apple,apple": 1,
          "apple,microsoft": 0.45,
          "apple,ibm": 0.38}



#add up covariance for same two companies
# def calculate(store):
#     calculatedResult={}
#     for stock, covar in store.items():
#         parts = stock.split(',')
#         reversed_key = ','.join(reversed(parts))
#         # print(reversed_key)
#         if  stock in calculatedResult:
#             calculatedResult[stock] += covar
#         elif reversed_key in calculatedResult:
#             calculatedResult[reversed_key] += covar
#         else: 
#             calculatedResult[stock] = covar
#     return calculatedResult

# linear = {('a','a'):-1}
# for key, value in linear.items():
#     if key[0] == key[1]:


def calculate(store,ticker):
    calculatedResult={}
    for stock in ticker:
        word = stock.split("_")[0]
        for stock2 in ticker:
            word2 = stock.split("_")[2]
            parts = (stock+","+stock2).split(',')
            reversed_key = ','.join(reversed(parts))
            if  reversed_key in calculatedResult:
                calculatedResult[reversed_key] += store.get(reversed_key, 0)
            else:
                calculatedResult.setdefault(stock + "," + stock2,0)
                calculatedResult[stock+","+stock2] += store.get(stock+","+stock2, 0)
    print(calculatedResult)
        

# apply penalty coefficient to all values stock vovariance values
def updateStore(stocks):
    store = {}
    result=0
    for stock, covar in stocks.items():   
        result = q*covar   
        store.setdefault(stock,result)
    return store
        

# relationship= updateStore(stocks)
# linearRelationship= calculate(relationship)
# print("This is the final linear relationship after applying the penalty term and adding equivalent tickers")
# print(linearRelationship)

calculate(stocks,stock_tickers)


