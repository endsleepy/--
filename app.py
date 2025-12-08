# app.py
"""
Main Flask application file.

This version:
- Connects to a SQLite database using SQLAlchemy
- Creates the 'users' table from models.py
- Provides routes for:
    /              -> home page
    /login         -> login page (UI only for now)
    /accommodation -> rooms page
    /tickets       -> tickets page
    /register      -> sign-up (with actual database insert)
"""

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)
from werkzeug.security import generate_password_hash, check_password_hash

# Import the shared db object and the User model from models.py
from models import db, User

# -------------------------------------------------
# APP CONFIGURATION
# -------------------------------------------------
app = Flask(__name__)

# Path to SQLite database file (created automatically if it doesn't exist)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rza.db'

# Turn off a noisy feature we don't need
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Secret key is used for flashes + sessions (keep this private in real life)
app.config['SECRET_KEY'] = 'a_long_bankai_key_i_suppose'

# Attach SQLAlchemy to this Flask app
db.init_app(app)

# Create all tables defined in models.py (here: users)
# This runs once when the app starts.
with app.app_context():
    db.create_all()

# -------------------------------------------------
# ROUTES FOR STATIC PAGES
# -------------------------------------------------

@app.route('/')
def index():
    """Home page: renders the main landing page."""
    return render_template('index.html')


@app.route('/login')
def login():
    """Login page (only UI for now – authentication will be added later)."""
    return render_template('login.html')


@app.route('/accommodation')
def rooms():
    """Rooms / accommodation listing page."""
    return render_template('rooms.html')


@app.route('/tickets')
def tickets():
    """Tickets page."""
    return render_template('tickets.html')


# -------------------------------------------------
# SIGN-UP / REGISTRATION
# -------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Sign-up route.
    GET  -> show the form.
    POST -> validate input, create a new user record in the database.
    """

    error = None  # This will hold any validation error message

    if request.method == 'POST':
        # 1. Read data from the submitted form
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        # 2. Server-side validation (simple but exam-friendly)

        # Make sure required fields are not empty
        if not first_name or not last_name or not email or not password:
            error = "Please fill in all required fields."
        # Check passwords match
        elif password != confirm_password:
            error = "Passwords do not match."
        else:
            # 3. Check if the email already exists in the database
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                error = "An account with that email already exists."

        # 4. If there was no error, create the user
        if not error:
            # Join first and last name for 'full_name' field
            full_name = f"{first_name} {last_name}"

            # Hash the raw password using Werkzeug (pbkdf2 is default)
            password_hash = generate_password_hash(password)

            # Create a new User object (in memory only for now)
            new_user = User(
                full_name=full_name,
                email=email,
                password_hash=password_hash
                # join_date is set automatically by default=datetime.utcnow
            )

            # Stage the new user to be saved
            db.session.add(new_user)

            # Permanently save to the database file rza.db
            db.session.commit()

            # Give user feedback and redirect them to login page
            flash("Account created successfully. You can now log in.", "success")
            return redirect(url_for('login'))

        # If we reached here and error is not None, fall through to re-render form

    # For GET requests OR when validation fails, show the form again.
    # 'error' is passed into the template so it can display a message.
    return render_template('signup.html', error=error)


# -------------------------------------------------
# RUN APP
# -------------------------------------------------
if __name__ == "__main__":
    # debug=True reloads the app when you change the code (useful during development)
    app.run(debug=True)
