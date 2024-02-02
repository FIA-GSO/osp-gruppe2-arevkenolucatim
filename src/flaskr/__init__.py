import os
from flask import Flask, render_template
from . import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    @app.route('/hello')
    def hello():
        return render_template("index.html")

    db.init_app(app)

    return app