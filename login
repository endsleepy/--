# ---------------------------------------------
# LOGIN
# ---------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles user login.
    - GET  -> shows the login form
    - POST -> checks email + password, and logs the user in if details are correct
    """

    error = None  # This will hold any error message to display in the template

    if request.method == 'POST':
        # 1. Get form data from the login form
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        # 2. Basic validation (server-side)
        if not email or not password:
            error = "Please enter both email and password."
        else:
            # 3. Look for a user with this email in the database
            user = User.query.filter_by(email=email).first()

            if user is None:
                # No user found with that email
                error = "No account found with that email."
            else:
                # 4. Check the entered password against the stored password hash
                if check_password_hash(user.password_hash, password):
                    # 5. Password is correct -> log the user in using session
                    session['user_id'] = user.user_id
                    session['user_name'] = user.full_name  # from your Users table

                    flash(f"Welcome back, {user.full_name}!", "success")

                    # 6. Redirect to home or a dashboard page
                    # Change 'index' to 'dashboard' if you later create a dashboard route
                    return redirect(url_for('index'))
                else:
                    # Password is incorrect
                    error = "Incorrect password. Please try again."

    # For GET requests or if there was an error, show the login form again
    # 'error' is passed to the template so {{ error }} can display it
    return render_template('login.html', error=error)


# ---------------------------------------------
# LOGOUT
# ---------------------------------------------
@app.route('/logout')
def logout():
    """
    Logs the user out by clearing the session.
    """
    # Remove all data stored in the session (user id, name, etc.)
    session.clear()

    # Show feedback message
    flash("You have been logged out successfully.", "success")

    # Redirect back to home page
    return redirect(url_for('index'))


html - 
<input type="email" name="email" ...>
<input type="password" name="password" ...>
{% if error %}
  <p class="error-message">{{ error }}</p>
{% endif %}
    