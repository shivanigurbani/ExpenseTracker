
    setTimeout(function() {
        var messageDivs = document.querySelectorAll(".messages > div");
        messageDivs.forEach(function(div) {
            div.remove();
        });
    }, 3000); // 3000 milliseconds = 3 seconds

