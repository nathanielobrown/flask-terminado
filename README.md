# flask-terminado
Integrates terminado with flask. This gives you a browser-based terminal with minimal effort.

## Limitations
Because the terminal requires websockets, your app can't be run as a WSGI app. Instead, the app should be served with `terminal.run`, rather than using your favorite webserver (gunicorn, uwsgi, waitress, etc.).

## Basic Example
```python
import flask
from flask_terminado import Terminal


app = flask.Flask(__name__)


@app.route('/')
def home():
    return 'home'


terminal = Terminal(app)
terminal.add_terminal('/bash', ['bash'])

if __name__ == '__main__':
    terminal.run(port=5000)
```

Head to [http://localhost:5000/bash](http://localhost:5000/bash) to see your terminal running.
