from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class UserRegister(Resource):
    def post(self):
        # 处理用户注册
        return jsonify({"message": "User registered successfully"})

class UserLogin(Resource):
    def post(self):
        # 处理用户登录
        return jsonify({"message": "User logged in successfully"})

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')

@app.route('/')
def index():
    return jsonify({"message": "User Service is running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
@app.route('/user/profile')
def profile():
    # 处理用户个人资料页面的逻辑
    return render_template('profile.html')
