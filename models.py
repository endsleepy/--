# models.py
# This file defines the database models (tables) using SQLAlchemy.

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a single SQLAlchemy object that will be shared with the app
# app.py will call db.init_app(app)
db = SQLAlchemy()

class User(db.Model):
    """
    Users table
    -----------
    Matches the ERD + data dictionary:
    - user_id      INT, PK, auto-increment
    - full_name    VARCHAR(255), not null
    - email        VARCHAR(255), not null, unique
    - password_hash VARCHAR(255), not null
    - join_date    DATETIME, not null, default = time account created
    """
    __tablename__ = "users"

    # Primary key, auto-incrementing integer
    user_id = db.Column(db.Integer, primary_key=True)

    # Full name of the user (e.g. "Bob English")
    full_name = db.Column(db.String(255), nullable=False)

    # Email used for login + communication, must be unique
    email = db.Column(db.String(255), nullable=False, unique=True)

    # Hashed password (never store the raw password)
    password_hash = db.Column(db.String(255), nullable=False)

    # When the account was created (default = now)
    join_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        # Helpful when printing user objects while debugging
        return f"<User {self.user_id} {self.email}>"

# Later you can add models for:
# - HotelBooking
# - TicketBooking
# - LoyaltyPoints
# - Roles / UserRoles
# But for sign-up we only need User.
