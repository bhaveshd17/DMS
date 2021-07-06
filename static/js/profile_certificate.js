$(document).ready(function(){
	$(".certificate_update").click(function(){
        let id = $(this).data('id')
        let cer_obj = {"id":id}
		$.ajax({
            url:'/student/update_certificate/'+id,
            data:cer_obj,
            dataType:'json',
            success:function(res){
                // console.log(res);
                $("#certificate_cards").html(res.data);
            }
        });
    });
});