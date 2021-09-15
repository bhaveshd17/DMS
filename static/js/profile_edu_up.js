$(document).ready(function(){
    $(".ajaxLoader").hide();
	$(".edu_update").click(function(){
        let id = $(this).data('id')
        let edu_obj = {"id":id}
		$.ajax({
            url:'/student/updateEdu/'+id,
            data:edu_obj,
            dataType:'json',
            beforeSend:function(){
                $(".ajaxLoader").show();
                $("#edu_cards").hide();
            },
            success:function(res){
                // console.log(res.data);
                $(".ajaxLoader").hide();
                $("#edu_cards").html(res.data);
                $("#edu_cards").show();
            }
        });
    });
});

