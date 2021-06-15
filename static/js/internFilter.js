
$(document).ready(function(){
	$(".ajaxLoader").hide();
	$(".filter_data").on('change',function(){
		var filter_obj={};
        var starting_from = $('#starting_from').val();
        filter_obj.starting_from = starting_from;
		
		$(".custom-select").each(function(index,elem){
			var filter_val=$(this).val();
			var filter_key=$(this).data('filter');
			filter_obj[filter_key]=Array.from(document.querySelectorAll('#'+filter_key)).map(function(e){
			 	return e.value;
			});
		});
        
        console.log(filter_obj)

		$.ajax({
			url:'/student/internshipFilter',
			data:filter_obj,
			dataType:'json',
			beforeSend:function(){
				$(".ajaxLoader").show();
			},
			success:function(res){
				console.log(res);
				$("#filter_internships").html(res.data);
				$(".ajaxLoader").hide();
			}
		});
    });
});
