$(document).ready(function(){

    // sending a connect request to the server.
    // var socket = io.connect("http://localhost:5000");

    // An event handler for a change of value
    $('#voter').click(function(event) { 
        socket.emit('Slider value changed', {who: $('#candidate').attr('id'), data: $('candidate').val()});
        console.log("emited");
    });

    
    $('#cba').click(function(event) { 
        e.preventDefault();
        console.log("emited");
        alert("button");
    });

    socket.on('after connect', function(msg){
        console.log('After connect', msg);
    });

    socket.on('update value', function(msg) {
        console.log('Slider value updated');
        $('#'+msg.who).val(msg.data);
    });
});
