{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    <div class="flash-container">
      {% for category, message in messages %}
        <div class="flash flash-{{ category }}">
          {{ message }}
        </div>
      {% endfor %}
    </div>
  {% endif %}
{% endwith %}


ccs 
.flash-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  padding: 0.5rem 0;
}

.flash {
  max-width: var(--container-width);
  margin: 0 auto;
  padding: 0.6rem 0.8rem;
  border-radius: 6px;
  font-size: 0.95rem;
}

/* Success = greenish */
.flash-success {
  background-color: #e0f7e9;
  color: #115827;
  border: 1px solid #9ad4ae;
}

/* Error = redish */
.flash-error {
  background-color: #fde4e4;
  color: #8b1a1a;
  border: 1px solid #f2a3a3;
}


flash("Account created successfully. You can now log in.", "success")
flash("Incorrect password. Please try again.", "error")
