from flask import Flask
from config import config

app = Flask(__name__)


def create_app(config_name):
    app = Flask(__name__)
    from .index import index_blueprint
    from .color import color_blueprint
    app.register_blueprint(index_blueprint)
    app.register_blueprint(color_blueprint)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    @app.cli.command()
    def test():
        """Run the unit tests."""
        import unittest
        tests = unittest.TestLoader().discover('tests')
        unittest.TextTestRunner(verbosity=2).run(tests)

    return app
