document.addEventListener('DOMContentLoaded', function() {
    var message = document.querySelector('.message');

    function bounce() {
        message.style.position = 'relative';
        var pos = 0;
        var direction = 1;
            setInterval(function() {
                pos += direction * 5;
                message.style.top = pos + 'px';
                if (pos >= 200 || pos <= 0) {
                    direction *= -1;
                }
                }, 
                40
            );
    }

    bounce();
});
