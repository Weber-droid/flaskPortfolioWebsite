from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mail import Mail, Message
from forms import ContactForm 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MAIL_SERVER'] = 'smtp.gmail.com' 
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'emmanueltotimeh2002@gmail.com'  
app.config['MAIL_PASSWORD'] = 'Jesselingard.2002' 


mail = Mail(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        recipient_email = 'emmanueltotimeh2002@gmail.com'  # Replace with your email address
        subject = 'New Message from your Portfolio Website'
        body = f'Name: {name}\nEmail: {email}\nMessage:\n{message}'

        msg = Message(subject=subject, recipients=[recipient_email], body=body)
        mail.send(msg)

        flash('Your message has been sent!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)