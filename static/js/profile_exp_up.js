$(document).ready(function(){
    $(".ajaxLoader").hide();
	$(".exp_update").click(function(){
        let id = $(this).data('id')
        let exp_obj = {"id":id}
		$.ajax({
            url:'/student/updateExp/'+id,
            data:exp_obj,
            dataType:'json',
            beforeSend:function(){
                $(".ajaxLoader").show();
                $("#exp_cards").hide();
            },
            success:function(res){
                // console.log(res);
                $(".ajaxLoader").hide();
                $("#exp_cards").html(res.data);
                $("#exp_cards").show();
            }
        });
    });
});
