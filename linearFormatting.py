from dwaveDataFormater import calculate, updateStore
from returnsFormater import updateReturns

stocks = {"ibm,apple": 0.76,
          "ibm,microsoft": 0.26,
          "ibm,ibm": 1,
          "microsoft,apple": 0.45,
          "microsoft,microsoft": 1,
          "microsoft,ibm": 0.56,
          "apple,apple": 1,
          "apple,microsoft": 0.66,
          "apple,ibm": 0.38}

returns = {"ibm": 0.76,
          "microsoft": 0.26,
          "apple": 0.7,
          }


store = updateStore(stocks)
print(store)
calculated = calculate(store)
print(calculated)
adjustedReturns = updateReturns(returns)
print(adjustedReturns)


for stock, val in adjustedReturns.items():
    search = stock+","+stock
    print(search)
    adjustedReturns[stock]+=calculated[search]

print (adjustedReturns)