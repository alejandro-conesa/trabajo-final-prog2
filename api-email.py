from flask import Flask, request
from flask_mail import Message, Mail

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com' #server exclusivo de email
app.config['MAIL_PORT'] = 465 #puerto exclusivo para email
app.config['MAIL_USERNAME'] = 'easygesttest@gmail.com' #correo del usuario que envía
app.config['MAIL_PASSWORD'] = 'easy_gest238973' #contraseña del usuario que envía
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/home')
@app.route('/')
def home():
    if request.method == 'POST':
        msg = Message ('Hey!', sender='noreply@demo.com', recipients=['hugolopez2005@gmail,com'])
        msg.body = 'Hey Hugo!, how are you?'
        mail.send(msg)
        #pendiente de conectar con tkinter

if __name__ == '__main__':
    app.run(debug=True)