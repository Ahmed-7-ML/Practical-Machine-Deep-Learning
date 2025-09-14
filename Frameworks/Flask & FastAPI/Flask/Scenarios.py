from flask import Flask, request, render_template
# LocalHost = 127.0.0.1 or localhost

app = Flask(__name__)

# Scenario 1
@app.route('/')
def hello():
    return 'Hello, World!'
# --------------------------------

# Scenario 2
# @app.route('/<name>')
# def hello(name=None):
#     return f'Hello, {name}!'
# --------------------------------

# Scenario 3
@app.route('/user/<username>')
def user_profile(username):
    return f'User Profile: {username}'
# --------------------------------

# Scenario 4
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'
# --------------------------------

# Scenario 5
@app.route('/<name>')
def greet(name=None):
    return render_template('index.html', name=name)
# --------------------------------

# Scenario 6
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return f"Username: {request.form['username']}, Password: {request.form['password']}"
    else:
        return '''
            <form method="post" action="/login">
                <input type="text" name="username" placeholder="Username">
                <input type="password" name="password" placeholder="Password"> 
                <input type="submit" value="Login">
            </form>
        '''
# --------------------------------

# Main Application
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
