failed=`<div class="row">
<div class="col-md-12"><a class="card py-5">
<info class="info">
<h2>مشکلی پیش آمده</h2><br>
<h3 class="h4">لطفا چند ثانیه بعد تلاش کنید</h3>
</info></a></div></div>`
var flag=false
var jqxhr = $.get("https://api.coingecko.com/api/v3/search/trending", function(data ) {
    })
    .done(function(data) {
    flag=true
    console.log(flag);
    $("div.cards-container").empty()
    rowcounter=0
    for(var i=0; i<(data["coins"]).length;i++){
        cardCreator(data["coins"][i]["item"],i)
    }
    })
    .fail(function() {
    })
    .always(function() {
        console.log(flag);
        if(flag==false){
            setTimeout(() => {$('div.cards-container').empty().html(failed)}, 1000);
        }
    });
function cardCreator(data,i){
    divrow=`<div class="row card-row`+rowcounter+`"></div>`
    if (i%4==0){
        rowcounter++;
        $("div.cards-container").append(divrow);

    }
    card_element=
    `
    <div class="col-md-3"><a href="#" class="card">
    <div class="image-container">
        <img src="`+data["large"]+`" width="71" style="z-index: 99;">
    </div>
    <info class="info">
    <h2>`+data["symbol"]+`</h2>
    <p>`+data["name"]+`</p>
    <p>Price:<br>`+(String(data["price_btc"]).substring(0,9))+` BTC</p>
    <p>Market Cap Rank:<br>`+data["market_cap_rank"]+`</p>
    </a>
    </info>
    </div>
    `
    $("div.card-row"+(rowcounter-1)).append(card_element);
}