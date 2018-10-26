from werkzeug.serving import run_simple

from . import app

if __name__ == '__main__':
    run_simple('localhost', 5000, app,
               use_reloader=False, use_debugger=True, use_evalex=True)
