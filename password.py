import re

elif len(password) < 8:
    error = "Password must be at least 8 characters long."
elif not re.search(r"\d", password):
    error = "Password must include at least one number."
elif not re.search(r"[A-Z]", password):
    error = "Password must include at least one uppercase letter."
