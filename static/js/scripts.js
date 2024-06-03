$(document).ready(function(){
    // Function to send a message
    function sendMessage() {
        var message = $('.type_msg').val().trim();
        if (message !== '') {
            var messageContainer = $('.msg_card_body');
            var currentTime = new Date().toLocaleTimeString('en-US', {hour: '2-digit', minute: '2-digit'});
            var messageTemplate = `
                <div class="d-flex justify-content-end mb-4">
                    <div class="msg_cotainer_send">
                        ${message}
                        <span class="msg_time_send">${currentTime}</span>
                    </div>
                    <div class="img_cont_msg">
                        <img src="https://avatars.hsoubcdn.com/ed57f9e6329993084a436b89498b6088?s=256" class="rounded-circle user_img_msg">
                    </div>
                </div>`;
            messageContainer.append(messageTemplate);
            $('.type_msg').val('');
            // Scroll to the bottom of the message container
            messageContainer.scrollTop(messageContainer.prop("scrollHeight"));
        }
    }

    // Function to initiate a video call
    function startVideoCall() {
        // Code to initiate a video call using WebRTC
        // This could involve creating a peer connection, obtaining local media stream, and connecting to a signaling server
        // For brevity, I'm omitting the detailed WebRTC implementation here
    }

    // Function to initiate a voice call
    function startVoiceCall() {
        // Code to initiate a voice call using WebRTC
        // Similar to starting a video call, but without video stream
    }

    // Event listener for sending a message when Enter key is pressed
    $('.type_msg').keypress(function(event){
        if (event.which == 13) {
            event.preventDefault();
            sendMessage();
        }
    });

    // Event listener for sending a message when send button is clicked
    $('.send_btn').click(function(event){
        event.preventDefault();
        sendMessage();
    });

    // Event listener for video call button
    $('.fa-video').click(function(){
        startVideoCall();
    });

    // Event listener for voice call button
    $('.fa-phone').click(function(){
        startVoiceCall();
    });

    // Toggle action menu
    $('#action_menu_btn').click(function(){
        $('.action_menu').toggle();
    });

    // Add any additional functions or WebRTC implementation here
});
