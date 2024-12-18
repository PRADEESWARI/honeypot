from app import create_app, db, socketio
from app.models import FailedLogin
import os

app = create_app()


with app.app_context(): #database
    db.create_all()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
    socketio.run(app, debug=True)
