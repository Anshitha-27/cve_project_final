from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
from extensions import db
from routes import app_routes  from flask_swagger_ui import get_swaggerui_blueprint  
def create_app():
    """Application Factory to create Flask app"""
    app = Flask(__name__)

    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cve_data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)      migrate = Migrate(app, db)  
  
    app.register_blueprint(app_routes)

    
    SWAGGER_URL = "/api/docs"
    API_URL = "/static/swagger.json"  # Path to your Swagger JSON file
    swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    return app  

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
