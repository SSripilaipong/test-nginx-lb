import os
from flask import Flask

app_id = os.environ.get('APP_ID', 0)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello from {app_id}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

