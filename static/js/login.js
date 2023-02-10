
//아이디 비밀번호 입력 여부 확인하기
const loginId = document.getElementById('LOGIN_ID');
const loginPw = document.getElementById('LOGIN_PW');
const loginBtn = document.getElementById('LOGIN_BTN');

function color() {
    if(loginId.value.length>0/* && loginId.value.indexOf("@")!==-1*/
        && loginPw.value.length>=5){
        loginBtn.style.backgroundColor = "#0095F6";
        loginBtn.disabled = false;
    }else{
        loginBtn.style.backgroundColor = "#C0DFFD";
        loginBtn.disabled = true;
    }
}


loginId.addEventListener('keyup', color);
loginPw.addEventListener('keyup', color);


//로그인 클릭시 회원 정보 확인
function open_site() {
    $.ajax({
        type: "POST",
        url: '/api/login',
        data: {
            id_give: $('#LOGIN_ID').val(),
            pw_give: $('#LOGIN_PW').val()
        },
        success: function (response) {
            if (response['result'] == 'success') {
                $.cookie('mytoken', response['token']);
                alert('로그인 완료')
                window.location.href = '/detail'
            } else {
                alert(response["msg"])
            }
        }
    });
}
