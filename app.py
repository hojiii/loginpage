import certifi
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
import hashlib

app = Flask(__name__)

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.0x2me9v.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/detail')
def detail():
    return render_template('detail.html')



# [회원가입 API]
# id, pw, nickname을 받아서, mongoDB에 저장합니다.
# 저장하기 전에, pw를 sha256 방법(=단방향 암호화. 풀어볼 수 없음)으로 암호화해서 저장합니다.
@app.route('/api/signup', methods=['POST'])
def api_signup():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    pw_pw_receive = request.form['pw_pw_give']
    nickname_receive = request.form['nickname_give']

    check = db.login.find_one({'id' : id_receive})
    
    if check is not None :
        return jsonify({'msg':'이미 존재하는 아이디입니다 !'})
    elif pw_receive != pw_pw_receive:
        return jsonify({'msg':'패스워드가 일치하지 않습니다 !'})
    else:
        pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
        db.login.insert_one({'id': id_receive, 'pw': pw_hash, 'nick': nickname_receive})

        return jsonify({'result': 'success', 'msg':'회원가입 완료!'})



# @app.route('/api/signup', methods=['POST'])
# def api_register():
#     id_receive = request.form['id_give']
#     pw_receive = request.form['pw_give']
#     nickname_receive = request.form['nickname_give']



#     pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

#     result = db.login.find_one({'id': id_receive})

#     if result is not None:
#         return jsonify({'result': 'fail', 'msg': '이미 존재하는 ID입니다!'})
#     else:
#         db.user.insert_one({'id': id_receive, 'pw': pw_hash, 'nick': nickname_receive})
#         return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5002, debug=True)
