

# stock_tickers = ["ibm","apple","microsoft"]
stock_tickers_test = ["ibm_0.125","apple_0.234","microsoft_0.325"]
from Changing_DWave_Output_Jake import createVariableList
import Finding_effective_weights as few
#Penalty coefficient
q = 0.8
stock_tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'FB', 'NFLX', 'NVDA', 'V', 'PYPL',
                 'INTC', 'CSCO', 'GS', 'JPM', 'IBM', 'GE', 'DIS', 'VZ', 'KO', 'PEP',
                 'WMT', 'COST', 'AMGN', 'GILD', 'PFE', 'BA', 'CAT', 'CVX', 'XOM', 'GS',
                 'HD', 'IBM', 'JNJ', 'MCD', 'MRK', 'NKE', 'P&G', 'TRV', 'UNH', 'UTX',
                 'WBA', 'MMM', 'CVS', 'ABT', 'ABBV', 'MO', 'JPM', 'BAC', 'WFC', 'C',
                 'MET', 'AXP', 'GS', 'USB', 'CME', 'GS', 'MS', 'JPM', 'GS', 'GS', 'AAPL',
                 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'FB', 'NFLX', 'NVDA', 'V', 'PYPL',
                 'INTC', 'CSCO', 'GS', 'JPM', 'IBM', 'GE', 'DIS', 'VZ', 'KO', 'PEP'] # 
stock_tickers_lower = [ticker.lower() for ticker in stock_tickers]
stock_values = {
    'AAPL': 0.0, 'GOOGL': 0.011, 'MSFT': 0.022,
    'AMZN': 0.032, 'TSLA': 0.043, 'FB': 0.054,
    'NFLX': 0.065, 'NVDA': 0.075, 'V': 0.086,
    'PYPL': 0.097, 'INTC': 0.108, 'CSCO': 0.118,
    'GS': 0.129, 'JPM': 0.14, 'IBM': 0.151,
    'GE': 0.161, 'DIS': 0.172, 'VZ': 0.183,
    'KO': 0.194, 'PEP': 0.204, 'WMT': 0.215,
    'COST': 0.226, 'AMGN': 0.237, 'GILD': 0.247,
    'PFE': 0.258, 'BA': 0.269, 'CAT': 0.28,
    'CVX': 0.29, 'XOM': 0.301, 'GS': 0.312,
    'HD': 0.312, 'IBM': 0.323, 'JNJ': 0.334,
    'MCD': 0.344, 'MRK': 0.355, 'NKE': 0.366,
    'P&G': 0.377, 'TRV': 0.387, 'UNH': 0.398,
    'UTX': 0.409, 'WBA': 0.419, 'MMM': 0.43,
    'CVS': 0.441, 'ABT': 0.452, 'ABBV': 0.462,
    'MO': 0.473, 'JPM': 0.484, 'BAC': 0.495,
    'WFC': 0.505, 'C': 0.516, 'MET': 0.527,
    'AXP': 0.537, 'GS': 0.548, 'USB': 0.559,
    'CME': 0.57, 'GS': 0.58, 'MS': 0.591,
    'JPM': 0.602, 'GS': 0.613, 'GS': 0.613,
    'AAPL': 0.624, 'GOOGL': 0.635, 'MSFT': 0.646,
    'AMZN': 0.656, 'TSLA': 0.667, 'FB': 0.678,
    'NFLX': 0.689, 'NVDA': 0.699, 'V': 0.71,
    'PYPL': 0.721, 'INTC': 0.732, 'CSCO': 0.742,
    'GS': 0.753, 'JPM': 0.764, 'IBM': 0.775,
    'GE': 0.785, 'DIS': 0.796, 'VZ': 0.807,
    'KO': 0.818, 'PEP': 0.828
}

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

official_stock_tickers = createVariableList(stock_tickers_lower,few.findWeights())


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

#take a store which contains the covariance values with penalty term applied
def calculate(store,ticker):
    calculatedResult={}

    #iterate through dictionary to get the key value in ticker
    for stock in ticker:
        word = stock.split("_")[0]
        for stock2 in ticker:
            word2 = stock2.split("_")[0]
            parts = (stock+","+stock2).split(',')
            reversed_key = ','.join(reversed(parts))
            if  reversed_key in calculatedResult:
                calculatedResult[reversed_key] += store.get(word+","+word2, 0)
            else:
                calculatedResult.setdefault(stock + "," + stock2,0)
                calculatedResult[stock+","+stock2] += store.get(word+","+word2, 0)
    for key in calculatedResult:
        calculatedResult[key] *= q
    print(calculatedResult)
        

# apply penalty coefficient to all values stock covariance values
def updateStore(stocks):
    store = {}
    result=0
    for stock, covar in stocks.items():   
        result = q*covar   
        store.setdefault(stock,result)
        store.setdefault(stock,result)
    return store
        

# relationship= updateStore(stocks)
# linearRelationship= calculate(relationship)
# print("This is the final linear relationship after applying the penalty term and adding equivalent tickers")
# print(linearRelationship)

calculate(stocks,official_stock_tickers)
# print(official_stock_tickers)


