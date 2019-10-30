from app import create_app, db
from app.auth.models import User

if __name__ == '__main__':
    flask_app = create_app('dev')
    with flask_app.app_context():
        db.init_app(flask_app)
        if not User.query.filter_by(user_name='harry').first():
            User.create_user(user='harry', email='harry@hogwarts.com', password='secret')
    flask_app.run()
