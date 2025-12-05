# ---------------------------------------------------------
# LOGIN SYSTEM (Version 5)
# ---------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():

    # If the login form is submitted
    if request.method == 'POST':

        # Collect form data
        email = request.form['email']               # User input email
        password = request.form['password']         # Entered password

        # Check if a user exists with this email
        user = User.query.filter_by(email=email).first()

        # If no account is found → stop login
        if not user:
            flash('No account exists with that email.', 'error')
            return redirect(url_for('login'))

        # Check if password matches stored hashed password
        password_match = bcrypt.check_password_hash(user.password, password)

        if password_match:
            # Store important user info in session for later pages
            session['user_id'] = user.id
            session['user_name'] = user.name
            session['user_role'] = user.role     # user / admin

            flash(f'Welcome back, {user.name}!', 'success')

            # Redirect based on role
            if user.role == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))

        else:
            flash('Incorrect password. Please try again.', 'error')
            return redirect(url_for('login'))

    # If simply viewing the login page
    return render_template('login.html')


# ---------------------------------------------------------
# LOGOUT SYSTEM
# ---------------------------------------------------------
@app.route('/logout')
def logout():

    # Remove everything stored in the session
    session.clear()

    flash('You have been logged out successfully.', 'success')

    # Redirect back to homepage
    return redirect(url_for('home'))
