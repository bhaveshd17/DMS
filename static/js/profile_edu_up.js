$(document).ready(function(){
	$(".edu_update").click(function(){
        let id = $(this).data('id')
        let edu_obj = {"id":id}
		$.ajax({
            url:'/student/updateEdu/'+id,
            data:edu_obj,
            dataType:'json',
            success:function(res){
                // console.log(res);
                $("#edu_cards").html(res.data);
            }
        });
    });
});

