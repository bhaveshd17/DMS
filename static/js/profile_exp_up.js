$(document).ready(function(){
	$(".exp_update").click(function(){
        let id = $(this).data('id')
        let exp_obj = {"id":id}
		$.ajax({
            url:'/student/updateExp/'+id,
            data:exp_obj,
            dataType:'json',
            success:function(res){
                // console.log(res);
                $("#exp_cards").html(res.data);
            }
        });
    });
});
