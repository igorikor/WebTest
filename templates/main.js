$(function(){

	var ip = '127.0.0.1:5000';

	$("#connect").click(function(){
		var com = $("#com").val();
		$.post('http://'+ip+'/connect',com);
	})

	$("#custom_command").click(function(){
		$("#log").append("-- "+$("#custom_command_text").val()+"\n");
		$("#custom_command_text").val("");
	})

	$("#xyz_coord").click(function(){
		$("#coord_1").text("X");
		$("#coord_2").text("Y");
		$("#coord_3").text("Z");
	})

	$("#some_coord").click(function(){
		$("#coord_1").text("A");
		$("#coord_2").text("B");
		$("#coord_3").text("C");
	})

})