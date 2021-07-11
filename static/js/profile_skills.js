$(document).ready(function(){
    $("#skills_update").click(function(){
        var skills = $(this).data('skills')
        var skills_obj = {"skills":skills}
		$.ajax({
            url:'/student/UpdateSkills',
            data:skills_obj,
            dataType:'json',
            success:function(res){
                console.log(res);
                $("#profile_info").html(res.data);
            }
        });
    });
});