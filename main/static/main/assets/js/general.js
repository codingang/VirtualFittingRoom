function rendermainpage(){
	$(".contain-page").load("/mainpage");
}
function rendertopmenu(){
	$(".header-wrap").load("/top_menu");
}
function homeclick(){
	$("#home").click(function(){
		$(".contain-page").load("/mainpage");
	});
}
function rendergrids(num_of_items, images, item_names, prices, ids){
		if(jQuery.type(num_of_items)!="number" || jQuery.type(images)!="array" || jQuery.type(item_names)!="array"|| jQuery.type(prices)!="array", jQuery.type(ids)!="array"){
			return false;
		}
		for ( var i = 0; i < num_of_items; i++ ) {
			var item = '<li> <a href="'+item_names[i] + "_" + ids[i] + '" id="item-img'+i+'"></a> <a href="'+item_names[i] + "_" + ids[i] +'" class="title">'+item_names[i]+'</a><strong>&dollar;'+prices[i].toFixed(2)+'</strong></li>'
			$("#items").append(item);
			$("a#item-img"+i).html("<img src='"+images[i]+"'/>");
		}
		return true;
}
function capitaliseFirstLetter(string)
{
	if(string ==""){
		return "";
	}
    return string.charAt(0).toUpperCase() + string.slice(1);
}
function toTitleCase(str)
{
    return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
}
function renderpage(desp, image, item_name, price,  brand){
	if(jQuery.type(desp)!="string" || jQuery.type(image)!="string" || jQuery.type(item_name)!="string"|| jQuery.type(price)!="number"){
		return false;
	}
	$("#price").html("Price: &dollar;"+price);
	var current_category = capitaliseFirstLetter(window.location.pathname.split('/')[1]);
	$("#breadcrumb").html('<a href="/'+current_category+'">'+current_category+'</a> > '+item_name );
	$("#item_name").html(item_name );
	$("#desp").html("Description: "+desp);
	$("#images").html("<img src='"+image+"' align='right'/>");
    $("#brand").html("Brand: " + brand);
	return true;
}
