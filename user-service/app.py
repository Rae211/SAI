from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 注册逻辑
        return jsonify({"message": "User registered successfully"})
    return render_template('register.html', title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 登录逻辑
        return jsonify({"message": "User logged in successfully"})
    return render_template('login.html', title='Login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
