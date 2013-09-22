from fastsnotsearch.app import app
from fastsnotsearch.default_settings import DEV_LISTEN_HOST, DEV_LISTEN_PORT, DEV_DEBUG

if __name__ == '__main__':
    app.debug=True
    app.run(host=DEV_LISTEN_HOST, port=DEV_LISTEN_PORT, debug=DEV_DEBUG)

