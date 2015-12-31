from flask.ext.api import FlaskAPI
from application.main.controllers import main
from application.admin.controllers import admin

app = FlaskAPI(__name__)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
