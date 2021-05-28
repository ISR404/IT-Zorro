document.addEventListener("DOMContentLoaded", function () {

    var emailField = document.getElementById('email');
    emailField.addEventListener("change", function () {

        var email = 'email=' + this.value;
        var url = emailField.dataset.url;

        var xhr = new XMLHttpRequest();
        xhr.open('POST', url, true);
        xhr.addEventListener('readystatechange', function () {
            if ( (xhr.readyState===4) && (xhr.status===200) ) {
                var notification = document.getElementById('checkemail-result');
                var data = JSON.parse(xhr.response);
                notification.innerHTML = data.message;
            }
        });

        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");

        xhr.send(email);

    });

});