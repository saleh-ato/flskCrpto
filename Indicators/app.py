import indicators
closes=[44.34,44.09,44.15,43.61,44.33,44.83,45.10,45.42,45.84,46.08,45.89,46.03,45.61,46.28,46.28]
# closes=[45.15,46.26,46.5,46.23,46.08,46.03,46.83,47.69,47.54,49.25,49.23,48.2,47.57,47.61]
#https://school.stockcharts.com/doku.php?id=technical_indicators:relative_strength_index_rsi
#print(RSI(0,0,0,closes,14))
# indicators.AvgGL(closes)
# indicators.RSI(closes,14)
# print(len(closes))

# lst=[5,8,8,8,9,4,321,5,49,88,8,7,5,213]
# lst=list(indicators.Chunks(lst, 3))
# print(lst)

#print(list(lst(range(10, 75), 10)))
#indicators.ema(closes,14)
# indicators.EMA(closes,14)
closes=[459.99,448.85,446.06,450.81,442.8,448.97,444.57,441.4,430.47,420.05,431.14,425.66,430.58,431.72,437.87,428.43,428.35,432.5,443.66,455.72,454.49,452.08,452.73,461.91,463.58,461.14,452.08]
print(indicators.EMA(closes,12))
print(indicators.MACD(closes,23,12))
#print(len(closes))

highs=[5,3,4,7,8,4,8,6,3,2,46,64,5,47,65,7,4,2,4323,5,464,7,5,6,5,87,6875,5,48,498,7,561,23,48,7,9,7,98]

lows=[1,2,3,5,88,4,5,1,5,4,7,9,9,21,4,8,9,7,9,8,21,65,48,97,5,8,1,3,7,9,0,2,1,1,31,87,89,8]
# print(len(highs))
indicators.AwesomeOscillator(highs,lows)
print()
print(indicators.McGinely(closes))
print(indicators.MA(closes))
print('ema: ',indicators.EMA(closes,14))
prices=[10, 12, 23, 23, 16, 23, 21, 16,15,17,19,14,12,9,17,15,13,18,20,16]
#print(len(prices))
print(indicators.Mean(prices))
#print(BollingerBands(prices))
print(indicators.MeanDeviation(prices))
print(indicators.CCI(prices))
print(indicators.MACross(prices))