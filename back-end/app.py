from flask import Flask, render_template, redirect, url_for, session
from config.config import db


app = Flask(__name__, template_folder="../front-end/templates", static_folder="../front-end/static")
app.config.from_object('config.config.Config')

# db = SQLAlchemy(app)
db.init_app(app)

with app.app_context():
    from routes.account_routes import account_blueprint
    from routes.auth_routes import auth_blueprint
    from routes.card_routes import card_blueprint
    from routes.dashboard_routes import dashboard_blueprint
    from routes.relatorios_routes import relatorios_blueprint
    from routes.profile_routes import profile_blueprint
    
    app.register_blueprint(account_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(card_blueprint)
    app.register_blueprint(relatorios_blueprint)
    app.register_blueprint(profile_blueprint)

@app.route("/")
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard.dashboard'))
    else:
        return render_template("login.html")
    
if __name__ == "__main__":
    app.run(debug=True)
