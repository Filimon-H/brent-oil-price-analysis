from flask import Flask
from flask_cors import CORS
from routes.changepoint import changepoint_bp

app = Flask(__name__)
CORS(app)  # ✅ Apply CORS to this one and only Flask app

app.register_blueprint(changepoint_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
