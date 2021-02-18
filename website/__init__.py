from flask inmport Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "adastatr"

    return app
