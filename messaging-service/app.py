from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Message(Resource):
    def post(self):
        # 处理消息发送
        return jsonify({"message": "Message sent successfully"})

api.add_resource(Message, '/message')

@app.route('/')
def index():
    return jsonify({"message": "Messaging Service is running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

