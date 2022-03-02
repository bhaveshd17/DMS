$(document).ready(function(){
    $(".ajaxLoader").hide();
	$(".certificate_update").click(function(){
        let id = $(this).data('id')
        let cer_obj = {"id":id}
		$.ajax({
            url:'/student/update_certificate/'+id,
            data:cer_obj,
            dataType:'json',
            beforeSend:function(){
                $(".ajaxLoader").show();
                $("#certificate_cards").hide();
            },
            success:function(res){
                // console.log(res);
                $(".ajaxLoader").hide();
                $("#certificate_cards").html(res.data);
                $("#certificate_cards").show();
            }
        });
    });
});