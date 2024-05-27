from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class UserProfile(Resource):
    def get(self, user_id):
        # 返回用户个人资料
        return jsonify({"profile": f"Profile of user {user_id}"})

api.add_resource(UserProfile, '/profile/<int:user_id>')

@app.route('/')
def index():
    return jsonify({"message": "Profile Service is running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
