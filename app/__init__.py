from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

db = SQLAlchemy()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    
    # database connection
    app.config['SECRET_KEY'] = 'secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///honeypot.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    socketio.init_app(app)

    #Register blueprints
    from app.routes import main
    app.register_blueprint(main)

    return app
