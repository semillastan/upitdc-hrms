$(document).ready(function(){
	$(this).find('div.main').each(function(){
		var submain = $(this).find('div.sub');
		$(this).mouseenter(function(){
			$(submain).show();
		}).mouseleave(function(){
			$(submain).hide();
		});
	});
});
