from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'POST':
        to_user = request.form['to_user']
        message = request.form['message']
        # 发送消息逻辑
        return jsonify({"message": "Message sent successfully"})
    return render_template('messages.html', title='Messages')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

import pika

def send_message(queue_name, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)
    connection.close()
