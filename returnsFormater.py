# returns = {"ibm": 0.76,
#           "microsoft": 0.26,
#           "apple": 0.7,
#           }

q = 0.8


# updates the returns by applying the penalty term to them
def updateReturns(returns):
    updatedReturns ={}
    for stock, returned in returns.items():   
        result = q*returned  
        updatedReturns.setdefault(stock,result)
    return updatedReturns


# x =updateReturns({"ibm":2,"apple":3})
# print(x)