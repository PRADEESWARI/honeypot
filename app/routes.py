from flask import Blueprint, render_template, request, redirect, url_for
from flask_socketio import emit
from . import db, socketio
from .models import FailedLogin
import datetime

main = Blueprint('main', __name__)

# Route for login
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        
        if username == 'admin' and password == 'password':
            return redirect(url_for('main.admin'))  
  
        elif username == 'user' and password == '12345':
            return redirect(url_for('main.home'))
  
        else:
            ip_address = request.remote_addr
            failed_login = FailedLogin(ip_address=ip_address, username=username)

        
            db.session.add(failed_login)
            db.session.commit()

        
            socketio.emit('alert', {
                'ip_address': ip_address,
                'username': username,
                'timestamp': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            })
            
            return redirect(url_for('main.fake_home')) 

    return render_template('login.html')


@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/fake_home')
def fake_home():
    return render_template('fake_home.html')

@main.route('/admin')
def admin():
    failed_logins = FailedLogin.query.order_by(FailedLogin.timestamp.desc()).all()
    return render_template('admin.html', failed_logins=failed_logins)
