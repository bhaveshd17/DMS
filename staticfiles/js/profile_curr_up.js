$(document).ready(function(){
    $(".ajaxLoader").hide();
	$(".curr_edu_update").click(function(){
        let id = $(this).data('id')
        let curr_edu_obj = {"id":id}
		$.ajax({
            url:'/student/update_current_education/'+id,
            data:curr_edu_obj,
            dataType:'json',
            beforeSend:function(){
                $(".ajaxLoader").show();
                $("#curr_edu_card").hide();
            },
            success:function(res){
                // console.log(res);
                $(".ajaxLoader").hide();
                $("#curr_edu_card").html(res.data);
                $("#curr_edu_card").show();
            }
        });
    });
});