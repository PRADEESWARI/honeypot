from app import create_app, db, socketio
from app.models import FailedLogin

app = create_app()


with app.app_context(): #database
    db.create_all()

if __name__ == "__main__":
    socketio.run(app, debug=True)
