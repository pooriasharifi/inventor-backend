from flask import Flask
from mongoengine import connect
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_mongoengine import MongoEngine

from Routs.user import user
from Routs.kala import kala
from Routs.request import requ
from Routs.all import all
from Routs.code import code


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "db": "myapp",
}
db = MongoEngine(app)





app.register_blueprint(user)
app.register_blueprint(kala)
app.register_blueprint(requ)
app.register_blueprint(all)
app.register_blueprint(code)

jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "@PZ-#22"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(host='127.0.0.1',debug=True)