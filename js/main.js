$(document).ready(function(){
    const sidebarbtn = $('#chat-sidebar');
    const chat = $('#chat');

    sidebarbtn.on('click', function(){
        chat.toggleClass('chat--close');
    })
});