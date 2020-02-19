baseUrl = 'http://localhost:8000'
const signupUrl = baseUrl + '/api/data';

$(document).ready(function() {
    $("#register").click(function() {
            $.get(signupUrl, {}, function(data) {
                if (data['result']) {
                    $("form")[0].reset();
                }
                alert(data);
            });
        }
    });
});