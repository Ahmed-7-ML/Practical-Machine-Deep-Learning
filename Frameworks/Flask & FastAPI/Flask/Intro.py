# 1 Introduction
# 2 How to run in localhost with simple codes
# 3 Deep Learning model with Flask website
# 4 Machine Learning model with Flask website
# 5 Deployment

"""
Flask Framework: A micro web framework(collection of packages and modules) 
to write a web application or services 
without handling low-level details as protocols, sockets or threads.
"""
# Import the Flask class from the flask module
from flask import Flask

# Template rendering For HTML files
from flask import render_template

# To handle HTTP methods (GET, POST)
from flask import request


# Create an instance of the Flask class -> Object
app = Flask(__name__)

# Define a route for the root URL ("/") -> Decorator 
# To Bind a Function to a URL
@app.route('/')
def index():
    return 'Index Page!'

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # Show the user profile for that user
    return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Show the post with the given ID
    return f'Post {post_id}'


@app.route('/greeting')
@app.route('/greeting/<name>')
def greeting(name=None):
    # Render a template file (HTML)
    return render_template('greeting.html', name=name)

# <!doctype html>
# <title>Greeting Page</title>
# {% if name %}
#   <h1>Hello, {{ name }}</h1>
# {% else %}
#   <h1>Hello, World</h1>
# {% endif %}

@app.route('/Test', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        return f'Username : {request.form["username"]} '
    else:
        return '''<form method="post" action="/Test">
                <input type="text" name="username">
                <input type="submit" value="Submit">
            </form>'''

# Run the application -> Main method
if __name__ == '__main__':
    # Run the Flask development server -> localhost:5000
    app.run(host='localhost', port=5000)