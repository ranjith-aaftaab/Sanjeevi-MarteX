from flask import Flask, render_template, request, flash,redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'Sanjeevi Constructions'  # Required for flash messages

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ranjithpython072@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'amus rjot xbzr unno'  # Use environment variable for security
app.config['MAIL_DEBUG'] = True


mail = Mail(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/submitform', methods=['GET', 'POST'])
def submitform():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('number')

        # Prepare email content
        subject = "Lead Enquiry"
        recipient = "ranjithmedigital@gmail.com"
        message_body = f"Name: {name}\nPhone: {phone}"

        # Send Email
        try:
            msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
            msg.body = message_body
            mail.send(msg)
            flash("Email sent successfully!", "success")
        except Exception as e:
            error_message = f"An error occurred while sending email: {str(e)}"
            flash(error_message, "danger")
    return render_template('index.html')

if __name__ == '__main__':
    app.run()