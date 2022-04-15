// var element = document.getElementById('Messages');
// element.addEventListener('click', function handleClick() {
//     console.log('element clicked');
// });
navs=['Information','Calculator','Other-Coins']
function remove_from(array,str){
    temp=[];
    for(var i=0;i<array.length;i++){
        if(array[i]!==str){
            temp.push(array[i]);
        }
    }
    return temp;
}

var el=$(".nav-item")
el.on( "click", function() {
    console.log($( this ).text());
    element=$( this ).text().trim().split("\n").slice(-1)[0].trim();
    // element_name=element[1].trim();
    
    // console.log(element_name);
    // console.log($( this ).attr('class'));
    // Inner_nav(element_name)
    // Nav_Choicer(element_name)
    Nav_Choicer(element)
  });
// $("#messages").css("border","1px solid #000 !important")

function Inner_nav(name){
    switch(name){
        case "Calculator":
            $('.'+name).addClass("active")
            $('.'+"Information").addClass("hidden")
            $('.'+"Other-coins").addClass("hidden")
            break;
        case "Other-Coins":
            $('.'+name).addClass("active")
            $('.'+"Information").addClass("hidden")
            $('.'+"Other-coins").addClass("hidden")
            break;
        case "Information":            
            $(".Information").addClass("active")
            break;
        default:
          // code block
      }
}

function Nav_Choicer(name){
    $('.'+name).addClass("active");
    console.log('.'+name)
    navigs=remove_from(navs,name)
    
    console.log(navigs);
    hidden(navigs)
    $('.'+name).removeClass("hidden");
}
function hidden(array){
    for(var i=0;i<array.length;i++){
        $('.'+array[i]).removeClass("active");
        $('.'+array[i]).addClass("hidden");
    }
}
var trending=$(".nav-item")

function localestr(element) {
    num=element.val()
    if(element.val()==''){
        element.val("")
    }else{
        element.val(null).val(parseInt(num).toLocaleString())
    }
}

function Create_element_tr(name,nickname,img_addr) {
    console.log(name,nickname,img_addr)
    var trending_coins_element=`
<li class="list-group-item border-0 d-flex align-items-center px-0 mb-2 pt-0">
    <div class="avatar me-3">
        <img src=`+img_addr+`alt="kal" class="border-radius-lg shadow">
    </div>
    <div class="d-flex align-items-start flex-column justify-content-center">
        <h6 class="mb-0 text-sm">`+name+`</h6>
        <p class="mb-0 text-xs">`+nickname+`</p>
    </div>
</li>
`
return trending_coins_element
}
$(document).ready(function(){
    $("#calculate").on("click", function(){
    BasePrice=$("#BasePrice").text()
    amount=$("#Amount").val()?$("#Amount").val():0
    DollarPrice=$("#DPrice").val()?$("#DPrice").val():0
    localestr($("#Amount"))
    localestr($("#DPrice"))
    $("#result").html((amount*DollarPrice*BasePrice).toLocaleString()+" تومان")
    $("#formula").html(amount.toLocaleString()+"*"+DollarPrice.toLocaleString()+"*"+BasePrice.toLocaleString()+"=")
    });
    
    $("#reset").on("click", function(){
        $("#Amount").val("")
        $("#DPrice").val("")
        $("#result").empty()
        $("#formula").empty()
    });
    $("#Tr").on("click", function(){
        var jqxhr = $.get("https://api.coingecko.com/api/v3/search/trending", function(data){
        })
        .done(function(data) {
        rowcounter=0
        pubvar=data;
        for(var i=0; i<4;i++){
            coin=data["coins"][i]["item"]
            element=Create_element_tr(coin["id"],coin["name"],coin["small"])
            $("#trendcoins").append(element)
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
    });
});
