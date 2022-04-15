function MA(array,length=9){
    // Moving Average
    let sum=0;
    if (array.length<length){
        return false
    }
    else{
        array=array.slice(-length)
        for(let a=0;a<array.length;a++){
            sum+=array[a]
        }
        ma=sum/length
    }
    return ma
}
function EMA(array,length){
    sum=0
    // Exponential Moving Average
    if (array.length<length){
        return False
    }
    else{
        alpha=2/(length+1)
        array=array.slice(-length)
        for(i=1;i<array.length;i++){
            sum+=array[i];
            if (i==1){
                ema=array[0]
            }
            ema=alpha*array[i]+(1-alpha)*ema
        }
    }
    return ema
}

function AvgGL(a){
    gain=0
    loss=0
    a=a.slice(-14)
    for (let i = 0; i < a.length; i++) {
        diff=a[i]-a[i-1]
        if(diff>0){
            gain+=diff
        }
        else if(diff<0){
            loss+=Math.abs(diff)  
        }
    }
    Avggain=gain/14
    Avgloss=loss/14
    return [Avggain,Avgloss]
}

function RSI(array,length=14){
    // Relative strength index
    avg=AvgGL(array)
    Avggain=avg[0]
    Avgloss=avg[1]
    rs=Avggain/Avgloss
    rsi=100-(100/(1+rs))
    return rsi
}
function MACD(prices,slow=26,fast=12){
    // Moving Average Convergence Divergence
    macd=EMA(prices,12)-EMA(prices,26)
    return macd
}
function Mean(array){
    sum=0
	for(i=0;i<array.length;i++){
		sum+=array[i]
    }
	mean=sum/array.length
	return mean
}
function BollingerBands(closes){
    length=20
    closes=closes.slice(-20)
	mean=Mean(closes)
	sum=0
    for (i=0;i<closes.length;i++){
        sum+=Math.pow(closes[i]-mean,2)
    }
	StandardDeviation=Math.pow(sum/length,0.5)
	upperBand=mean+StandardDeviation
	lowerBand=mean-StandardDeviation
	return [upperBand,lowerBand]
}
function MeanDeviation(prices){
    length=20
    prices=prices.slice(-20)
    mean=Mean(prices)
    meanDeviation=0
    for (i=0;i<prices.length;i++){
        meanDeviation+=Math.abs(prices[i]-mean)
    }
    meanDeviation=(1/length)*meanDeviation
    return meanDeviation
}
function CCI(prices){
    length=20
    prices=prices.slice(-20)
	mean20=Mean(prices)
	meanDeviation=MeanDeviation(prices)
	cci=(prices[prices.length-1]-mean20)/(0.015*meanDeviation)
	return cci
}
function RawMF(prices,volumes){
    length=14
	positiveMF=0
	negativeMF=0
    prices=prices.slice(-14)
    for (i=0;i<prices.length;i++){
        if(prices[i]>prices[i-1]){
			positiveMF+=prices[i]*volumes[i]
        }
		else{
			negativeMF+=prices[i]*volumes[i]
        }
    }
	return [positiveMF,negativeMF]    
}
function MFI(prices,volumes){
    length=14
	rawmf=RawMF(prices,volumes)
	MoneyFlowRatio=rawmf[0]/rawmf[1]
	mfi= 100 - (100/1+MoneyFlowRatio)
	return mfi
}
function PositiveDM(today_high,yesterday_high,yesterday_low,today_low){
    if((today_high - yesterday_high)> (yesterday_low - today_low)){
        positiveDM=Math.max(today_high-yesterday_high,0)
    }
    else{
        positiveDM=0
    }
    return positiveDM
}
function NegativeDM(today_high,yesterday_high,yesterday_low,today_low){
    if(yesterday_low-today_low>today_high-yesterday_high){
        negativeDM=Math.max(yesterday_low-today_low,0)
    }
    else{
        negativeDM=0
    }
    return negativeDM
}
function DI_DIFF(positiveDI,negativeDI){
    return Math.abs(positiveDI-negativeDI)
}
function DI_SUM(positiveDI,negativeDI){
return positiveDI+negativeDI
}
function DI14(DM,TR){
    return (100*(DM/TR))
}
function TR(today_high,today_low,yesterday_close){
    tr_list=[]
    tr_list.push(today_high-today_low)
    tr_list.push(Math.abs(today_high-yesterday_close))
    tr_list.push(Math.abs(today_low-yesterday_close))
    return Math.max(...tr_list)
}
function DX(DI_diff,DI_sum){
    return 100*(DI_diff/DI_sum)
}
function DMI(highs,lows,closes,length=14){
    TRs=[]
    positiveDMs=[]
    negativeDMs=[]
    highs=highs.slice(-14)
    lows=lows.slice(-14)
    closes=closes.slice(-14)
    if ((closes.length)==(lows.length) && ((closes.length)==(highs.length))){
        for(i=1;i<highs.length;i++){
            TRs.push(TR(highs[i],lows[i],closes[i-1]))
            positiveDMs.push(PositiveDM(highs[i],highs[i-1],lows[i-1],lows[i]))
            negativeDMs.push(NegativeDM(highs[i],highs[i-1],lows[i-1],lows[i]))
        }
    }
    Tr14=TRs.reduce((previousValue, currentValue) => previousValue + currentValue);
    PositiveDM14=positiveDMs.reduce((previousValue, currentValue) => previousValue + currentValue);
    NegativeDM14=negativeDMs.reduce((previousValue, currentValue) => previousValue + currentValue);
    Positive_DI=DI14(PositiveDM14,Tr14)
    Negative_DI=DI14(NegativeDM14,Tr14)
    return [Positive_DI,Negative_DI]
}
