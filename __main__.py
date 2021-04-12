from devopswiki.app import app
from devopswiki.config import config


if __name__ == '__main__':
    app.run(debug=True, host=config['host'])
