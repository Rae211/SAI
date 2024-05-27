from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Notification(Resource):
    def post(self):
        # 处理通知发送
        return jsonify({"message": "Notification sent successfully"})

api.add_resource(Notification, '/notify')

@app.route('/')
def index():
    return jsonify({"message": "Notification Service is running!"})
def callback(ch, method, properties, body):
    print(f"Received {body}")
import pika
def callback(ch, method, properties, body):
    print(f"Received {body}")

def receive_messages(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print(f"Waiting for messages in {queue_name}. To exit press CTRL+C")
    channel.start_consuming()
    
@app.route('/notifications')
def notifications():
    # 获取通知逻辑
    return render_template('notifications.html', title='Notifications')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    receive_messages('message_queue')





