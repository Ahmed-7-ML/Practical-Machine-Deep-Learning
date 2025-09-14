from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'pass':
            return 'Login Successful!'
        else:
            return 'Invalid Credentials. Please try again.'
    elif request.method == 'GET':
        return '''
            <form method="post" action="/login">
                <input type="text" name="username" placeholder="Username">
                <input type="password" name="password" placeholder="Password"> 
                <input type="submit" value="Login">
            </form>
        '''


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)