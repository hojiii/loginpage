function signup() {
    $.ajax({
        type: "POST",
        url: "/api/signup",
        data: {
            id_give: $('#input-id').val(),
            pw_give: $('#input-password').val(),
            pw_pw_give: $('#input-password2').val(),
            nickname_give: $('#input-nickname').val()
        },
        success: function (response) {
            if (response['result'] == 'success') {
                alert('회원가입이 완료되었습니다.')
                window.location.href = '/detail'
            } else {
                alert(response['msg'])
            }
        }
    })
}


