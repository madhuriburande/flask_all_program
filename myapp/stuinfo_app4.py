from first_flask import create_app,db
import os

config_name=os.getenv('FLASK_CONFIG','development')
app= create_app(config_name)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
