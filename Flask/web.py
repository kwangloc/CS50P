from flask import Flask, render_template
from flask_mail import Mail, Message
import config

app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = config.EMAIL,
    MAIL_PASSWORD = config.PASSWORD,
)
mail = Mail(app)

@app.route("/")
def index():
    # msg = Message("Hello",
    #               sender=config.EMAIL,
    #               body="Testing! This is the body",
    #               recipients=["snowball140902@gmail.com"])
    # mail.send(msg)
    # mail.send_message(msg)

    return render_template('main.html')

# to run the application
# export FLASK_APP = web.py
# flask run

if __name__ == "__main__":
    app.run(debug=True)
