from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    print("GET /")
    return "Hello from " + str(datetime.now())

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), host='0.0.0.0')
