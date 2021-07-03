$(document).ready(function(){
	$(".fe_update").click(function(){
        let id = $(this).data('id')
        let year = $(this).data('year')
		$.ajax({
            url:'/student/update_current_education/'+id+'/'+year,
            data:{},
            dataType:'json',
            success:function(res){
                // console.log(res);
                $("#fe_card").html(res.data);
            }
        });
    });
	$(".se_update").click(function(){
        let id = $(this).data('id')
        let year = $(this).data('year')
		$.ajax({
            url:'/student/update_current_education/'+id+'/'+year,
            data:{},
            dataType:'json',
            success:function(res){
                // console.log(res);
                $("#se_card").html(res.data);
            }
        });
    });

	$(".te_update").click(function(){
        let id = $(this).data('id')
        let year = $(this).data('year')
		$.ajax({
            url:'/student/update_current_education/'+id+'/'+year,
            data:{},
            dataType:'json',
            success:function(res){
                // console.log(res);
                $("#te_card").html(res.data);
            }
        });
    });
    
	$(".be_update").click(function(){
        let id = $(this).data('id')
        let year = $(this).data('year')
		$.ajax({
            url:'/student/update_current_education/'+id+'/'+year,
            data:{},
            dataType:'json',
            success:function(res){
                // console.log(res);
                $("#be_card").html(res.data);
            }
        });
    });
});