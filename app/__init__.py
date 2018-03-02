from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


from flask_sqlalchemy import SQLAlchemy
import os




login_manager = LoginManager()
login_manager.login_view = "login"
bootstrap = Bootstrap()
db = SQLAlchemy()


basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(name=__name__):
    app = Flask(name)
    bootstrap.init_app(app)
    app.config.update(
        DEBUG=True,
        SECRET_KEY=os.environ.get('SECRET_KEY', 'secret_xxx'),
        SQLALCHEMY_DATABASE_URI='sqlite:///' +
        os.path.join(basedir, 'data.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    )

    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
