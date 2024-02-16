import os
from flask import Flask, render_template
from . import db, auth, internal, public

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='database.db',
    )

    db.init_app(app)

    @app.route('/')
    def index():
        return render_template("index.html")

    app.register_blueprint(auth.bp)
    app.register_blueprint(internal.bp)
    app.register_blueprint(public.bp)

    return app