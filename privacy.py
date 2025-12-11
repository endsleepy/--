<p class="copyright">
  © 2020 - 2025 RZA —
  <a href="{{ url_for('privacy') }}">Privacy</a> —
  <a href="{{ url_for('terms') }}">Terms</a>
</p>

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')


{% extends "base.html" %}
{% block title %}Privacy Policy{% endblock %}
{% block content %}
<main class="container">
  <h1>Privacy Policy</h1>
  <p>This placeholder explains how user data would be handled in a full system.</p>
</main>
{% endblock %}


{% extends "base.html" %}
{% block title %}Terms & Conditions{% endblock %}
{% block content %}
<main class="container">
  <h1>Terms & Conditions</h1>
  <p>Basic terms for using the Riget Zoo Adventures website will go here.</p>
</main>
{% endblock %}
