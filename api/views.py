from . import app
from flask import render_template, request, flash, redirect
import re
import smtplib
from email.message import EmailMessage


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/send_suggestion", methods=['GET', 'POST'])
def send_suggestion():
    if request.method == 'POST':
        text = re.sub(r"\s+", '', request.form['textarea'])
        if text != "":
            send_email(request.form['textarea'])
            return redirect("/")
        else:
            flash('Ваше предложение пустое')
    return render_template("send_suggestion.html")

def send_email(text):
    email_address = 'zona.otdiha.chernomorskoe@gmail.com'
    email_password = "sdsu ksjg pggn ymev"

    # create email
    msg = EmailMessage()
    msg['Subject'] = "Предложение о зоне отдыха"
    msg['From'] = email_address
    msg['To'] = 'zona.otdiha.chernomorskoe@gmail.com'
    msg.set_content(text)

    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/participants")
def participants():
    return render_template("participants.html")


@app.route("/about")
def about():
    return render_template("about.html")
