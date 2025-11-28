# Importing necessary modules from Flask
from flask import Flask, render_template

# Creating an instance of the Flask class for your web app
app = Flask(__name__)

# Defining the route for the home page (index)
@app.route('/')
def index():
    # When a user visits the home page, render 'index.html' template
    return render_template('index.html')

# Defining the route for the login page
@app.route('/login')
def login():
    # When a user visits the '/login' page, render 'login.html' template
    return render_template('login.html')

# Defining the route for the rooms page
@app.route('/rooms')
def rooms():
    # When a user visits the '/rooms' page, render 'rooms.html' template
    return render_template('rooms.html')

# Defining the route for the tickets page
@app.route('/tickets')
def tickets():
    # When a user visits the '/tickets' page, render 'tickets.html' template
    return render_template('tickets.html')

# Add any additional routes you might need in future versions
# Example for a profile page route
@app.route('/profile')
def profile():
    # When a user visits the '/profile' page, render 'profile.html' template
    return render_template('profile.html')

# Example for a dashboard route (if admin or user dashboard is required)
@app.route('/dashboard')
def dashboard():
    # When a user visits the '/dashboard' page, render 'dashboard.html' template
    return render_template('dashboard.html')

# The 'if' statement ensures that the application runs only if this script is executed directly
if __name__ == "__main__":
    # Running the Flask web server in debug mode (which automatically reloads the server when you make changes)
    app.run(debug=True)
