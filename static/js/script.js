$(function() {

	$("#donate__info").hide();
	$("#menu__block").hide();

	var date = new Date();
	var day = date.getDate() + 1;
	var month = date.getMonth() + 1 ;
	if(day >= 32) { day = day - 1 }
	
	$("#timer").countdown("2021/" + month + "/" + day, function(event) {
		$('#timer__day').text(event.strftime('%d'));
		$('#timer__hour').text(event.strftime('%H'));
		$('#timer__minute').text(event.strftime('%M'));
		$('#timer__second').text(event.strftime('%S'));
	});

	$("#ajax__product").change(function() {
		$.ajax({
			url: "/api/product/get",
			method: "POST",
			data: "id=" + $("#ajax__product").val(),
			success: function(data) {
				var json = JSON.parse(data);
				if(json.error == null) {
					$("#ajax__buy").text("ПРИОБРЕСТИ ЗА " + json.price + " руб");
				} 
			}
		});
	});

	$("#menu__open").on("click", function() {
		$("#menu__block").fadeIn(300);
		$("body").css("overflow-y", "hidden");
	});

	$("#menu__close").on("click", function() {
		$("#menu__block").fadeOut(300);
		$("body").css("overflow-y", "scroll");
	});

	$("#ajax__buy").on("click", function() {
		$.ajax({
			url: "/api/kassa/generate",
			method: "POST",
			data: "username=" + $("#ajax__username").val() + "&product=" + $("#ajax__product").val() + "&coupon=" + $("#ajax__coupon").val(),
			success: function(data) {
				var json = JSON.parse(data);
				if(json.error == null) {
					location.href=json.url;
				}else{
					alert(json.error);
				}
			}
		});
	});

});