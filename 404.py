{% extends "base.html" %}

{% block title %}Page Not Found — RZA{% endblock %}

{% block content %}

<main class="error-layout">
    <section class="error-card">

        <h1 class="error-code">404</h1>
        <p class="error-message">Oops! The page you're looking for doesn't exist.</p>

        <a href="{{ url_for('index') }}" class="btn btn-primary error-btn">
            Go Back Home
        </a>

    </section>
</main>

{% endblock %}


/* -------------------------
   404 Error Page
-------------------------- */

.error-layout {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: calc(100vh - 160px);
    padding: 2rem 1rem;
}

.error-card {
    text-align: center;
    background: var(--surface);
    padding: 3rem 2.5rem;
    border-radius: 12px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    max-width: 420px;
}

.error-code {
    font-size: 6rem;
    font-weight: 800;
    color: var(--accent);
    margin-bottom: 0.5rem;
}

.error-message {
    font-size: 1.15rem;
    color: var(--muted);
    margin-bottom: 1.4rem;
}

.error-btn {
    margin-top: 1rem;
}

# ---------------------------------------------
# 404 ERROR HANDLER
# ---------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
