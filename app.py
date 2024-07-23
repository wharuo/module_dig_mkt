from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import Config
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.profile import profile_bp
from routes.settings import settings_bp
from routes.export import export_bp

app = Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(settings_bp)
app.register_blueprint(export_bp)

if __name__ == '__main__':
    app.run(debug=True)
