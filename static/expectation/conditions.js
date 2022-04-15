var signals_obj={
    'good':'btn btn-success',
    'neutral':'btn btn-info',
    'warn':'btn btn-warning',
    'danger':'btn btn-danger'}
var texts_obj={
    'good':'مناسب برای خرید',
    'neutral':'متعادل',
    'warn':'نسبتا خطرناک',
    'danger':'فروش'}
var oscillators=["اشباع فروش","متعادل","نزدیک به اشباع خرید","اشباع خرید"]
function MACD_signal(macd){
    if(macd>0){
        signal=signals_obj["good"]
        text=texts_obj["good"]
    }else if(macd=0){
        signal=signals_obj["neutral"]
        text=texts_obj["neutral"]
    }else if(macd<0 && macd>40){
        signal=signals_obj["warn"]
        text=texts_obj["warn"]
    }else if(macd<0 && macd<40){
        signal=signals_obj["danger"]
        text=texts_obj["danger"]
    }
$(".macd-signal").text(text).addClass(signal)
}
function Oscillator_signal(mid,high,low,warn,value,id){
    if(low>value){
        signal=signals_obj["good"]
        text=oscillators[0]
    } else if (value>low && warn>value) {
        signal=signals_obj["neutral"]
        text=oscillators[1]       
    } else if (value>mid && warn>value) {
        signal=signals_obj["warn"]
        text=oscillators[2]
    } else if (value>high){
        signal=signals_obj["danger"]
        text=oscillators[3]
    }
    $("#"+id).text(text).addClass(signal)
}
function biggerSingal(lower,bigger,id){
    signal=bigger>lower?signals_obj["good"]:signals_obj["danger"]
    text=bigger>lower?texts_obj["good"]:texts_obj["danger"]
    $("#"+id).text(text).addClass(signal)
}
function BollingerSignal(lower,upper,price){
    if(price>lower && price<upper){
        signal=signals_obj["neutral"]
        text=texts_obj["neutral"]
    }else if(price>upper){
        signal=signals_obj["danger"]
        text=texts_obj["danger"]
    }else if(lower>price){
        signal=signals_obj["good"]
        text=texts_obj["good"]
    }
    $("#bollinger-signal").text(text).addClass(signal)
}