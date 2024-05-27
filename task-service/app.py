from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Task(Resource):
    def post(self):
        # 处理任务创建
        return jsonify({"message": "Task created successfully"})

api.add_resource(Task, '/task')

@app.route('/')
def index():
    return jsonify({"message": "Task Service is running!"})

app = Flask(__name__)

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        task = request.form['task']
        # 创建任务逻辑
        return jsonify({"message": "Task created successfully"})
    return render_template('tasks.html', title='Tasks')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
