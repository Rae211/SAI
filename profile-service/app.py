from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # 资料更新逻辑
        return jsonify({"message": "Profile updated successfully"})
    return render_template('profile.html', title='Profile')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
