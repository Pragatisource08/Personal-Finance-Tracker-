print("Starting the Application...")
from app import build_app
from app import db
app=build_app()
with app.app_context():
    db.create_all()
app.run(debug=True)