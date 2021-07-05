var filter_obj={
	"skills":["e.g. JAVA"],
	"salary":"0",
	"starting_from":"",
    "location":["e.g. Mumbai"],
	"sort_by_date":false,
	"work_from_home":false,
};
const ajax_method = {
	url:'/student/jobFilter',
	data:filter_obj,
	dataType:'json',
	beforeSend:function(){
		$(".ajaxLoader").show();
	},
	success:function(res){
		// console.log(res);
		$("#filter_jobs").html(res.data);
		$(".ajaxLoader").hide();
	}
}

$(document).ready(function(){
	$(".ajaxLoader").hide();
	$(".sort_by_date").delegate("p", "click", function(){
		filter_obj.sort_by_date = true
		$.ajax(ajax_method);

	  });
	$("#salary").on('click', function(){
		var salary = $('#salary').val()
		filter_obj.salary = salary
		$.ajax(ajax_method);
	})

	$(".filter_data").on('change',function(){
        var starting_from = $('#starting_from').val();
        filter_obj.starting_from = starting_from;
		work_from_home = $('#work_from_home').is(":checked");
		filter_obj.work_from_home = work_from_home;

		$(".custom-select").each(function(index,elem){
			var filter_val=$(this).val();
			var filter_key=$(this).data('filter');
			filter_obj[filter_key]=Array.from(document.querySelectorAll('#'+filter_key)).map(function(e){
			 	return e.value;
			});
            // console.log(filter_obj)
		});
		$.ajax(ajax_method);
    });
});
