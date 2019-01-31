$(document).ready(function (){
    document.getElementById('btn').onclick = function(){
       $.ajax({
        type:'get',
        url:'/my_app/stuinfo/',
        dataType:'json',
        success:function(data,status){
            console.log(data)
            var d = data["data"]
            for(var i = 0;i < d.lenth; i++){
                document.write('<p>' +d[i][0] + '</p>')
            }
        }
       })
    }
})