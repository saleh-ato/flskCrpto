def MA(array,length=9):
    """Moving Average"""
    sum=0
    if len(array)<length:
        return False
    else:
        array=array[-length:]
        for i in range(1,len(array)):
            sum+=array[i]
        ma=sum/length
        return round(ma,2)

def EMA(array,length):
    """Exponential Moving Average"""
    if len(array)<length:
        return False
    else:
        alpha=2/(length+1)
        array=array[-length:]
        for i in range(1,len(array)):
            if i==1:
                ema=array[0]
            ema=round(alpha*array[i]+(1-alpha)*ema,2)
            #ema=round((array[i]-ema)*alpha +ema)
        return ema

def RSI(array,length=14):
    '''Relative strength index'''
    Avggain,Avgloss=AvgGL(array)
    rs=Avggain/Avgloss
    rsi=round(100-(100/(1+rs)),2)
    return rsi    

def AvgGL(a):
    gain=0
    loss=0
    a=a[-14:]
    for i in range(1,len(a)):
        diff=round(a[i]-a[i-1],2)
        print(a[i],diff)
        if(diff>0):
            gain+=round(diff,2)
        elif(diff<0):
            # print('loss ',loss,'+',round(abs(diff),2))
            loss+=round(abs(diff),2)
    print('gain ',gain, a[i])
    print('gain ',loss, a[i])
    Avggain=round(gain/14,2)
    Avgloss=round(loss/14,2)
    return Avggain,Avgloss

def MACD(prices,slow=26,fast=12):
    '''Moving Average Convergence Divergence'''
    #macd=EMA(prices["prices"],12)-EMA(prices["prices"],26)
    macd=round(EMA(prices,12)-EMA(prices,26),3)
    return macd

def AwesomeOscillator(Highs,Lows):
    # Median_Price=(High+Low)/2
    Median_Price=[]
    if len(Highs)!=len(Lows):
        return False
    Highs=Highs[-34:]
    Lows=Lows[-34:]
    print(len(Lows))
    for i in range(len(Highs)):
        Median_Price+=[round((Highs[i]+Lows[i])/2,2)]
    fast=MA(Median_Price,5)
    slow=MA(Median_Price,34)
    diff=slow-fast
    print(slow,fast)
    print(diff)

def Mean(array):
	sum=0
	for i in range(len(array)):
		sum+=round(array[i],2)
	mean=round(sum/len(array),2)
	return mean

def BollingerBands(closes):
	length=20
	mean=Mean(closes)
	#bollingerbands=()**0.5
	sum=0
	for i in range(len(closes)):
		sum+=(closes[i]-mean)**2
	StandardDeviation=(sum/length)**0.5
	upperBand=round(mean+StandardDeviation,2)
	lowerBand=round(mean-StandardDeviation,2)
	return [upperBand,lowerBand]

def MeanDeviation(prices):
	length=20
	mean=Mean(prices)
	meanDeviation=0
	for i in range(len(prices)):
		meanDeviation+=abs(prices[i]-mean)
	meanDeviation=round((1/length)*meanDeviation,2)
	return meanDeviation

def CCI(prices):
	length=20
	mean20=Mean(prices)
	meanDeviation=MeanDeviation(prices)
	cci=round((prices[-1]-mean20)/(0.015*meanDeviation),2)
	return cci

def MACross(prices):
	BullishFlag=None
	shortMAPrices=prices[-9:]
	longMAPrices=prices[-21:]
	shortMA=MA(shortMAPrices)
	longMA=MA(longMAPrices)
	if shortMA>longMA:
		BullishFlag=True
	elif shortMA<longMA:
		BullishFlag=False
	return BullishFlag

def RawMF(prices,volumes):
	length=14
	positiveMF=0
	negativeMF=0
	for i in range(1,len(prices)):
		if(prices[i]>prices[i-1]):
			positiveMF+=prices[i]*volumes[i]
		else:
			negativeMF+=prices[i]*volumes[i]
	return [positiveMF,negativeMF]
		
def MFI(prices,volumes):
	length=14
	rawmf=RawMF(prices,volumes)
	MoneyFlowRatio=rawmf[0]/rawmf[1]
	mfi= 100 - (100/1+MoneyFlowRatio)
	return mfi
#_______________________________________
def PositiveDM(today_high,yesterday_high,yesterday_low,today_low):
    if ((today_high - yesterday_high)> (yesterday_low - today_low)):
        positiveDM=max(today_high-yesterday_high,0)
    else:
        positiveDM=0
    return round(positiveDM,2)
def NegativeDM(today_high,yesterday_high,yesterday_low,today_low):
    if(yesterday_low-today_low>today_high-yesterday_high):
        negativeDM=max(yesterday_low-today_low,0)
    else:
        negativeDM=0
    return round(negativeDM,2)

def DI_DIFF(positiveDI,negativeDI):
    return round(abs(positiveDI-negativeDI),2)
def DI_SUM(positiveDI,negativeDI):
    return round(positiveDI+negativeDI,2)

def DI14(DM,TR):
    return round((100*(DM/TR)),2)

def DX(DI_diff,DI_sum):
    return round(100*(DI_diff/DI_sum),2)

def DMI(highs,lows,closes,length=14):
    TRs=[]
    positiveDMs=[]
    negativeDMs=[]
    if (len(closes)==len(lows)) and (len(closes)==len(highs)):
        for i in range(1,len(highs)):
            TRs+=[TR(highs[i],lows[i],closes[i-1])]
            positiveDMs+=[PositiveDM(highs[i],highs[i-1],lows[i-1],lows[i])]
            negativeDMs+=[NegativeDM(highs[i],highs[i-1],lows[i-1],lows[i])]
    Tr14=round(sum(TRs),2)
    PositiveDM14=round(sum(positiveDMs),2)
    NegativeDM14=round(sum(negativeDMs),2)
    Positive_DI=DI14(PositiveDM14,Tr14)
    Negative_DI=DI14(NegativeDM14,Tr14)
    return [Positive_DI,Negative_DI]

def TR(today_high,today_low,yesterday_close):
    tr_list=[]
    tr_list+=[today_high-today_low]
    tr_list+=[abs(today_high-yesterday_close)]
    tr_list+=[abs(today_low-yesterday_close)]
    return round(max(tr_list),2)

def Chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
    return lst