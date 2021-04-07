from flask import Flask
from devopswiki.views.index import bp as bp_index


app = Flask(__name__)

app.config.update(
    SECRET_KEY='abc123',
    TEMPLATES_AUTO_RELOAD=True
)

app.register_blueprint(bp_index)
