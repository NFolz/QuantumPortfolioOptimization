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
          "MSFT": 0.26,
          "apple": 0.7,
          }


store = updateStore(stocks)
print(store)
calculated = calculate(store)
print(calculated)
adjustedReturns = updateReturns(returns)
print(adjustedReturns)

testInput = {"IBM,0,IBM,2":2,}

def removingDoublesFromReturns(q,*something,returns):
    for stock, val in adjustedReturns.items():
        #Split key by the comma to be able to isolate the two companies being compared
        words = stock.split(',')
    
        if words[0]==words[2]:
            search = stock+","+stock
            print(search)
            adjustedReturns[stock]-=calculated[search]*q

print (adjustedReturns)